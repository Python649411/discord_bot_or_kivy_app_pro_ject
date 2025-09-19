
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
#음식들 인덱스

    
class 운세뽑기App(App):
    def ko1(self, instance):
           self.ran = random.choice(self.ko)
           self.menu_label.text = self.ran
           if self.sound_swoosh:
                self.sound_swoosh.play()
   

    def build(self):
        self.sound_swoosh = SoundLoader.load('swoosh.mp3')
        image1 = Image(source='ima.png')
        layout = BoxLayout(orientation="vertical")
        

        self.ko = ["오늘은 여친이 생기실거에요","오늘은 부자가 되실거예요","오늘은 날씨가 안좋아서 비를 맞을거에요","오늘은 포경수술을 할거예요"]
       
        self.menu_label = Label(text='오늘의 운세 뽑기! 오늘도 힘차게 아자아자!', font_name='BMJUA_ttf.ttf', font_size=30)
        button = Button(text='지금 운세뽑기',font_name='BMJUA_ttf.ttf',size_hint_y=None, height=100 , font_size=50)
        
        button.bind(on_press=self.ko1)
       
        
        layout.add_widget(self.menu_label)
        layout.add_widget(image1)
        layout.add_widget(button)
        
        return layout
    
        

if __name__ == '__main__':
    운세뽑기App().run()
