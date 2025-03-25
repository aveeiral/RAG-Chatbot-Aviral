#sk_e9e3d22e0878ba1de8709e5e21c4714881eec62df2dc88e4

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os
from dotenv import load_dotenv  # Import load_dotenv

# Load environment variables
load_dotenv()
client = ElevenLabs(
    api_key=os.getenv("Eleven_API_KEY")  # Use getenv to fetch the API key
)

def play_audio(text_data, v_id):
    audio = client.text_to_speech.convert(
    text=text_data,
    voice_id = v_id,
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
    )
    play(audio)


#t_data = "The first move is what sets everything in motion."
#play_audio(t_data)
    
