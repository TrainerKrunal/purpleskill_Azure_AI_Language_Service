"""
Step 2: Text Analysis and Sentiment Detection
This script demonstrates text analysis capabilities including sentiment analysis,
key phrase extraction, and entity recognition.
"""

import os
from config import get_language_credentials
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def analyze_text_sentiment():
    """Analyze sentiment of sample texts"""
    try:
        print("=" * 60)
        print("🧠 AZURE LANGUAGE SERVICE - SENTIMENT ANALYSIS")
        print("=" * 60)
        
        # Get credentials and create client
        endpoint, key = get_language_credentials()
        client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )
        
        # Sample texts for analysis
        sample_texts = [
            "I love using Azure AI services! They make development so much easier.",
            "The weather is terrible today, I'm feeling quite disappointed.",
            "This is a neutral statement about technology and programming.",
            "Azure Language Service provides amazing natural language processing capabilities!"
        ]
        
        print("\n📝 Sample texts for analysis:")
        for i, text in enumerate(sample_texts, 1):
            print(f"{i}. {text}")
        
        print("\n🔍 Analyzing sentiment...")
        
        # Analyze sentiment
        response = client.analyze_sentiment(documents=sample_texts)
        
        print("\n📊 SENTIMENT ANALYSIS RESULTS:")
        print("-" * 40)
        
        for idx, doc in enumerate(response):
            if not doc.is_error:
                print(f"\n📄 Text {idx + 1}:")
                print(f"   Sentiment: {doc.sentiment.upper()}")
                print(f"   Confidence Scores:")
                print(f"     - Positive: {doc.confidence_scores.positive:.2f}")
                print(f"     - Neutral:  {doc.confidence_scores.neutral:.2f}")
                print(f"     - Negative: {doc.confidence_scores.negative:.2f}")
                
                # Show sentence-level sentiment
                if doc.sentences:
                    print(f"   Sentence-level sentiment:")
                    for sentence in doc.sentences:
                        print(f"     - '{sentence.text[:50]}...' → {sentence.sentiment}")
            else:
                print(f"❌ Error analyzing text {idx + 1}: {doc.error}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in sentiment analysis: {str(e)}")
        return False

def extract_key_phrases():
    """Extract key phrases from text"""
    try:
        print("\n" + "=" * 60)
        print("🔑 KEY PHRASE EXTRACTION")
        print("=" * 60)
        
        # Get credentials and create client
        endpoint, key = get_language_credentials()
        client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )
        
        # Sample text for key phrase extraction
        sample_text = """
        Azure AI Language Service is a cloud-based service that provides 
        Natural Language Processing (NLP) features for understanding and 
        analyzing text. It offers sentiment analysis, key phrase extraction, 
        language detection, and named entity recognition capabilities.
        """
        
        print(f"\n📝 Sample text: {sample_text.strip()}")
        
        print("\n🔍 Extracting key phrases...")
        
        # Extract key phrases
        response = client.extract_key_phrases(documents=[sample_text])
        
        if response and not response[0].is_error:
            print("\n🔑 EXTRACTED KEY PHRASES:")
            print("-" * 30)
            for phrase in response[0].key_phrases:
                print(f"   • {phrase}")
        else:
            print("❌ Error extracting key phrases")
            
        return True
        
    except Exception as e:
        print(f"❌ Error in key phrase extraction: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting text analysis demonstration...")
    
    # Run sentiment analysis
    if analyze_text_sentiment():
        print("\n✅ Sentiment analysis completed successfully!")
    
    # Run key phrase extraction
    if extract_key_phrases():
        print("\n✅ Key phrase extraction completed successfully!")
    
    print("\n🎉 Text analysis demonstration complete!")
    print("💡 Real-world applications:")
    print("   - Customer feedback analysis")
    print("   - Social media monitoring")
    print("   - Document summarization")
    print("   - Content classification")
