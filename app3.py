import kivy
from kivy.uix.togglebutton import ToggleButton
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
import random

class 게임뽑기App(App):
  def a(self, instance):
    a = random.choice(self.fps)
    text.text = a
  def build(self):
  layout = BoxLayout(orientation="vertical")
  self.fps = ["발로란트","배틀그라운드","카운트 스트라이트2","오버워치2","에이펙스 레전드","콜 오브 듀티"]
  self.tps = [""]

  text = Label(text="오늘 게임 뭐하지?", font_name='', font_size=80)
  button = Button(text="FPS게임 뽑기", font_name="", font_size=80)
  button2 = Button(text="TPS게임 뽑기", font_name="", font_size=80)

  button.bind(self.a)
  # button2.bind()

  layout.add_widget(text)
  layout.add_widget(button)
  layout.add_widget(button2)

if __name__ == '__main__':
  게임뽑기App().run()
