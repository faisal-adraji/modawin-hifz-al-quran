'''
author  :   Faisal Adraji
email   :   faisal.adraji@gmail.com
version :   0.0
start   :   27-05-2017
kivy.require("1.9.0")
'''


# import threading
import kivy
kivy.require("1.9.0")

#necesary for utf
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from kivy.animation import Animation
from kivy.uix.scrollview import ScrollView
from kivy.metrics import sp, dp


# BLUE= Color(0, 0, 1, 1)
# GREEN= Color(0, 1, 0, 1)
# YELLOW= Color(1, 1, 0, 1)
# ORANGE= Color(1, .5, 0, 1)
# RED= Color(1, 0, 0, 1)


from kivy.lang import Builder

Builder.load_string('''
<Mdw>:

    StackLayout:
        id: hizb_list
        size_hint: (1.001, 1.001)
        rows: 12
        cols: 5
        padding: '20dp'
        #spacing: '10dp'
        orientation: 'rl-bt'
    # MdwButton:
    #     id: btn
    #     text: 'l'
    #     background_color: 0, 0, 0, 0
    #     size_hint: (.2, .2)
    #     on_press: root.func()


    ''')

blue = Color(0, 0, 1, 1)
green = Color(0, 1, 0, 1)
yellow = Color(1, 1, 0, 1)
orange = Color(1, .4, 0, 1)
red = Color(1, 0, 0, 1)
gray = Color(.5, .5, .5, 1)
white = Color(1, 1, 1, 1)


class MdwButton(Button):
    g_list = []    

    def __init__(self, **kwargs):
        super(MdwButton, self).__init__(**kwargs)
        self.g_list = [0,0,0,0,5, 0,0,0,0,0]
        #def on_size(self, *args):
        self.canvas.before.clear()
        for i in range(0,10):
            with self.canvas.before:
                Color(0, 0, 1, 1)
                Rectangle(pos=(self.pos[0],self.pos[1]), size=(self.size[0]*(1-float(i)/10),self.size[1]))
    
    def set_glist(self, idx, val):
        self.g_list[idx] = val

        
    def get_color(self, val):
        if val == 0:
            return Color(.5, .5, .5, 1)
        if val == 1:
            return Color(1, 0, 0, 1)
        if val == 2:
            return Color(1, .4, 0, 1)
        if val == 3:
            return Color(1, 1, 0, 1)
        if val == 4:
            return Color(0, 1, 0, 1)
        if val == 5:
            return Color(0, 0, 1, 1)

    def update(self):

        for i in range(0,10):
            self.canvas.before.children[0+i*3] = self.get_color(int(self.g_list[i]))
            self.canvas.before.children[2+i*3].pos = [self.pos[0]+5,self.pos[1]+5]
            self.canvas.before.children[2+i*3].size = [(self.size[0]-5)*(1-float(i)/10),self.size[1]-5]




class Mdw(FloatLayout):

    isfirsttime = 1

    def __init__(self, **kwargs):
        super(Mdw, self).__init__(**kwargs)

    def update(self, dt):
        # if self.isfirsttime:
        for i in range(0,60):
            self.ids.hizb_list.children[i].update()
            # self.isfirsttime = 0

        # btn = self.ids.btn
        # btn2 = self.ids.btn2

        # btn.set_glist(1,1)
        # btn2.set_glist(2,1)


        # for i in range(0,10):
        #     btn.canvas.before.children[0+i*3] = btn.grade[btn.g_list[i]]
        # for i in range(0,10):
        #     btn2.canvas.before.children[0+i*3] = btn2.grade[btn2.g_list[i]]


        #self.ids.btn.rect.pos = self.pos
        #self.ids.btn.rect.size = self.size
    
    def func(self):
        pass

        
class MdwApp(App):

    def build(self):

        Window.set_title('modawin_al_hifz')
        self.title = 'modawin_al_hifz'
        #self.icon = 'tin.png'
        self.wdg = Mdw(size= Window.size)
        main_wdg = self.wdg
        hizb_list = self.wdg.ids.hizb_list
        # btn = self.wdg.ids.btn
        # btn2 = self.wdg.ids.btn2

        # self.wdg.ids.btn.set_glist(0,2)

        #restore last session
        f = open("save.dat")
        f.readline()
        f.close()
        
    # initializing graphic objects
        
        for i in range(1,61):
            obj = MdwButton(text= str(i), size_hint= (.2, .08), background_color= (0, 0, 0, 0))
            hizb_list.add_widget(obj, len(hizb_list.children))

        Clock.schedule_interval(main_wdg.update, 1.0 / 60.0)
        return main_wdg

    def on_stop(self):
        f = open("save.dat", "w")
        f.write( str('thing') + '\n')    
        f.close()

if __name__ == '__main__':
    MdwApp().run()