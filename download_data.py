import os
import pandas as pd
import urllib.request
import csv
import random
import string

def download_data():
    """
    Downloads or creates sample data for the fake news detector.
    
    Since we're building a simplified version, instead of downloading 
    large datasets from external sources, we'll create a small sample
    dataset that simulates fake and real news.
    """
    print("Setting up data for the Fake News Detector...")
    
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Check if data already exists
    if os.path.exists('data/fake_news.csv') and os.path.exists('data/real_news.csv'):
        print("Data files already exist.")
        return
    
    print("Creating sample datasets...")
    
    # Sample fake news articles - These are completely made up examples for educational purposes
    fake_news_samples = [
        "BREAKING: Scientists Discover Secret Microchips in COVID Vaccines That Track Your Location",
        "SHOCKING: Famous Celebrity Found to Be an Alien in Disguise, Government Confirms",
        "URGENT: Study Shows Drinking Water Causes Cancer - Government Hiding the Truth",
        "REVEALED: Secret Government Program Can Control Weather and Caused Recent Hurricanes",
        "ALERT: New Study Finds Link Between Common Fruit and Memory Loss - Doctors Stunned",
        "EXCLUSIVE: World Leader Caught on Tape Admitting New World Order Plans",
        "BOMBSHELL: Whistleblower Reveals Fast Food Companies Add Addictive Chemicals Not Listed in Ingredients",
        "INCREDIBLE: Man Lives to 150 Years Using This One Simple Trick Doctors Don't Want You to Know",
        "TERRIFYING: 5G Towers Actually Mind Control Devices, Engineer Confesses",
        "EXPOSED: Major Bank Deliberately Crashing Economy, Inside Sources Reveal",
        "UNBELIEVABLE: Scientists Find Evidence Earth is Actually Flat, NASA Lies Exposed",
        "DANGER: Common Household Item Found to Cause Instant Death in New Study",
        "SECRET REVEALED: Hollywood Stars Drinking Children's Blood to Stay Young",
        "BREAKING: Major City Discovered to Be Entirely Populated by Robots",
        "BEWARE: Government Putting Mind-Altering Substances in Airplane Contrails",
        "SCANDAL: Famous Politician Revealed to Be Three Children in a Trenchcoat",
        "ALERT: Your Smartphone is Recording Everything You Say and Selling it to Advertisers",
        "SHOCKING: Scientists Discover Vaccine Makes People Magnetic - Covered Up by Media",
        "URGENT: Research Shows Tap Water Contains Mind-Control Chemicals from Government",
        "EXCLUSIVE: Antarctica is Actually a Giant Wall Hiding the Edge of Our Flat Earth"
    ]
    
    # Sample real news headlines and content - These are generic examples for educational purposes
    real_news_samples = [
        "Local Community Raises Funds for New Public Library Opening Next Month",
        "Study Finds Regular Exercise May Improve Cognitive Function in Older Adults",
        "City Council Approves New Infrastructure Project to Repair Aging Bridges",
        "Scientists Identify Potential New Treatment Option for Type 2 Diabetes",
        "Local Farm Introduces Sustainable Farming Practices, Reduces Water Usage",
        "School Board Votes to Increase Teacher Salaries by 3% Next Academic Year",
        "Research Shows Benefits of Mediterranean Diet for Heart Health",
        "New Public Transportation Route to Connect Downtown with Western Suburbs",
        "Company Announces Plan to Reduce Carbon Emissions by 30% by 2030",
        "University Researchers Develop More Efficient Solar Panel Technology",
        "City Parks Department Plants 500 New Trees in Urban Neighborhoods",
        "National Weather Service Predicts Above Average Rainfall This Spring",
        "Local Restaurant Wins Regional Culinary Award for Third Consecutive Year",
        "Health Department Issues Guidelines for Preventing Seasonal Flu",
        "International Trade Agreement Expected to Boost Agricultural Exports",
        "State Legislature Passes Bill to Fund Road Improvements Across County",
        "Survey Finds Increasing Job Satisfaction Among Remote Workers",
        "Nonprofit Organization Opens New Homeless Shelter Downtown",
        "Researchers Discover New Species of Deep-Sea Fish Off the Pacific Coast",
        "Local High School Math Team Wins State Championship"
    ]
    
    # Generate longer content for each headline
    def generate_article_content(headline, is_fake=False):
        # Start with the headline
        content = headline + "\n\n"
        
        # Add 3-5 paragraphs
        paragraphs = random.randint(3, 5)
        
        for i in range(paragraphs):
            # Generate a paragraph of 3-8 sentences
            sentences = random.randint(3, 8)
            paragraph = ""
            
            for j in range(sentences):
                # Generate a sentence of 10-20 words
                word_count = random.randint(10, 20)
                words = []
                
                for k in range(word_count):
                    # Random word length between 3-10 characters
                    word_length = random.randint(3, 10)
                    word = ''.join(random.choice(string.ascii_lowercase) for _ in range(word_length))
                    words.append(word)
                
                sentence = ' '.join(words).capitalize() + '. '
                paragraph += sentence
            
            content += paragraph + "\n\n"
        
        # Add some stylistic elements for fake news if applicable
        if is_fake:
            # Add some common fake news phrases
            fake_phrases = [
                "The mainstream media won't report this!",
                "What they don't want you to know...",
                "Scientists are shocked!",
                "This information is being suppressed.",
                "Share before they take this down!",
                "The truth is finally revealed!"
            ]
            
            content += random.choice(fake_phrases) + "\n\n"
            
            # Add excessive punctuation and capitalization
            if random.random() > 0.5:
                content = content.replace(".", "!!!").replace("?", "???")
            
            # Add more sensationalist language
            if random.random() > 0.7:
                content = content.upper()
        
        return content
    
    # Create fake news dataset
    fake_articles = []
    for headline in fake_news_samples:
        article = generate_article_content(headline, is_fake=True)
        fake_articles.append({'text': article, 'label': 1})
    
    # Create real news dataset
    real_articles = []
    for headline in real_news_samples:
        article = generate_article_content(headline, is_fake=False)
        real_articles.append({'text': article, 'label': 0})
    
    # Save to CSV files
    fake_df = pd.DataFrame(fake_articles)
    real_df = pd.DataFrame(real_articles)
    
    fake_df.to_csv('data/fake_news.csv', index=False)
    real_df.to_csv('data/real_news.csv', index=False)
    
    print("Sample data created successfully.")
    print(f"- {len(fake_articles)} fake news articles in data/fake_news.csv")
    print(f"- {len(real_articles)} real news articles in data/real_news.csv")
    print("\nNote: This is a small, generated dataset for educational purposes.")
    print("For a real project, you would use larger, established datasets.")

if __name__ == "__main__":
    download_data()