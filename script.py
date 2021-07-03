import requests

from bs4 import BeautifulSoup
from notifypy import Notify
import schedule
import time
import datetime
import webbrowser
from termcolor import colored

# SET THE COURSES THAT YOU WANT TO WATCH
URLS = {
    'MATH200': 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=MATH&course=200&section=921',
    'MATH221': 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=MATH&course=221&section=921'
}

INTERVAL = 1 # 1 minute interval

notification = Notify()
notification.title = "COURSE AVAILABLE"
notification.message = "..."


def check_urls():
    for (course, url) in URLS.items():
        curl = requests.get(url)
        soup = BeautifulSoup(curl.text, features="xml")
        
        contains_cnt = soup.find(text="Total Seats Remaining:").parent.next_sibling.find("strong").children
        count = int(next(contains_cnt))
        if count != 0:
            notification.message = f"{count} seats available in {course}"
            notification.send()
            webbrowser.open(url)
            print(colored(f'{datetime.datetime.now().strftime("%I:%M%p")} -- {course} has {count} seats', 'green'))
        else:
            print(colored(f'{datetime.datetime.now().strftime("%I:%M%p")} -- {course} has {count} seats', 'red'))

schedule.every(INTERVAL).minutes.do(check_urls)
schedule.run_all()
while True:
    schedule.run_pending()
    time.sleep(1)
