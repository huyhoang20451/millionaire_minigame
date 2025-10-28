"""
Test script for Gemini AI Support
This demonstrates how the AI support uses the explanation field to provide accurate hints
"""

import os
from dotenv import load_dotenv
from ai_support import GeminiAISupport

# Load environment variables
load_dotenv()

def test_ai_support():
    print("=" * 70)
    print("Testing Gemini AI Support for Millionaire Game")
    print("=" * 70)
    
    # Check if API key is available
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("\n⚠️  WARNING: GEMINI_API_KEY not found in environment variables!")
        print("To test the AI support:")
        print("1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("2. Create a .env file (copy from .env.example)")
        print("3. Add your API key: GEMINI_API_KEY=your_key_here")
        print("\nRunning fallback mode demo instead...\n")
        
        # Demo with fallback
        ai_support = GeminiAISupport.__new__(GeminiAISupport)
        explanation = "Paris is the capital and most populous city of France. It has been the country's capital since the 12th century."
        fallback_hint = ai_support.get_simple_hint(explanation)
        print(f"Fallback Hint: {fallback_hint}")
        return
    
    try:
        # Initialize AI Support
        print("\n✓ Initializing Gemini AI Support...")
        ai_support = GeminiAISupport(api_key=api_key)
        print("✓ Successfully connected to Gemini API\n")
        
        # Test Question 1: Paris
        print("=" * 70)
        print("TEST 1: Geography Question")
        print("=" * 70)
        
        question1 = "What is the capital of France?"
        answers1 = {
            1: "London",
            2: "Berlin",
            3: "Paris",
            4: "Madrid"
        }
        explanation1 = "Paris is the capital and most populous city of France. It has been the country's capital since the 12th century and is located in the north-central part of the country along the Seine River."
        
        print(f"\nQuestion: {question1}")
        print("Options:")
        for i, ans in answers1.items():
            print(f"  {chr(64+i)}) {ans}")
        
        print(f"\n📚 Verified Facts (from questions.json):")
        print(f"   {explanation1}")
        
        print("\n🤖 AI-Generated Hint:")
        hint1 = ai_support.get_ai_hint(question1, answers1, explanation1)
        print(f"   {hint1}")
        
        # Test Question 2: Mona Lisa
        print("\n" + "=" * 70)
        print("TEST 2: Art History Question")
        print("=" * 70)
        
        question2 = "Who painted the Mona Lisa?"
        answers2 = {
            1: "Vincent van Gogh",
            2: "Leonardo da Vinci",
            3: "Pablo Picasso",
            4: "Michelangelo"
        }
        explanation2 = "Leonardo da Vinci painted the Mona Lisa between 1503 and 1519. It is one of the most famous paintings in the world and is housed in the Louvre Museum in Paris. The painting is renowned for the subject's enigmatic smile and da Vinci's masterful technique."
        
        print(f"\nQuestion: {question2}")
        print("Options:")
        for i, ans in answers2.items():
            print(f"  {chr(64+i)}) {ans}")
        
        print(f"\n📚 Verified Facts (from questions.json):")
        print(f"   {explanation2}")
        
        print("\n🤖 AI-Generated Hint:")
        hint2 = ai_support.get_ai_hint(question2, answers2, explanation2)
        print(f"   {hint2}")
        
        print("\n" + "=" * 70)
        print("✓ AI Support Test Completed Successfully!")
        print("=" * 70)
        print("\nNote: The AI hints are based on the verified explanations from")
        print("questions.json, ensuring accurate information without giving away")
        print("the answer directly.")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPlease check your API key and internet connection.")

if __name__ == "__main__":
    test_ai_support()
