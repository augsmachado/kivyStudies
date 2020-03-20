from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Tasks(BoxLayout):
    def __init__(self, tasks, **kwargs): #keywords arguments
        super().__init__(**kwargs)
        for task in tasks:
            self.add_widget(Label(text=task, font_size=30))


class Test(App):
    def build(self):
        return Tasks(['beber agua', 'fazer compras', 'dormir mais cedo', orientation='horizontal'])

Test().run()