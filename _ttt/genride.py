# generates template md files for rides
# rerun to add any missing weeks

from datetime import timedelta, datetime
from os import path

start_date = datetime(2023, 11, 2, 18, 0, 0)
current_date = start_date
week = timedelta(7)

def make_ride(current_date, name="???"):
    date = f'{datetime.strftime(current_date, "%Y-%m-%d")}'
    filename = f'{date}.md'
    if path.isfile(filename):
        print(filename, 'already exists')
    else:
        with open(filename, 'w') as f:
            template = f'''---
route: {name} # (where did you go / what way)
swim: ??? # (did you swim? yes/no)
venue: # (where you ended up or ate)
---'''
            f.write(template) 
        print(f'created {filename}')

if __name__ == "__main__":
    i = 1
    while current_date < datetime.now() + week:
        make_ride(current_date)
        current_date += week
        i += 1

    # add milestone rides
    milestone = i + 50 - i % 50
    make_ride(start_date +  timedelta(weeks=milestone - 1), f'{milestone}th ride')
    # multiples of 50
    # birthday
    make_ride(start_date +  timedelta(weeks=52 * (datetime.now().year - start_date.year)), "3rd Birthday")
