import os
import base64
from io import BytesIO
from PIL import Image
import openai
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def get_artifact_info(image):
    """
    Identify museum artifact and generate a 3-sentence fascinating story.
    
    Args:
        image: PIL Image object or file-like object
        
    Returns:
        str: 3-sentence story with <#0.5#> tags between sentences
    """
    vision_service = os.getenv('VISION_SERVICE', 'openai').lower()
    
    if vision_service == 'openai':
        return _get_artifact_info_openai(image)
    elif vision_service == 'google':
        return _get_artifact_info_google(image)
    else:
        raise ValueError(f"Unsupported vision service: {vision_service}")

def _get_artifact_info_openai(image):
    """Use OpenAI GPT-4o for vision analysis"""
    api_key = os.getenv('VISION_API_KEY')
    if not api_key:
        raise ValueError("VISION_API_KEY not found in environment variables")
    
    client = openai.OpenAI(api_key=api_key)
    
    # Convert PIL Image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """You are a museum curator and storyteller. Look at this museum artifact and:
1. Identify what it is
2. Create exactly 3 fascinating sentences about its history, significance, or interesting facts
3. Format your response with <#0.5#> tags between sentences for natural breathing pauses

Example format: "This ancient Roman coin dates back to 100 AD.<#0.5#>It features the profile of Emperor Trajan on one side.<#0.5#>Such coins were used throughout the Roman Empire for daily commerce."

Please provide exactly 3 sentences with the breathing pause tags."""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )
    
    return response.choices[0].message.content.strip()

def _get_artifact_info_google(image):
    """Use Google Gemini for vision analysis"""
    api_key = os.getenv('VISION_API_KEY')
    if not api_key:
        raise ValueError("VISION_API_KEY not found in environment variables")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = """You are a museum curator and storyteller. Look at this museum artifact and:
1. Identify what it is
2. Create exactly 3 fascinating sentences about its history, significance, or interesting facts
3. Format your response with <#0.5#> tags between sentences for natural breathing pauses

Example format: "This ancient Roman coin dates back to 100 AD.<#0.5#>It features the profile of Emperor Trajan on one side.<#0.5#>Such coins were used throughout the Roman Empire for daily commerce."

Please provide exactly 3 sentences with the breathing pause tags."""
    
    response = model.generate_content([prompt, image])
    return response.text.strip()
