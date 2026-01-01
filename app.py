import streamlit as st
import os
from PIL import Image
import io
from vision_helper import get_artifact_info
# NEW CODE
from voice_helper import generate_elevenlabs_voice
from dotenv import load_dotenv

load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Museum AI Narrator",
    page_icon="🏛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
    }
    .upload-container {
        border: 2px dashed #ccc;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
    .result-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🏛️ Museum AI Narrator")
    st.markdown("Upload a photo of a museum artifact and let AI bring it to life with a fascinating story!")
    st.markdown('</div>', unsafe_allow_html=True)
    
   # Check for API keys
    eleven_key = os.getenv('ELEVENLABS_API_KEY')
    vision_key = os.getenv('VISION_API_KEY')

    if not eleven_key or not vision_key:
        st.error("⚠️ Missing API keys! Please update your .env file.")
        st.info("Ensure you have added ELEVENLABS_API_KEY and VISION_API_KEY to your .env file.")
        return
    
    # File uploader
    st.markdown('<div class="upload-container">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "📸 Upload Museum Artifact Photo",
        type=['jpg', 'jpeg', 'png', 'webp'],
        help="Upload a clear photo of a museum artifact"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(image, caption="Uploaded Artifact", use_column_width=True)
        
        with col2:
            st.info("🔍 Analyzing artifact...")
        
        # Process the image
        try:
            # Get artifact information
            with st.spinner("🧠 Identifying artifact and generating story..."):
                artifact_story = get_artifact_info(image)
            
            # Display the story
            st.markdown('<div class="result-container">', unsafe_allow_html=True)
            st.subheader("📖 Artifact Story")
            st.write(artifact_story)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Generate audio
            with st.spinner("🎙️ Creating audio narration..."):
                audio_data = generate_elevenlabs_voice(artifact_story)
            
            # Display audio player
            st.subheader("🔊 Audio Narration")
            st.audio(audio_data, format='audio/mp3')
            
            # Download button for audio
            st.download_button(
                label="📥 Download Audio",
                data=audio_data,
                file_name="museum_artifact_narration.mp3",
                mime="audio/mp3"
            )
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("Please check your API keys and try again.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Made with ❤️ using Streamlit • Vision by OpenAI/Google • Voice by MiniMax</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
