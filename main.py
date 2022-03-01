import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.widget import Label
from kivy.uix.screenmanager import ScreenManager, Screen


class MyApp(App):
    def build(self):
        return Label(text='Test')


if __name__ == '__main__':
    KivyApp().run()