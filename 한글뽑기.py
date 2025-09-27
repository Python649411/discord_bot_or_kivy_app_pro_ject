import kivy
from kivy.uix.togglebutton import ToggleButton
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
#from kivy.uix.image import Image
import random

kivy.require('2.3.1')

class 한글자음모음뽑기App(App):
    def a(self, instance):
        self.a2 = random.choice(self.a1)
        self.text0.text = self.a2
    def b(self, instance):
        self.b3 = random.choice(self.b2)
        self.text0.text = self.b3

    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.text0 = Label(text='한글 자&모음을 뽑아보세요!',font_name='BMJUA_ttf.ttf', font_size=30)
        button = Button(text='자음뽑기',font_name='BMJUA_ttf.ttf',size_hint_y=None, height=100 , font_size=50)
        button1 = Button(text='모음뽑기',font_name='BMJUA_ttf.ttf',size_hint_y=None, height=100 , font_size=50)

        self.a1 = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
        self.b2 = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ']

        button.bind(on_press=self.a)
        button1.bind(on_press=self.b)

        layout.add_widget(self.text0)
        layout.add_widget(button)
        layout.add_widget(button1)

        return layout
    
if __name__ == '__main__':
    한글자음모음뽑기App().run()
