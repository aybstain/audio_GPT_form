
import speech_recognition as sr
from pydub import AudioSegment

def speech_recognition():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source, timeout=3)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Speech recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    print("Finished recording.")
