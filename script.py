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
    'STAT': 'https://courses.students.ubc.ca/cs/courseschedule?sesscd=S&pname=subjarea&tname=subj-section&course=305&sessyr=2021&section=001&dept=STAT',
}

INTERVAL = 1 # 1 minute interval


notification = Notify()
notification.title = "COURSE AVAILABLE"
notification.message = "..."

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def check_urls():
    for (course, url) in URLS.items():
        curl = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(curl.text, features="lxml")
        
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