# generates template md files for rides
# rerun to add any missing weeks

from datetime import timedelta, datetime
from os import path

current_date = datetime(2023, 11, 2)
week = timedelta(7)

if __name__ == "__main__":
    i = 1
    while current_date < datetime.now():
        date = f'{datetime.strftime(current_date, "%Y-%m-%d")}'
        filename = f'{date}.md'

        if path.isfile(filename):
            print(filename, i, 'already exists')
        else:
            with open(filename, 'w') as f:
                template = f'''---
                    route: ??? # (where did you go / what way)
                    swim: ??? # (did you swim? yes/no)
                    venue: # (where you ended up or ate)
                    ---

                    <!-- content goes here, uses markdown -->

                    <!-- images will automatically be shown, if put in images/ttt/. must match the date of the ride, in format YYYY-MM-DD. can be jpg or png -->

                    ![](../images/ttt/{date}.png)
                    ![](../images/ttt/{date}.jpg)
                '''
                f.write(template) 
            print(f'created {filename} ride number {i}')
        current_date += week
        i += 1
