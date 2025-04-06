import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

load_dotenv()

def get_breed_info_from_gemini(breed_name, language_code='en'):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Updated prompts with clear sections for UI integration
    prompts = {
        "Overview": f"Give a short overview of the {breed_name} breed including its origin and appearance. Be concise and helpful for rural farmers.",
        "Region & Adaptability": f"Describe the regions where {breed_name} cattle are common and the climates they adapt well to.",
        "Milk Production & Use": f"How much milk does a {breed_name} cow yield on average, and what is its typical use (e.g., commercial, household)?",
        "Care Tips": f"List 2-3 care tips for maintaining the health and productivity of a {breed_name} cow, including feeding and disease prevention.",
        "Fun Fact": f"Share an interesting cultural or historical fact about the {breed_name} breed."
    }

    breed_info = {}

    for title, eng_prompt in prompts.items():
        try:
            # Step 1: Generate English response
            response = model.generate_content(eng_prompt)
            english_text = re.sub(r'[\*\#\[\]\(\)\`\~\_\+\=\>\|\{\}]', '', response.text).strip()

            # Step 2: Translate if needed
            if language_code != 'en':
                translate_prompt = f"Translate the following to {language_code}, keep it friendly and simple:\n{english_text}"
                translated_response = model.generate_content(translate_prompt)
                translated_text = re.sub(r'[\*\#\[\]\(\)\`\~\_\+\=\>\|\{\}]', '', translated_response.text).strip()
            else:
                translated_text = english_text

            breed_info[title] = translated_text
            print(f"{title}: {translated_text}")

        except Exception as e:
            breed_info[title] = f"Error: {str(e)}"
            print(f"Error for {title}: {e}")

    return breed_info, breed_name, language_code