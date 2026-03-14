import os
import logging
from dotenv import load_dotenv
from cognitext.core import CogniTextEngine

load_dotenv()

def main():
    print("--- CogniText AI Orchestration Demo ---")
    
    # 1. Validate Environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env file.")
        return

    # 2. Initialize Engine
    engine = CogniTextEngine(api_key=api_key)

    # 3. Sample Text (e.g., a customer feedback)
    sample_text = \"\"\"
    I've been using your mobile banking app for 3 months now. 
    The biometric login is extremely fast and I love the new dark mode. 
    However, the transaction history takes too long to load on 4G networks. 
    It would be great if you could add a spending tracker feature.
    \"\"\"

    print(f"📄 Analyzing Text: {sample_text[:100]}...")
    
    try:
        # 4. Execute Structured Analysis
        result = engine.analyze(sample_text)
        
        print("\n✅ AI ANALYSIS RESULTS:")
        print(f"📊 Sentiment: {result.sentiment}")
        print(f"📝 Summary: {result.summary}")
        print(f"📌 Key Points: {', '.join(result.key_points)}")
        if result.suggested_actions:
            print(f"💡 Suggested Actions: {', '.join(result.suggested_actions)}")
            
    except Exception as e:
        print(f"❌ Failed to process analysis: {str(e)}")

if __name__ == "__main__":
    main()