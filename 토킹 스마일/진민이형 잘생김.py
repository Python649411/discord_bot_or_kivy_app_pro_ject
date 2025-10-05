import kivy
#from kivy.uix.togglebutton import ToggleButton
#from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#from kivy.core.audio import SoundLoader
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
import pyaudio
from playsound import playsound
import wave
import os
import time
import random
class 테스트앱App(App):
    
    def a(self,instance):
            CHUNK = 1024
            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 44100
            RECORD_SECONDS = 5
            
            p = pyaudio.PyAudio()

            # 오디오 스트림 열기
            stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

            print("음성 녹음 중...")

            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            print("녹음 종료.")

        # 스트림과 PyAudio 객체 닫기
            stream.stop_stream()
            stream.close()
            p.terminate()


    def build(self):
        def b(instacne):
            list0 = ['a.png','b.png']
            e = random.choice(list0)
            image.source = e
            if image.source == 'a.png':
                 playsound('Yes.wav')
                 text.text = 'Yes!'
            else:
                 playsound('NO.wav')
                 text.text = 'No!'
        layout = BoxLayout(orientation='vertical')
        text = Label(text='Hello! :)', font_name='BMJUA_ttf.ttf', font_size=40)
        image = Image(source='a.png')
        button = Button(text='스마일과 얘기할려면 이 버튼을 누르세요!', font_name='BMJUA_ttf.ttf', font_size=40)
        
        button.bind(on_press=b)
        time.sleep(0.5)
        button.bind(on_press=self.a)
        layout.add_widget(image)
        layout.add_widget(text)
        layout.add_widget(button)

        return layout
        
if __name__ == '__main__':
    테스트앱App().run()
