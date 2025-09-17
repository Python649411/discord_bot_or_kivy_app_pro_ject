
import kivy
from kivy.uix.togglebutton import ToggleButton
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
import random
#음식들 인덱스

    
class 점메추App(App):
    def ko1(self, instance):
           self.ran = random.choice(self.ko)
           self.menu_label.text = self.ran
           if self.sound_swoosh:
                self.sound_swoosh.play()
    #def jp1(self, instance):
           #self.ran1 = random.choice(self.jp)
           #self.menu_label.text = self.ran1
           #if self.sound_swoosh:
                #self.sound_swoosh.play()
    #def cn1(self, instance):
             #self.ran2 = random.choice(self.cn)
             #self.menu_label.text = self.ran2
             #if self.sound_swoosh:
                #self.sound_swoosh.play()
    #def bc1(self, instance):
             #self.ran3 = random.choice(self.bc)
             #self.menu_label.text = self.ran3
             #if self.sound_swoosh:
                #self.sound_swoosh.play()
    #def en1(self, instance):
             #self.ran4 = random.choice(self.en)
             #self.menu_label.text = self.ran4
             #if self.sound_swoosh:
                #self.sound_swoosh.play()
    #def all1(self, instance):
             #self.ran5 = random.choice(self.all)
             #self.menu_label.text = self.ran5
             #if self.sound_swoosh:
                #self.sound_swoosh.play()

    def build(self):
        self.sound_swoosh = SoundLoader.load('swoosh.mp3')
        
        layout = BoxLayout(orientation="vertical")
        

        self.ko = ["오늘은 여친이 생기실거에요","오늘은 부자가 되실거예요","아무거나","오늘은 날씨가 안좋아서 비를 맞을거에요"]
        #self.jp = ['초밥','회덮밥','참치회','연어회','우동','라멘','돈까스','가츠동','오야코동','규동','텐동','카레라이스','타코야끼','오코노미야끼']
        #self.cn = ['짜장면','볶음짬뽕','간짜장','쟁반짜장','울면','기스면','짬뽕','탕수육','마파두부덮밥','양장피','팔보채','깐풍기','유산슬','고추잡채밥','동파육','라조기','유린기','양장피','팔보채','고추잡채','크림새우','칠리새우','마라탕','마라샹궈','훠궈','꿔바로우','즈란심관(양고기 볶음)','군만두','물만두']
        #self.bc = ['떡볶이', '순대', '튀김', '김밥', '어묵', '라볶이', '쫄면', '라면', '잔치국수', '충무김밥', '유부초밥', '볶음밥', '김치볶음밥', '튀김만두', '삶은 계란', '핫도그', '컵밥', '꼬마김밥', '떡꼬치', '소떡소떡', '닭꼬치', '콜팝']
        #self.en = ['햄버거', '스테이크', '핫도그', '피자', '치킨', '바비큐 립', '베이글', '샌드위치', '팬케이크', '와플', '프렌치 토스트', '오믈렛', '베이컨 & 에그', '프렌치프라이', '어니언링', '콜슬로', '머핀', '스모어', '클램 차우더', '검보', '타코', '엔칠라다', '잠발라야', '미트볼', '맥앤치즈']
        #self.all =['김치찌개','된장찌개','순두부찌개','부대찌개','갈비탕','설렁탕','순대국밥','콩나물국밥','뼈해장국','미역국','감자탕','비빔밥','김치볶음밥','돌솥비빔밥','제육덮밥','오징어덮밥','뚝배기제육','잔치국수','김치말이국수','칼국수','쌀국수','평양냉면','물냉면','비빔냉면','삼겹살','돼지갈비','소불고기','제육볶음','닭볶음탕','족발','장충동보쌈','떡볶이','어묵','찜닭','아구찜','간장게장','보리밥','쭈구미볶음','초밥','회덮밥','참치회','연어회','우동','라멘','돈까스','가츠동','오야코동','규동','텐동','카레라이스','타코야끼','오코노미야끼','짜장면','볶음짬뽕','간짜장','쟁반짜장','울면','기스면','짬뽕','탕수육','마파두부덮밥','양장피','팔보채','깐풍기','유산슬','고추잡채밥','동파육','라조기','유린기','양장피','팔보채','고추잡채','크림새우','칠리새우','마라탕','마라샹궈','훠궈','꿔바로우','즈란심관(양고기 볶음)','군만두','물만두','떡볶이', '순대', '튀김', '김밥', '어묵', '라볶이', '쫄면', '라면', '잔치국수', '충무김밥', '유부초밥', '볶음밥', '김치볶음밥', '튀김만두', '삶은 계란', '핫도그', '컵밥', '꼬마김밥', '떡꼬치', '소떡소떡', '닭꼬치', '콜팝','햄버거', '스테이크', '핫도그', '피자', '치킨', '바비큐 립', '베이글', '샌드위치', '팬케이크', '와플', '프렌치 토스트', '오믈렛', '베이컨 & 에그', '프렌치프라이', '어니언링', '콜슬로', '머핀', '스모어', '클램 차우더', '검보', '타코', '엔칠라다', '잠발라야', '미트볼', '맥앤치즈']
        self.menu_label = Label(text='오늘의 운세 뽑기! 오늘도 힘차게 아자아자!', font_name='BMJUA_ttf.ttf', font_size=30)
        button = Button(text='지금 운세뽑기기',font_name='BMJUA_ttf.ttf',size_hint_y=None, height=100 , font_size=50)
        #button1 = Button(text='한식 점메추하기', font_name='BMJUA_ttf.ttf', size_hint_y=None, height=50, font_size=40)
        #button2 = Button(text='일식 점메추하기', font_name='BMJUA_ttf.ttf', size_hint_y=None, height=50, font_size=40)
        #button3 = Button(text='중식 점메추하기', font_name='BMJUA_ttf.ttf', size_hint_y=None, height=50, font_size=40)
        #button4 = Button(text='미식 점메추하기', font_name='BMJUA_ttf.ttf', size_hint_y=None, height=50, font_size=40)
        #button5 = Button(text='분식 점메추하기', font_name='BMJUA_ttf.ttf', size_hint_y=None, height=50, font_size=40)
        button.bind(on_press=self.ko1)
        #button1.bind(on_press=self.ko1)
        #button2.bind(on_press=self.jp1)
        #button3.bind(on_press=self.cn1)
        #button4.bind(on_press=self.en1)
        #button5.bind(on_press=self.bc1)
        
        layout.add_widget(self.menu_label)
        layout.add_widget(button)
        #layout.add_widget(button1)
        #layout.add_widget(button2)
        #layout.add_widget(button3)
        #layout.add_widget(button4)
        #layout.add_widget(button5)
        return layout
    
        

if __name__ == '__main__':
    점메추App().run()
