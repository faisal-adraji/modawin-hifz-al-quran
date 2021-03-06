'''
author  :   Faisal Adraji
email   :   faisal.adraji@gmail.com
version :   1.0
kivy.require("1.9.0")
kivy.used("1.10.0")
'''
#for using kivy
import kivy
kivy.require("1.9.0")

#necesary for utf
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#graphics anwidgets and others kivy modules
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.metrics import sp, dp
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


#build app with kv language
Builder.load_string('''
<Mdw>:

#main menu, list of ahzab

    Button:
        id:quit
        on_press: root.show_guide()

    StackLayout:
        id: hizb_list
        size_hint: (1.001, 1.001)
        rows: 12
        cols: 5
        padding: '20dp'
        orientation: 'lr-bt'

    Label:
        id: lbl
        markup: True
        size_hint: (.2, .05)
        pos_hint: {'x':.4, 'y':.94}
        font_size: '20dp'
        font_name: 'arial.ttf'

    Label:
        id: lbl2
        size_hint: (.2, .05)
        pos_hint: {'x':.15, 'y':.935}
        font_size: '20dp'

#sub list, when selecting a hizb in main menu

    StackLayout:
        id: kb
        size_hint: (.75, .75)
        pos_hint: {'x':.125, 'y':.02}
        rows: 5
        cols: 2
        padding: '20dp'
        spacing: '10dp'
        orientation: 'lr-bt'


#legend, opened when you touch background

    FloatLayout:
        id: lgd
        color: 1, 1, 1, 1
        size_hint: (1., 1.)
        pos_hint: {'x': .0, 'y': .0}
        orientation: 'vertical'
        on_touch_down: root.hide_guide()

        canvas:
            Color:
                rgba: .5, .5, .5, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Button:
            size: lgd.size
            pos: lgd.pos
            background_color: .0, .0, .0, .0
            on_press: root.hide_guide()
        Image:
            size: lgd.size
            pos: lgd.pos
            source: 'legend.png'
            allow_stretch: True

    ''')

blue = Color(0, 0, 1, 1)
green = Color(0, 1, 0, 1)
yellow = Color(1, 1, 0, 1)
orange = Color(1, .4, 0, 1)
red = Color(1, 0, 0, 1)
gray = Color(.5, .5, .5, 1)
white = Color(1, 1, 1, 1)

#globals variable used for dialog between classes of the app
glb = 1
glb2 = 1

'''
abreviation of modawin button this class is a
button with ten partq that can take a different
colors, so it can sumarise the colors of it sub-menu buttons
'''
class MdwButton(Button):
    g_list = []    

    def __init__(self, **kwargs):
        super(MdwButton, self).__init__(**kwargs)
        self.g_list = [0,0,0,0,0, 0,0,0,0,0]
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

    '''
    this function tell the number of the button 
    pressed in hizb list through glb variable
    '''
    def set_mnu(self,instance):
        global glb
        glb = int(self.text)

    def update(self):
        for i in range(0,10):
            #reversed
            #self.canvas.before.children[0+i*3] = self.get_color(int(self.g_list[9-i]))
            self.canvas.before.children[0+i*3] = self.get_color(int(self.g_list[i]))
            self.canvas.before.children[2+i*3].pos = [self.pos[0]+5,self.pos[1]+5]
            self.canvas.before.children[2+i*3].size = [(self.size[0]-5)*(1-float(i)/10),self.size[1]-5]


'''
abreviation of modawin sub-button, this class is a
button that upgrade color in each press from gray to blue
'''
class MdwSubButton(Button):
    #color values take a look at get_color function
    col_val = 0

    def __init__(self, **kwargs):
        super(MdwSubButton, self).__init__(**kwargs)

        self.canvas.before.clear()

        with self.canvas.before:
            Color(0, 0, 1, 1)
            Rectangle(pos=(self.pos[0],self.pos[1]), size=(self.size[0],self.size[1]))

    def set_glist(self, val):
        self.col_val = val

    def get_color(self, val):
        if val == 0:
            #gray
            return Color(.5, .5, .5, 1)
        if val == 1:
            #red
            return Color(1, 0, 0, 1)
        if val == 2:
            #orange
            return Color(1, .4, 0, 1)
        if val == 3:
            #yellow
            return Color(1, 1, 0, 1)
        if val == 4:
            #green
            return Color(0, 1, 0, 1)
        if val == 5:
            #blue
            return Color(0, 0, 1, 1)

    '''
    this function tell the number of pressed
    button through glb2 variable
    '''
    def set_mnu2(self,instance):
        global glb2
        glb2 = int(self.text)

    def update(self):
        self.canvas.before.children[0] = self.get_color(int(self.col_val))
        self.canvas.before.children[2].pos = [self.pos[0]+5,self.pos[1]+5]
        self.canvas.before.children[2].size = [self.size[0]-5,self.size[1]-5]


class Mdw(FloatLayout):

    isfirsttime = 1
    ismain_menu = 1
    islgd = 1

    def __init__(self, **kwargs):
        super(Mdw, self).__init__(**kwargs)

    def update(self, dt):
        if self.isfirsttime:
            self.show_main(self)
            self.hide_main(self)
            self.show_main(self)
            self.hide_guide()
            #print(kivy.__version__)
            self.isfirsttime = 0

        if self.ismain_menu:
            for i in range(0,60):
                self.ids.hizb_list.children[i].update()
        else:
            for i in range(0,12):
                self.ids.kb.children[i].update()
        
    def show_main(self, wdg):
        if not wdg.ismain_menu:
            wdg.ids.kb.opacity = 0
            wdg.ids.kb.size_hint_x = 0
            wdg.ids.hizb_list.size_hint_x = 1
            wdg.ids.hizb_list.opacity = 1
            wdg.ismain_menu = 1
            wdg.ids.lbl.text = u'\ufe8f\ufe8d\ufeaf\ufea3\ufef7\ufe8d'
            wdg.ids.lbl2.text = ''
     
    def hide_main(self, wdg):
        if wdg.ismain_menu:
            wdg.ids.hizb_list.opacity = 0
            wdg.ids.hizb_list.size_hint_x = 0
            wdg.ids.kb.size_hint_x = .75
            wdg.ids.kb.opacity = 1
            wdg.ismain_menu = 0
            for i in range(1,11):
                wdg.ids.kb.children[i-1].text = str(i+1+((int(glb)-1)*10))
                wdg.ids.kb.children[i-1].col_val = wdg.ids.hizb_list.children[glb-1].g_list[i-1]
            wdg.ids.lbl.text = u'\ufe8f\ufeaf\ufea4\ufedf\ufe8d\u0020\ufe95\ufe8e\ufea4\ufed4\ufebb'
            wdg.ids.lbl2.text = str(glb)

    #this function increment the color index of the button pressed
    def col_upg(self, wdg):
        wdg.ids.hizb_list.children[glb-1].g_list[(glb2-2)%10] += 1
        # wdg.ids.hizb_list.children[glb-1].g_list[(glb2-2)%10] %= 6
        if wdg.ids.hizb_list.children[glb-1].g_list[(glb2-2)%10] > 5:
            wdg.ids.hizb_list.children[glb-1].g_list[(glb2-2)%10] = 5
        wdg.ids.kb.children[(glb2-2)%10].col_val = wdg.ids.hizb_list.children[glb-1].g_list[(glb2-2)%10]

    #set color to 0 (gray)
    def reset(self, wdg):
        for i in range(1,11):
            wdg.ids.hizb_list.children[glb-1].g_list[i-1] = 0
            wdg.ids.kb.children[i-1].col_val = 0

    def show_guide(self):
        if not self.islgd:
            self.ids.lgd.size_hint_x = 1
            self.ids.lgd.size_hint_y = 1
            self.ids.lgd.opacity = 1
            self.islgd = 1

    def hide_guide(self):
        if self.islgd:
            self.ids.lgd.opacity = 0
            self.ids.lgd.size_hint_x = 0
            self.ids.lgd.size_hint_y = 0
            self.islgd = 0


class MdwApp(App):

    def build(self):
        Window.set_title('modawin_al_hifz')
        self.title = 'modawin_al_hifz'
        #self.icon = 'tin.png'
        self.wdg = Mdw(size= Window.size)
        main_wdg = self.wdg
        hizb_list = self.wdg.ids.hizb_list
        kb = self.wdg.ids.kb
        lgd = self.wdg.ids.lgd

        
        def show_main(instance):
           self.wdg.show_main(self.wdg)

        def hide_main(instance):
           self.wdg.hide_main(self.wdg)

        def col_upg(instance):
           self.wdg.col_upg(self.wdg)
        def reset(instance):
           self.wdg.reset(self.wdg)


        
    # initializing graphic objects
    
        for i in range(1,61):
            obj = MdwButton(id='btn'+str(i), text= str(i), size_hint= (.2, .08), background_color= (0, 0, 0, 0) )
            hizb_list.add_widget(obj, len(hizb_list.children))
            obj.bind(on_press= hide_main)
            obj.bind(on_press= obj.set_mnu)

        for i in range(1,11):
            obj = MdwSubButton(text= str(i), size_hint= (.5, .2), background_color= (0, 0, 0, 0) )
            kb.add_widget(obj, len(kb.children))
            obj.bind(on_press= col_upg)
            obj.bind(on_press= obj.set_mnu2)

        obj = MdwSubButton(text= "<--", size_hint= (.8, .13), background_color= (0, 0, 0, 1) )
        kb.add_widget(obj, len(kb.children))
        obj.bind(on_press= show_main)

        obj = MdwSubButton(text= "O\nX", padding= ('90dp','90dp'), size_hint= (.2, .13), background_color= (0, 0, 0, 1) )
        kb.add_widget(obj, len(kb.children))
        obj.bind(on_press= reset)


        #restore last session auto-save if exist
        try:
            f = open("save.dat")
        except :
            # save file don't exist
            for i in range(0,60):
                for j in range(0,10):
                    self.wdg.ids.hizb_list.children[i].g_list[j] = 0
        else:
            # save file exists
            for i in range(0,60):
                for j in range(0,10):
                    self.wdg.ids.hizb_list.children[i].g_list[j] = int(f.readline())
            f.close()
        
        #fps of the app
        Clock.schedule_interval(main_wdg.update, 1.0 / 30.0)
        return main_wdg



    def on_stop(self):
        f = open("save.dat", "w")
        for i in range(0,60):
            for j in range(0,10):
                f.write( str(self.wdg.ids.hizb_list.children[i].g_list[j]) + "\n")    
        f.close()

if __name__ == '__main__':
    MdwApp().run()