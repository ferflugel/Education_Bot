import csv
import pandas

# input should be ~insert event_name MMDDYY
def insert_event(event, deadline):
  with open(r'data.csv', 'a', newline='') as csvfile:
    fieldnames = ['Event','Deadline']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'Event':f'{event}', 'Deadline':f'{deadline}'})


def print_calendar():
  df = pandas.read_csv('data.csv')
  return df
