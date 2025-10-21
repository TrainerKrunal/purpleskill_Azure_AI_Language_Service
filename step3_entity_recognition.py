"""
Step 3: Entity Recognition and Language Detection
This script demonstrates named entity recognition and language detection capabilities.
"""

import os
from config import get_language_credentials
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def recognize_entities():
    """Recognize named entities in text"""
    try:
        print("=" * 60)
        print("🏷️ AZURE LANGUAGE SERVICE - ENTITY RECOGNITION")
        print("=" * 60)
        
        # Get credentials and create client
        endpoint, key = get_language_credentials()
        client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )
        
        # Sample text with various entities
        sample_text = """
        Microsoft Corporation was founded by Bill Gates and Paul Allen on April 4, 1975.
        The company is headquartered in Redmond, Washington, and has offices in Seattle.
        In 2021, Microsoft acquired GitHub for $7.5 billion. The CEO Satya Nadella
        announced the Azure cloud platform expansion to serve customers worldwide.
        """
        
        print(f"\n📝 Sample text: {sample_text.strip()}")
        
        print("\n🔍 Recognizing named entities...")
        
        # Recognize entities
        response = client.recognize_entities(documents=[sample_text])
        
        if response and not response[0].is_error:
            print("\n🏷️ RECOGNIZED ENTITIES:")
            print("-" * 40)
            
            # Group entities by category
            entities_by_category = {}
            for entity in response[0].entities:
                category = entity.category
                if category not in entities_by_category:
                    entities_by_category[category] = []
                entities_by_category[category].append(entity)
            
            # Display entities by category
            for category, entities in entities_by_category.items():
                print(f"\n📂 {category.upper()}:")
                for entity in entities:
                    print(f"   • {entity.text} (confidence: {entity.confidence_score:.2f})")
                    if entity.subcategory:
                        print(f"     └─ Subcategory: {entity.subcategory}")
        else:
            print("❌ Error recognizing entities")
            
        return True
        
    except Exception as e:
        print(f"❌ Error in entity recognition: {str(e)}")
        return False

def detect_language():
    """Detect language of various text samples"""
    try:
        print("\n" + "=" * 60)
        print("🌍 LANGUAGE DETECTION")
        print("=" * 60)
        
        # Get credentials and create client
        endpoint, key = get_language_credentials()
        client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )
        
        # Sample texts in different languages
        sample_texts = [
            "Hello, how are you today?",
            "Bonjour, comment allez-vous?",
            "Hola, ¿cómo estás?",
            "Guten Tag, wie geht es Ihnen?",
            "こんにちは、元気ですか？",
            "Привет, как дела?",
            "Azure AI Language Service is amazing!"
        ]
        
        print("\n📝 Sample texts for language detection:")
        for i, text in enumerate(sample_texts, 1):
            print(f"{i}. {text}")
        
        print("\n🔍 Detecting languages...")
        
        # Detect languages
        response = client.detect_language(documents=sample_texts)
        
        print("\n🌍 LANGUAGE DETECTION RESULTS:")
        print("-" * 40)
        
        for idx, doc in enumerate(response):
            if not doc.is_error:
                language = doc.primary_language
                print(f"\n📄 Text {idx + 1}:")
                print(f"   Language: {language.name}")
                print(f"   ISO Code: {language.iso6391_name}")
                print(f"   Confidence: {language.confidence_score:.2f}")
            else:
                print(f"❌ Error detecting language for text {idx + 1}: {doc.error}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in language detection: {str(e)}")
        return False

def recognize_pii_entities():
    """Recognize Personally Identifiable Information (PII) entities"""
    try:
        print("\n" + "=" * 60)
        print("🔒 PII ENTITY RECOGNITION")
        print("=" * 60)
        
        # Get credentials and create client
        endpoint, key = get_language_credentials()
        client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )
        
        # Sample text with PII information
        sample_text = """
        John Smith lives at 123 Main Street, Seattle, WA 98101.
        His phone number is (555) 123-4567 and email is john.smith@email.com.
        His Social Security Number is 123-45-6789 and credit card number is 4111-1111-1111-1111.
        """
        
        print(f"\n📝 Sample text with PII: {sample_text.strip()}")
        
        print("\n🔍 Recognizing PII entities...")
        
        # Recognize PII entities
        response = client.recognize_pii_entities(documents=[sample_text])
        
        if response and not response[0].is_error:
            print("\n🔒 RECOGNIZED PII ENTITIES:")
            print("-" * 40)
            
            for entity in response[0].entities:
                print(f"   • {entity.text} → {entity.category}")
                print(f"     └─ Confidence: {entity.confidence_score:.2f}")
                if entity.subcategory:
                    print(f"     └─ Subcategory: {entity.subcategory}")
        else:
            print("❌ Error recognizing PII entities")
            
        return True
        
    except Exception as e:
        print(f"❌ Error in PII entity recognition: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting entity recognition and language detection demonstration...")
    
    # Run entity recognition
    if recognize_entities():
        print("\n✅ Entity recognition completed successfully!")
    
    # Run language detection
    if detect_language():
        print("\n✅ Language detection completed successfully!")
    
    # Run PII entity recognition
    if recognize_pii_entities():
        print("\n✅ PII entity recognition completed successfully!")
    
    print("\n🎉 Entity recognition and language detection demonstration complete!")
    print("💡 Real-world applications:")
    print("   - Content moderation and data protection")
    print("   - Multi-language content processing")
    print("   - Information extraction from documents")
    print("   - Automated data classification")
