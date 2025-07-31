import os
from gtts import gTTS
from dotenv import load_dotenv
from playsound import playsound  # ✅ Direct audio playback

load_dotenv()

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    try:
        playsound(output_filepath)
    except Exception as e:
        print(f"An error occurred while playing audio: {e}")

# input_text = "Hi, How are you boss"
# output_filepath = "test_txt_to_speech.mp3"
# text_to_speech_with_gtts(input_text, output_filepath)
