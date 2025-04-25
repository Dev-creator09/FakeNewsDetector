import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download required NLTK resources
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

def preprocess_text(text):
    """
    Preprocesses text for the fake news detection model.
    
    Args:
        text (str): The raw text to preprocess
    
    Returns:
        str: The preprocessed text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    # Join tokens back into a string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

def extract_features(text):
    """
    Extracts basic features from text that might indicate fake news.
    
    Args:
        text (str): The news text
    
    Returns:
        dict: Dictionary of extracted features
    """
    features = {}
    
    # Length-based features
    features['text_length'] = len(text)
    features['word_count'] = len(text.split())
    
    # Count special characters
    features['exclamation_count'] = text.count('!')
    features['question_count'] = text.count('?')
    features['all_caps_count'] = len(re.findall(r'\b[A-Z]{2,}\b', text))
    
    # Sentiment indicators (simplified)
    positive_words = ['good', 'great', 'excellent', 'amazing', 'best', 'wonderful']
    negative_words = ['bad', 'worst', 'terrible', 'awful', 'horrible', 'poor']
    
    text_lower = text.lower()
    features['positive_word_count'] = sum(1 for word in positive_words if word in text_lower)
    features['negative_word_count'] = sum(1 for word in negative_words if word in text_lower)
    
    # Sensationalist language (simplified)
    clickbait_phrases = [
        'you won\'t believe', 'shocking', 'amazing', 'incredible', 
        'mind blowing', 'unbelievable', 'breaking', 'urgent'
    ]
    features['clickbait_phrase_count'] = sum(1 for phrase in clickbait_phrases if phrase in text_lower)
    
    return features