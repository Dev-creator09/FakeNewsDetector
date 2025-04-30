# AI Fake News Detector

A web application that uses machine learning to analyze news article text and predict whether it might be fake or real news.

## Project Overview

This project uses Natural Language Processing (NLP) and machine learning to analyze text content of news articles and classify them as potentially fake or legitimate. It's designed to demonstrate how basic AI techniques can be applied to the real-world problem of misinformation detection.

### Features

- Text analysis of news articles using NLP techniques
- Machine learning classification (real vs. fake news)
- User-friendly web interface
- Confidence score with visual indicator
- API endpoints for programmatic access

## Technologies Used

- **Backend**: Python with Flask web framework
- **Machine Learning**: scikit-learn (RandomForest classifier)
- **NLP Processing**: NLTK for text preprocessing
- **Data Storage**: Simple file-based storage with joblib
- **Frontend**: HTML, CSS, JavaScript for responsive UI
- **Development**: Git/GitHub for version control

## How It Works

1. **Text Preprocessing**: The system cleans and standardizes input text through:

   - Removing punctuation, URLs, and HTML tags
   - Converting text to lowercase
   - Tokenization (breaking text into words)
   - Removing stopwords (common words like "the", "and")
   - Stemming (reducing words to their root form)

2. **Feature Extraction**: The processed text is converted to numerical features using:

   - Bag-of-words representation
   - TF-IDF vectorization to identify important words

3. **Classification**: A RandomForest classifier analyzes these features to predict if the content resembles patterns found in fake news.

4. **Result Analysis**: The system provides a prediction with a confidence score and explanation.

## Implementation Details

### Machine Learning Model

The system uses a RandomForest classifier trained on a dataset of labeled real and fake news articles. This ensemble learning method was chosen for its:

- Effectiveness with text classification tasks
- Resistance to overfitting
- Ability to handle the high dimensionality of text data

### NLP Pipeline

The text processing pipeline includes:

1. Text cleaning (URL removal, HTML stripping)
2. Tokenization using NLTK
3. Stopword removal
4. Stemming with Porter Stemmer
5. Vectorization using scikit-learn's CountVectorizer

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/YOUR-USERNAME/FakeNewsDetector.git
   cd FakeNewsDetector
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up NLTK resources:

   ```
   python download_nltk.py
   ```

5. Generate sample data:

   ```
   python download_data.py
   ```

6. Train the model:

   ```
   python -m model.train_model
   ```

7. Run the application:

   ```
   python app.py
   ```

8. Open your browser and go to `http://localhost:5000`

## Project Structure

```
FakeNewsDetector/
├── app.py                  # Main Flask application
├── model/
│   ├── __init__.py
│   ├── predict.py          # Functions for making predictions
│   ├── train_model.py      # Script to train the model
│   └── utils.py            # Helper functions for text processing
├── data/
│   ├── fake_news.csv       # Dataset of fake news articles
│   └── real_news.csv       # Dataset of real news articles
├── static/
│   ├── css/
│   │   └── style.css       # Application styling
│   └── js/
│       └── main.js         # Frontend JavaScript
├── templates/
│   ├── index.html          # Homepage template
│   └── result.html         # Results page template
├── download_data.py        # Script to generate sample data
├── download_nltk.py        # Script to download NLTK resources
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## API Usage

The application provides a simple API for programmatic access:

### Analyze Text

**Endpoint:** `/api/analyze`

**Method:** POST

**Request Body:**

```json
{
  "text": "Your news article text here"
}
```

**Response:**

```json
{
  "prediction": "Likely Fake",
  "confidence": 85.7,
  "text": "Your news article text here..."
}
```

### Submit Feedback

**Endpoint:** `/api/feedback`

**Method:** POST

**Request Body:**

```json
{
  "text": "Article text",
  "prediction": "Likely Fake",
  "user_label": "fake"
}
```

**Response:**

```json
{
  "status": "success",
  "message": "Feedback received"
}
```

## Educational Purpose

This project is developed for educational purposes to demonstrate:

- How machine learning can be applied to text classification
- Basic NLP techniques for text preprocessing
- Full-stack web application development with Flask
- Building a complete data science project pipeline

The model is trained on a limited dataset and should not be used as a definitive fake news detector.

## Future Improvements

- Implement more advanced NLP features (named entity recognition, sentiment analysis)
- Add URL input to analyze articles directly from the web
- Improve the model with larger, more diverse datasets
- Add user accounts to save analysis history
- Implement more sophisticated classification algorithms (BERT, transformers)
- Add detailed explanations for why content might be classified as fake

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by research in misinformation detection
- Built with open-source tools and libraries
- Created for educational purposes
