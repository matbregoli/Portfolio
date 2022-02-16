import datetime

class DateManager:

	def get_day(self, date_string):
		date = datetime.datetime(int(date_string[:4]), int(date_string[4:6]), int(date_string[6:]))
		return date.strftime("%A")

	def get_date(self, date_string):
		date = datetime.datetime(int(date_string[:4]), int(date_string[4:6]), int(date_string[6:]))
		return f'{date.strftime("%Y")} {date.strftime("%m")} {date.strftime("%d")}' 

	def dates_to_string(self, dates_dic):
		return str(dates_dic['date'])

class Date:
	def __init__(self, date, day):
		self.day = day
		self.date = date
		self.weather = ''
		self.temp = {}

	def get_day(self):
		return self.day

	def get_date(self):
		return self.date
 
date_manager = DateManager()

