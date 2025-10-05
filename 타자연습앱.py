import kivy
from kivy.uix.togglebutton import ToggleButton
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
#from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
import random

class 타자연습App(App):
    def build(self):
        self.a = ['가는말이 고아야 오는말이 곱다','바늘 도둑이 소 도둑 된다','소 잃고 외양간 고친다.','식은 죽 먹기','누워서 떡 먹기','다람쥐 헌 쳇바퀴에 타고파.']
        def on_ener(instance):
            if instance.text == text.text:
                text.text = random.choice(self.a)
                text_box0.text = ''
        layout = BoxLayout(orientation='vertical')
        text = Label(text='다람쥐 헌 쳇바퀴에 타고파.',font_name='BMJUA_ttf.ttf', font_size=70)
        text_box0 = TextInput(font_name='BMJUA_ttf.ttf', font_size=50, multiline=False)
        text_box0.bind(on_text_validate=on_ener)

        layout.add_widget(text)
        layout.add_widget(text_box0)
        return layout

if __name__ == '__main__':
    타자연습App().run()