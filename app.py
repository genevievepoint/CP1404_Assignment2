from kivy.app import App
from kivy.lang import Builder


# The custom App class
#   Widget creation code is removed
#   Another example of abstraction at work!
class CurrencyConvert(App):
    def build(self):
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        return self.root


# create and start the App running
CurrencyConvert().run()