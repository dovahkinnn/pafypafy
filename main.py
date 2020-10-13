import kivy
from kivy.app import App

from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
import pafy
Builder.load_file('main.kv')


class MyGrid(Widget):
    name = ObjectProperty(None)
    

    def btn(self):
        print("'", self.name.text,"'",)
        a=(self.name.text)
        url = str(a)
        video = pafy.new(url)
        bestaudio = video.getbestaudio()
        bestaudio.download()
        print(video)
        
       
        
    
   


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue" 
        return MyGrid()


if __name__ == "__main__":
    MainApp().run()