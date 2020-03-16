from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ClickCounter(App):
    def build(self):
        # empilha widgets como caixas
        box = BoxLayout(orientation="vertical")
        
        button = Button(text='Button 1', font_size=30, on_release=self.increment)
        self.label = Label(text='1', font_size=30)
        
        box.add_widget(button)
        box.add_widget(self.label)
    	
        return box

    def increment(self, button):
        self.label.text = str(int(self.label.text)+1) 

ClickCounter().run()