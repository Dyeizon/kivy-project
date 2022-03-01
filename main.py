from kivy.app import App
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

login_screen = Builder.load_file('login_screen_kv.kv')


class KivyApp(App):
    def build(self):
        return login_screen


if __name__ == '__main__':
    KivyApp().run()