import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to Text to Audio generator created by Kavya")
    while True:
         x = input("Enter what you want me to pronounce: ")
         if x == 'q':
             break
         text_to_speech(x)
