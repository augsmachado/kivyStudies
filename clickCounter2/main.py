from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Incrementer(BoxLayout):
    pass

class Test(App):
    def build(self):
       return Incrementer()

Test().run()