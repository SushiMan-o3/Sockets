import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


Window.size = (1000, 700)


class Chat(App):
    def build(self):
        self.icon = 'Assets/chat-logo.ico'
        return ConnectPage()


class ConnectPage(Screen):
    pass


class Home(Screen):
    pass


if __name__ == "__main__":
    Chat().run()
