from kivy.app import App
import webbrowser as wb
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Container(BoxLayout):
    label_text = ObjectProperty()
    text_input = ObjectProperty()

    def change_something(self):
        self.label_text.text = wb.open('https://music.youtube.com/search?q=' + self.text_input.text)


class MusicKivyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MusicKivyApp().run()
