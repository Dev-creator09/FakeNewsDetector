import numpy as np
from .utils import preprocess_text

def predict_fake_news(text, model, vectorizer):
    """
    Predicts whether the given news text is fake or real.
    
    Args:
        text (str): The news article text to analyze
        model: The trained machine learning model
        vectorizer: The trained text vectorizer
    
    Returns:
        tuple: (prediction label, confidence score)
    """
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Vectorize the text
    text_vector = vectorizer.transform([processed_text])
    
    # Make prediction
    prediction_proba = model.predict_proba(text_vector)[0]
    prediction = model.predict(text_vector)[0]
    
    # Get confidence score
    # If prediction is 1 (fake), use that probability
    # If prediction is 0 (real), use the inverse probability
    confidence = prediction_proba[1] if prediction == 1 else prediction_proba[0]
    confidence = float(confidence) * 100  # Convert to percentage
    
    # Format the output
    label = "Likely Fake" if prediction == 1 else "Likely Real"
    
    return label, round(confidence, 2)

def get_explanation(text, model, vectorizer):
    """
    Provides a simple explanation for the prediction.
    
    Args:
        text (str): The news article text
        model: The trained machine learning model
        vectorizer: The trained text vectorizer
    
    Returns:
        str: A simple explanation for the prediction
    """
    # This is a simplified implementation
    # In a more advanced version, you could:
    # - Use LIME or SHAP for feature importance
    # - Highlight suspicious phrases
    # - Compare with known fake news patterns
    
    # For this simplified version, we'll just check for some common indicators
    common_fake_indicators = [
        'shocking', 'you won\'t believe', 'secret', 'conspiracy',
        'they don\'t want you to know', 'miracle', 'explosive',
        'bombshell', 'stunning'
    ]
    
    text_lower = text.lower()
    found_indicators = [word for word in common_fake_indicators 
                       if word in text_lower]
    
    if found_indicators:
        indicators_text = ", ".join(found_indicators)
        return f"This text contains potentially sensationalist terms: {indicators_text}"
    else:
        return "No specific red flags detected in the text. Prediction is based on the overall language patterns."