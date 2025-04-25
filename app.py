from flask import Flask, render_template, request, jsonify
import os
import joblib
from model.predict import predict_fake_news
from model.utils import preprocess_text

app = Flask(__name__)

# Load model
try:
    # Check if model exists, otherwise we'll train a new one
    if os.path.exists('model/fake_news_model.pkl'):
        model = joblib.load('model/fake_news_model.pkl')
        vectorizer = joblib.load('model/vectorizer.pkl')
    else:
        print("Model files not found. Run train_model.py first.")
        # Import and run training script if model doesn't exist
        from model.train_model import train_model
        model, vectorizer = train_model()
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    vectorizer = None

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Process text and return prediction."""
    if request.method == 'POST':
        # Get text from form or API
        if request.content_type == 'application/json':
            data = request.get_json()
            news_text = data.get('text', '')
        else:
            news_text = request.form.get('news_text', '')
        
        if not news_text:
            return render_template('result.html', 
                                  prediction="Error: No text provided",
                                  confidence=0,
                                  text="Please provide text to analyze")
        
        # Preprocess text and make prediction
        try:
            # Check if model is loaded
            if model is None or vectorizer is None:
                return render_template('result.html',
                                      prediction="Error: Model not loaded",
                                      confidence=0,
                                      text=news_text)
            
            # Make prediction
            prediction, confidence = predict_fake_news(news_text, model, vectorizer)
            
            # Return the result
            if request.content_type == 'application/json':
                return jsonify({
                    'prediction': prediction,
                    'confidence': confidence,
                    'text': news_text[:100] + '...' if len(news_text) > 100 else news_text
                })
            else:
                return render_template('result.html',
                                      prediction=prediction,
                                      confidence=confidence,
                                      text=news_text)
        
        except Exception as e:
            error_message = f"Error making prediction: {str(e)}"
            if request.content_type == 'application/json':
                return jsonify({'error': error_message}), 500
            else:
                return render_template('result.html',
                                      prediction="Error",
                                      confidence=0,
                                      text=error_message)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    """API endpoint for text analysis."""
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'Missing text parameter'}), 400
    
    try:
        prediction, confidence = predict_fake_news(data['text'], model, vectorizer)
        return jsonify({
            'prediction': prediction,
            'confidence': confidence,
            'text': data['text'][:100] + '...' if len(data['text']) > 100 else data['text']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/feedback', methods=['POST'])
def api_feedback():
    """API endpoint for user feedback on predictions."""
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    required_fields = ['text', 'prediction', 'user_label']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # In a real application, you would store this feedback to improve the model
    # For this simplified version, we'll just acknowledge receipt
    return jsonify({'status': 'success', 'message': 'Feedback received'})

if __name__ == '__main__':
    # For development
    app.run(debug=True)