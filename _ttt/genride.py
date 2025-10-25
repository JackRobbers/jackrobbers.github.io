# generates template md files for rides
# rerun to add any missing weeks

from datetime import timedelta, datetime
from os import path

template = '''---
route: ??? # (where did you go / what way)
swim: ??? # (did you swim? yes/no)
venue: # (where you ended up or ate)
---

<!-- content goes here, can be images or words. uses markdown -->
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
        current_date += week
        i += 1
