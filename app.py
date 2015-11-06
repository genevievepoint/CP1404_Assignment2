import datetime
import time

from kivy.app import App
from kivy.lang import Builder

from kivy.core.window import Window

from currency import get_all_details
from currency import convert
from trip import Details


# The custom App class
class CurrencyConvert(App):
    def __init__(self, **kwargs):
        super(CurrencyConvert, self).__init__(**kwargs)
        self.details = Details()

# Creates the window and provides the basic information used in the start up of the program
    def build(self, ):
        Window.size = (350, 700)
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file('gui.kv')
        self.find_trip_details()
        # Sets the current date in the layout
        self.root.ids.current_date.text = 'Today is: \n' + str(datetime.date.today()).replace('-', '/')
        # sets the current location of the user in their trip
        self.root.ids.trip_location.text = ('Current Location: \n' + self.details.current_country(str(datetime.date.today()).replace('-', '/')))
        return self.root

    def find_trip_details(self):
        # calls the Details class from the trip module
        self.details = Details()
        # opens the config file that contains the users trip details
        file = open('config.txt', encoding='utf-8')
        self.home_country = file.readline().strip()
        self.root.ids.home_country.text = str(self.home_country)
        # displays the users trip order in a chronological list
        self.country_list = []
        for line in file:
            parts = line.strip().split(',')
            print(parts)
            self.details.add(parts[0], parts[1], parts[2])
            self.root.ids.country_selection.values = self.country_list
            self.country_list.append(parts[0])
        file.close()
        return self.country_list


    def get_currency_conversion(self, directions):
        # print(directions)
        # creates a dictionary from the currency module
        place_dictionary = get_all_details()
        # stores the user selection from the spinner gui
        spinner_location = self.root.ids.country_selection.text
        # print(spinner_location)
        location_currency = place_dictionary[spinner_location][1]
        home_currency = place_dictionary[self.home_country][1]
        # print(location_currency)
        # print(home_currency)
        # provides the status message and conversion amount in the gui
        # allows for back and forth conversion
        if directions == 'to home':
            value = convert(float(self.root.ids.target_amount.text), home_currency, location_currency)
            self.root.ids.home_amount.text = str(value)
            self.root.ids.status.text = location_currency + ' to ' + home_currency
        else:
            value = convert(float(self.root.ids.home_amount.text), location_currency, home_currency)
            self.root.ids.target_amount.text = str(value)
            self.root.ids.status.text = home_currency + ' to ' + location_currency

    # updates the conversion rate for the user
    def update_currency(self):
        self.root.update_currency.text = 'updated' + time.strftime('%X')


# create and start the app
CurrencyConvert().run()



# OH MY LORD!!!
