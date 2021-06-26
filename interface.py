import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (1000,700)

class Chat(App):
    def build(self):
        self.icon = 'Assets/chat-logo.ico'
        return ConnectPage()

class ConnectPage(Widget):
    pass
 
class Home(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.img = Image(source='Assets/background.jpg',
            size_hint=(1000, 700),
        )
        self.add_widget(self.img)

if __name__ == "__main__":
    Chat().run()
