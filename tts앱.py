import kivy
#from kivy.uix.togglebutton import ToggleButton
#from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput
#import pyttsx3
from gtts import gTTS
from playsound import playsound
import os
#import time

class tts앱App(App):
   

    def build(self):
          
        #script = value
        #tts = gtts.gTTS(text=script, lang='ko')
        #tts.save("voiceKo.mp3")
        #ps.playsound("voiceKo.mp3")
        def on_ener(instance):
          tts = gTTS(text=instance.text, lang='ko')
          file = str("tts" + str() + ".mp3")
          tts.save(file)
          # time.sleep(10)
          
          playsound(file, True)
          os.remove(file)
          #print(f"디버깅: 이벤트 발생 위젯:{instance.text}")
          #print(f"변경된 텍스트 값:{value}")
        layout = BoxLayout(orientation='vertical')
        
        text_box0 = TextInput(font_name='BMJUA_ttf.ttf', font_size=80, multiline=False)
 
        text_box0.bind(on_text_validate=on_ener)
        
        layout.add_widget(text_box0)
        #def on_text(instance, value):
            #print('텍스트 변겅:', value)
        

       
        return layout
    
    
if __name__ == '__main__':
    tts앱App().run()