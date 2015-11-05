from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import datetime


# The custom App class
#   Widget creation code is removed
#   Another example of abstraction at work!
class CurrencyConvert(App):

    # def __init__(self):

    def build(self):
        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        # self.country_code = sorted(COUNTRY.keys())
        # self.current_location = self.country_code[2]
         return self.root

    def current_location(self, current_location):
        self.current_location = current_location
        return current_location

    def home_country(self, home_country):
        self.home_country = home_country
        return home_country

    def get_currency_conversion(self):
        try:
            value = float(self.root.ids.input_amount.text)
            return value
        except ValueError:
            return -1

    def update_details(self):
        self.root.output_leabel.text = Update_Details
        return self.root

# create and start the App running
CurrencyConvert().run()