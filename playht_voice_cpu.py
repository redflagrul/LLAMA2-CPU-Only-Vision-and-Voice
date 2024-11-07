import requests
import sounddevice as sd
from scipy.io.wavfile import write
import json
import numpy as np

PLAYHT_API_KEY = "MwdYeBi6lfXYPa8dcgcuhYNGduz2"  # Replace with your API key
VOICE_ID = "Sabby Wabby"  # Your cloned voice model

def get_voice_response(text):
    url = "https://play.ht/api/v1/convert"
    headers = {
        "Authorization": PLAYHT_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "voice": VOICE_ID,
        "content": text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        audio_url = response.json().get("audio_url")
        if audio_url:
            audio_data = requests.get(audio_url).content
            with open("response.wav", "wb") as f:
                f.write(audio_data)
            fs, data = wavfile.read("response.wav")
            sd.play(data, fs)
            sd.wait()
        else:
            print("Error: No audio URL received.")
    else:
        print("Error:", response.json())
