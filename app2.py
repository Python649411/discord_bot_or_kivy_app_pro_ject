import kivy
#from kivy.uix.togglebutton import ToggleButton
#from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random

class 김정은똥뽑기App(App):
    def ko(self, instance):
        self.ran = random.choice(self.list)
        self.text.text = self.ran


    def build(self):

        layout = BoxLayout(orientation="vertical")
        self.list = ['평범한 김정은 똥\n등급:★\n특징:냄새가 드럽다',"슈퍼아이돌 김정은 똥\n등급:★★\n특징:증류수를 뽑는다 물냄새가 난다",'유태영 똥\n등급:★★★★★\n특징:똥에서 진민이형이 나와서 태영이형을 팬다.']
        self.text = Label(text='오늘 점심을 뭐 먹을지 고민된다면? 점메추 버튼 한번으로 점심먹기!', font_name='BMJUA_ttf.ttf', font_size=30)
        button = Button(text='똥 뽑기',font_name='BMJUA_ttf.ttf',size_hint_y=None, height=100 , font_size=50)

        button.bind(on_press=self.ko)

        layout.add_widget(self.text)
        layout.add_widget(button)
        return layout
    
if __name__ == '__main__':
    김정은똥뽑기App().run()
