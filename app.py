from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from currency import get_all_details
import datetime
# from trip import details


# The custom App class
#   Widget creation code is removed
#   Another example of abstraction at work!
class CurrencyConvert(App):

    def __init__(self, **kwargs):
        super(CurrencyConvert, self).__init__(**kwargs)
        self.details =

    def build(self,):
        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.find_trip_details()
        self.root.ids.current_date.text = 'Today is: \n' + str(datetime.date.today()).replace('-', '/')
        return self.root

    def add_date(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def find_trip_details(self):
        file = open('config.txt', encoding='utf-8')
        self.home_country = file.readline().strip()
        self.root.ids.home_country.text = str(self.home_country)
        self.country_list = []
        for line in file:
            parts = line.strip().split(',')
            self.details.add(parts[0], parts[1], parts[2])
            self.root.ids.country_selection.values = self.country_list
            # self.root.ids.country_selection.values = parts[0]
            self.country_list.append(parts[0])
        file.close()

    def current_location(self, current_location):
        self.current_location = current_location
        return current_location

    def get_currency_conversion(self):
        place_dictionary = get_all_details
        home_currency = place_dictionary
        spinner_location = self.root.ids.country_selection.text
        # print(spinner_location)
        location_currency = place_dictionary(spinner_location)[1]
        # print(location_currency)
        # print(home_currency)
        # value = convert(float(self.root.ids.input_amount.text)), home_currency, location_currency
        # self.root.ids.input_amount = str(value)
        try:
            value = float(self.root.ids.input_amount.text)
            return value
        except ValueError:
            return -1

    # def update_details(self):
    #     self.root.output_leabel.text = tkinter.Button(self.frame, text='Update Details', command=self.root.output_label.text_click)
    #     return self.root

# create and start the App running
CurrencyConvert().run()



# OH MY LORD!!!