from replit import db

def create_deadline(event, deadline):
  db[f"{event}"] = deadline

def print_calendar():
  assignments = "Assignments and Dates\n" 
  keys = db.keys()
  for k in keys:
    assignments += f"\n{k} due {db[k]}"
  return assignments

def delete_deadline(event):
  del db[f"{event}"]
