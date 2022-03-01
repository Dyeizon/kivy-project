import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# from kivy.lang.builder import Builder

import random

kivy.require('2.0.0')


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))


class TravelApp(App):
    def build(self):
        return MyRoot()


if __name__ == '__main__':
    TravelApp().run()
