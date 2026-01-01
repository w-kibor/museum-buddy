# 🏛️ Museum AI Narrator

A Streamlit web application that identifies museum artifacts from photos and generates fascinating audio narrations using AI.

## Features

- 📸 **Image Upload**: Upload photos of museum artifacts
- 🧠 **AI Vision**: Uses GPT-4o or Gemini-1.5-Pro to identify artifacts
- 📖 **Story Generation**: Creates 3-sentence fascinating stories with natural pauses
- 🎙️ **Voice Narration**: Converts stories to audio using MiniMax Speech-02-Turbo
- 🔊 **Audio Player**: Built-in audio player with download option

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
MINIMAX_API_KEY=your_minimax_api_key_here
VISION_API_KEY=your_vision_api_key_here
VISION_SERVICE=openai  # or "google"
```

### 3. Get API Keys

- **MiniMax API Key**: Get from [MiniMax Console](https://api.minimax.io/)
- **Vision API Key**: 
  - For OpenAI: Get from [OpenAI Platform](https://platform.openai.com/)
  - For Google: Get from [Google AI Studio](https://aistudio.google.com/)

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Launch the app
2. Upload a photo of a museum artifact
3. Wait for AI to identify and analyze the artifact
4. Listen to the fascinating audio narration
5. Download the audio file if desired

## Project Structure

```
museum-buddy/
├── app.py              # Main Streamlit application
├── vision_helper.py    # Vision API integration
├── voice_helper.py     # MiniMax TTS integration
├── requirements.txt     # Python dependencies
├── .env.example       # Environment variables template
└── README.md          # This file
```

## Technical Details

- **Frontend**: Streamlit with custom CSS styling
- **Vision**: OpenAI GPT-4o or Google Gemini-1.5-Pro
- **Voice**: MiniMax Speech-02-Turbo with happy emotion
- **Audio Format**: MP3 with streaming support
- **Pause Tags**: `<#0.5#>` tags for natural breathing pauses

## Troubleshooting

- **API Key Errors**: Ensure your `.env` file is properly configured
- **Image Upload Issues**: Supported formats: JPG, JPEG, PNG, WebP
- **Audio Generation**: Check MiniMax API quota and connectivity
- **Vision Analysis**: Verify your vision API key is valid and has credits

## Enjoy!

Transform your museum visits into interactive storytelling experiences! 🎭
