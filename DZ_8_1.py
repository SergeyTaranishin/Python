import time
class Date:
   @classmethod
   def print(cls, valid_date):
      dd = int(time.strftime('%d', valid_date))
      mm = int(time.strftime('%m', valid_date))
      yyyy = int(time.strftime('%Y', valid_date))
      print(f'день {dd} месяц {mm} год {yyyy}')

   @staticmethod
   def validation(date_str):
      try:
         valid_date = time.strptime(date_str, '%d-%m-%Y')
         Date.print(valid_date)
      except ValueError:
         print('Формат даты указан некорректно!')


date_str = input('Введите дату в формате ДД-ММ-ГГГГ: ')
Date.validation(date_str)
