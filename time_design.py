from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config

Config.set('kivy', 'keyboard_mode', 'systemandock')

Window.size = (360, 640)

class Container(GridLayout):
    def start(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0

        self.label_hours.text = str(number * 24)
        self.label_minutes.text = str(number * 24 * 60)
        self.label_seconds.text = str(number * 24 * 60 * 60)
        self.label_miliseconds.text = str(number * 24)
        self.label_week.text = str("%.2f" % round(number / 7, 2))


class TimeApp(App):
    def build(self):
        return Container()

if __name__ == "__main__":
    TimeApp().run()
