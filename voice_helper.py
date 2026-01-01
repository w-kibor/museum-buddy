import pyttsx3
import io

def generate_elevenlabs_voice(text):
    """
    Generate speech using pyttsx3 (works with espeak or Windows TTS)
    Returns audio bytes in WAV format
    """
    engine = pyttsx3.init()
    
    # Optional: Configure voice properties
    engine.setProperty('rate', 150)    # Speed of speech (default is 200)
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    
    # Optional: Set voice (uncomment to use specific voice)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)  # 0=male, 1=female typically
    
    # Save to bytes
    audio_buffer = io.BytesIO()
    engine.save_to_file(text, 'temp_audio.wav')
    engine.runAndWait()
    
    # Read the file into bytes
    with open('temp_audio.wav', 'rb') as f:
        audio_bytes = f.read()
    
    # Clean up temp file
    import os
    os.remove('temp_audio.wav')
    
    return audio_bytes