"""
Step 1: Azure Language Service Setup and Connection Test
This script tests the connection to Azure Language Service and verifies credentials.
"""

import os
import sys
from config import get_language_credentials
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def test_language_connection():
    """Test connection to Azure Language Service"""
    try:
        print("=" * 60)
        print("🔧 AZURE LANGUAGE SERVICE - CONNECTION TEST")
        print("=" * 60)
        
        # Get credentials
        print("\n📋 Loading configuration...")
        endpoint, key = get_language_credentials()
        
        print(f"✅ Endpoint: {endpoint}")
        print(f"✅ Key: {'*' * 20}{key[-4:]}")
        
        # Create client
        print("\n🔗 Creating Language Service client...")
        client = TextAnalyticsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )
        
        # Test with a simple text analysis
        print("\n🧪 Testing connection with sample text...")
        sample_text = "Hello, this is a test of Azure Language Service!"
        
        # Detect language
        response = client.detect_language(documents=[sample_text])
        
        if response:
            print("✅ Connection successful!")
            print(f"🌍 Detected language: {response[0].primary_language.name}")
            print(f"📊 Confidence: {response[0].primary_language.confidence_score:.2f}")
        else:
            print("❌ Connection failed - no response received")
            return False
            
        print("\n🎉 Azure Language Service is ready!")
        print("✨ You can now run the other demo scripts.")
        
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Check your .env file has correct AZURE_LANGUAGE_ENDPOINT and AZURE_LANGUAGE_KEY")
        print("2. Verify your Azure Language Service resource is active")
        print("3. Ensure your API key is valid and not expired")
        print("4. Check your internet connection")
        return False

if __name__ == "__main__":
    success = test_language_connection()
    if not success:
        sys.exit(1)
