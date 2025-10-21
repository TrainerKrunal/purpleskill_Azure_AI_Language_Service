"""
Configuration module for Azure AI Language Service
Handles loading and validating environment variables for secure credential management.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_language_credentials():
    """
    Get Azure Language Service credentials from environment variables.
    
    Returns:
        tuple: (endpoint, key) for Azure Language Service
        
    Raises:
        ValueError: If required environment variables are missing
    """
    endpoint = os.getenv('AZURE_LANGUAGE_ENDPOINT')
    key = os.getenv('AZURE_LANGUAGE_KEY')
    
    if not endpoint:
        raise ValueError("AZURE_LANGUAGE_ENDPOINT environment variable is required")
    
    if not key:
        raise ValueError("AZURE_LANGUAGE_KEY environment variable is required")
    
    return endpoint, key

def validate_environment():
    """
    Validate that all required environment variables are set.
    
    Returns:
        bool: True if all required variables are present, False otherwise
    """
    try:
        get_language_credentials()
        return True
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("💡 Please check your .env file and ensure all required variables are set.")
        return False

# Configuration constants
DEFAULT_LANGUAGE = "en"
MAX_RETRY_ATTEMPTS = 3
REQUEST_TIMEOUT = 30

# Supported languages for language detection
SUPPORTED_LANGUAGES = [
    "en", "es", "fr", "de", "it", "pt", "ja", "ko", "zh", "ar", "hi", "ru"
]

def get_config_info():
    """
    Get configuration information for debugging.
    
    Returns:
        dict: Configuration information (without sensitive data)
    """
    endpoint, _ = get_language_credentials()
    
    return {
        "endpoint": endpoint,
        "key_configured": bool(os.getenv('AZURE_LANGUAGE_KEY')),
        "default_language": DEFAULT_LANGUAGE,
        "max_retry_attempts": MAX_RETRY_ATTEMPTS,
        "request_timeout": REQUEST_TIMEOUT,
        "supported_languages": len(SUPPORTED_LANGUAGES)
    }

# Legacy support for older config format
class LanguageConfig:
    def __init__(self):
        # Azure AI Language Service endpoint and key
        self.endpoint = os.getenv('AZURE_LANGUAGE_ENDPOINT')
        self.key = os.getenv('AZURE_LANGUAGE_KEY')
        
        # Validate configuration
        if not self.endpoint or not self.key:
            raise ValueError("Please set AZURE_LANGUAGE_ENDPOINT and AZURE_LANGUAGE_KEY environment variables")
    
    def get_language_credentials(self):
        """Returns language service credentials"""
        return {
            'endpoint': self.endpoint,
            'key': self.key
        }

# Create a global config instance
config = LanguageConfig()
