from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class Tasks(BoxLayout):
    def __init__(self, tasks, **kwargs): #keywords arguments
        super().__init__(**kwargs)
        for task in tasks:
            self.ids.box.add_widget(Label(text=task, font_size=30, size_hint_y=None, height=200))


class Test(App):
    def build(self):
        return Tasks(['beber agua', 'fazer compras', 'dormir mais cedo', 'iuuuuuuu', 'uhuuuuu', 'estamos no caminho certo'])

Test().run()