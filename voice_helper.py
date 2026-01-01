import os
import requests
from dotenv import load_dotenv
import io

load_dotenv()

def generate_minimax_voice(text):
    """
    Generate audio from text using MiniMax Speech-02-Turbo API.
    
    Args:
        text (str): Text to convert to speech (should include <#0.5#> pause tags)
        
    Returns:
        bytes: Audio data in MP3 format
    """
    api_key = os.getenv('MINIMAX_API_KEY')
    if not api_key:
        raise ValueError("MINIMAX_API_KEY not found in environment variables")
    
    url = "https://api.minimax.io/v1/text_to_speech"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "speech-02-turbo",
        "text": text,
        "emotion": "happy",
        "format": "mp3"
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, stream=True)
        response.raise_for_status()
        
        # Read the audio data from the streaming response
        audio_data = io.BytesIO()
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                audio_data.write(chunk)
        
        audio_data.seek(0)
        return audio_data.getvalue()
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error calling MiniMax API: {str(e)}")
    except Exception as e:
        raise Exception(f"Error processing audio: {str(e)}")
