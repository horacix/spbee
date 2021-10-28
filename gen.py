from os import write
from os.path import exists
import json
import requests
from google.cloud import texttospeech

dictionary = {}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# GCP Text to Speech
client = texttospeech.TextToSpeechClient()
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

with open('input.txt') as f:
    lines = f.readlines()

with open('data.json') as f:
    data = json.load(f)


def google2file(text, path):
    synth_input = texttospeech.SynthesisInput(text=text)
    res = client.synthesize_speech(
        input=synth_input, voice=voice, audio_config=audio_config)
    with open(path, 'wb') as f:
        f.write(res.audio_content)


for line in lines:
    word = line.rstrip()
    print(word)
    file = f"{word}.mp3"
    path = f"out/{file}"
    sppath = f"out/sp-{file}"
    if not exists(path):
        if word in data:
            r = requests.get(data[word], headers=headers)
            if r.status_code == 200 and r.encoding is None:
                print('* dict')
                with open(path, 'wb') as f:
                    f.write(r.content)
            else:
                print('* google')
                google2file(word, path)
        else:
            print('* google')
            google2file(word, path)
    if not exists(sppath):
        print('* spelling')
        google2file(f"{','.join(list(word))}. {word}", sppath)

with open(f'out/words.csv', 'w') as f:
    for line in lines:
        word = line.rstrip()
        f.write(f"{word},[sound:{word}.mp3],[sound:sp-{word}.mp3]\n")
