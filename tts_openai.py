import openai
import os
import io
from pydub import AudioSegment
from pydub.playback import play

# Set OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

def text_to_speech(text):
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )

    # Save the audio file
    audio_file = "speech.mp3"
    response.stream_to_file(audio_file)

    # Load and play the audio
    audio = AudioSegment.from_file(audio_file, format="mp3")
    play(audio)

    # Remove the file after playing
    os.remove(audio_file)

# Example usage
#text_to_speech("Hello! I want o assist you please do me?")