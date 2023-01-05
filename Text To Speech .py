import gtts
import playsound


text = input("Enter Something :\n")
sound = gtts.gTTS(text, lang='en')
sound.save("welcome.mp3")
playsound.playsound("Welcome.mp3")