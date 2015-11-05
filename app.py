from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import datetime
# import config.txt

# The custom App class
#   Widget creation code is removed
#   Another example of abstraction at work!
class CurrencyConvert(App):

    open('config.txt', encoding='utf-8')
    in_file = open('config.txt', 'r')
    in_file.readline()
    # reader = txt.reader(in_file)
    # for row in reader:
    #     print(row)

    # def __init__(self, trip_country, home_country, start_date, end_date ):
    #     super().__init__(trip_country, home_country, start_date, end_date)
    #     self.trip_details = config.txt

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
        self.root.output_leabel.text = tkinter.Button(self.frame, text='Update Details', command=self.root.output_label.text_click)
        return self.root

# create and start the App running
CurrencyConvert().run()