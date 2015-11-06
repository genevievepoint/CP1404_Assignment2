__author__ = 'jc260183'

# this is the exception class
class Error:
    def __init__(self, value):
        super().__init__(value)


class Country:
    def __init__(self, name="", currency_code="", currency_symbol=""):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def currency_string(self, amount):
        # formats the currency to two decimal places
        amount = '{:.2f}'.format(amount)
        return str(amount)

    def __str__(self):
        return self.name + ' ' + self.currency_code + ' ' + self.currency_symbol + ' '


class Details:
    def __init__ (self, country_name, start_date, end_date):
        self.country_name = country_name
        self.start_date = start_date
        self.end_date = end_date
        self.locations = []

    def add(self, country_name, start_date, end_date):
        # adds a start date and end date makes sure that the date is in the correct format
        self.locations.append((country_name, start_date, end_date))
        start_date = start_date.strip().split('/')
        if not len(start_date[0]) == 4 or len(start_date[1]) == 2 or len(start_date[2]) == 2:
            raise Error('Date does not follow format. YYYY/MM/DD')

        end_date = end_date.strip().split('/')
        if not len(end_date[0]) == 4 or len(end_date[1]) == 2 or len(end_date[2]) == 2:
            raise Error('Date does not follow format. YYYY/MM/DD')
        if start_date < end_date:
            self.locations.append((country_name, start_date, end_date))
        else:
            raise Error('End date is before start date')

    def current_country(self, date_string):
        for location in self.locations:
            if location[1] <= date_string <= location[2]:
                return location[0]
            else:
                return Error('Date not found')

    # doesn't work properly
    def is_empty(self, is_empty):
        # creates a true of false error
        if self.locations is '':
            return True
        else:
            return False


# testing to see if stuff works
def main():
    australia = Country('Australia', 'AUD', '$')
    print(australia.currency_string(100.236))
    print(australia)

    # details = Details()
    # print(details.is_empty())

if __name__ == "__main__":
    # execute only if run as a script
    main()