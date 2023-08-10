from gtts import gTTS
import os

def text_to_audio(text,language='en',output_file='output.mp3'):
    #creatett a gtts object
    
    tts = gTTS(text=text,lang=language,slow=False)
    tts.save(output_file)
    os.system('start' + output_file)
    
#calling the fxn
if __name__=="__main__":
    input_text ="hello migwi"
    text_to_audio(input_text,language='en',output_file='output.mp3')