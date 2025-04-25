import os
import sys
import nltk

def download_resources():
    """Downloads required NLTK resources and sets up initial model."""
    print("Setting up FakeNewsDetector resources...")
    
    # Create model directory if it doesn't exist
    if not os.path.exists('model'):
        os.makedirs('model')
    
    # Download NLTK resources
    print("Downloading NLTK resources...")
    try:
        nltk.download('punkt')
        nltk.download('stopwords')
        print("NLTK resources downloaded successfully.")
    except Exception as e:
        print(f"Error downloading NLTK resources: {e}")
        print("Please make sure you have an internet connection and try again.")
        sys.exit(1)
    
    # Check if model exists, if not try to train it
    if not os.path.exists('model/fake_news_model.pkl'):
        print("Pre-trained model not found.")
        
        # Check if data exists to train a model
        if os.path.exists('data/fake_news.csv') and os.path.exists('data/real_news.csv'):
            print("Training data found. Attempting to train a new model...")
            try:
                from model.train_model import train_model
                train_model()
                print("Model training complete!")
            except Exception as e:
                print(f"Error training model: {e}")
                print("Please run train_model.py separately to train the model.")
        else:
            print("Training data not found.")
            print("Please run download_data.py first to download the training data.")
    else:
        print("Pre-trained model already exists.")
    
    print("\nSetup complete!")
    print("To run the application, use command: python app.py")

if __name__ == "__main__":
    download_resources()