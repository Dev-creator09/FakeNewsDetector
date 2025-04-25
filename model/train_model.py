import os
import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from .utils import preprocess_text

def train_model(save_model=True, data_path='data'):
    """
    Trains a fake news detection model using the provided datasets.
    
    Args:
        save_model (bool): Whether to save the trained model to disk
        data_path (str): Path to the data directory
    
    Returns:
        tuple: The trained model and vectorizer
    """
    print("Loading and preparing data...")
    
    # Check if datasets exist
    fake_news_path = os.path.join(data_path, 'fake_news.csv')
    real_news_path = os.path.join(data_path, 'real_news.csv')
    
    if not os.path.exists(fake_news_path) or not os.path.exists(real_news_path):
        raise FileNotFoundError(f"Dataset files not found. Please run download_data.py first.")
    
    # Load datasets
    fake_df = pd.read_csv(fake_news_path)
    real_df = pd.read_csv(real_news_path)
    
    # Add labels
    fake_df['label'] = 1  # 1 for fake news
    real_df['label'] = 0  # 0 for real news
    
    # Combine datasets
    df = pd.concat([fake_df, real_df], ignore_index=True)
    
    # Shuffle data
    df = df.sample(frac=1).reset_index(drop=True)
    
    # Preprocess text
    print("Preprocessing text...")
    df['processed_text'] = df['text'].apply(preprocess_text)
    
    # Split data
    X = df['processed_text']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create TF-IDF vectorizer
    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    
    # Train model
    print("Training model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_vectorized, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_vectorized)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    print(f"Model Evaluation:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"Confusion Matrix:")
    print(conf_matrix)
    
    # Save model
    if save_model:
        print("Saving model...")
        os.makedirs('model', exist_ok=True)
        joblib.dump(model, 'model/fake_news_model.pkl')
        joblib.dump(vectorizer, 'model/vectorizer.pkl')
        print("Model saved successfully.")
    
    return model, vectorizer

if __name__ == "__main__":
    # If run directly, train and save the model
    train_model()