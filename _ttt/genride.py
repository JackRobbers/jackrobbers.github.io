# generates template md files for rides
# rerun to add any missing weeks
# easy since always on a thursday

from datetime import timedelta, datetime
from os import path

template = '''---
route: ???
swim: ???
---
'''

current_date = datetime(2023, 11, 2)
week = timedelta(7)

if __name__ == "__main__":
    i = 1
    while current_date < datetime.now():
        filename = f'{datetime.strftime(current_date, "%Y-%m-%d")}.md'
        if path.isfile(filename):
            print(filename, i, 'already exists')
        else:
            with open(filename, 'w') as f:
                f.write(template) 
            print(f'created {filename} ride number {i}')
        current_date 
venue:= week
        i 
venue:= 1
