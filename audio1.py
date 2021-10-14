from gtts import gTTS
from playsound import playsound
audio="name.mp3"
language='en'
lang_check=True
s=gTTS("my name is  balaji",slow=True)
s.save(audio)
playsound(audio)
