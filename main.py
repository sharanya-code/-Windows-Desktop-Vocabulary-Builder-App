
import sys

import bs4
import requests
import lxml

import datetime

from win10toast import ToastNotifier

toaster = ToastNotifier()

while (True):
    try:
        date = datetime.date.today()
        main_req = requests.get("https://randomword.com")
        soup_object = bs4.BeautifulSoup(main_req.text, "lxml")
        word = soup_object.select('#random_word')[0].getText()
        word_defination = soup_object.select('#random_word_definition')[0].getText()
        message = "The Word is: "+ word + '\n'+ "The word definition is: " + word_defination + '\n'+"The date is: " + str(date)+ '\n'
        toaster.show_toast(message,
                           icon_path='words-icon-5.jpg',
                           duration=86400)
        sys.exit()

    except:
        toaster.show_toast("Oops! No Internet Connection! Retrying Now!",
                           icon_path='words-icon-5.jpg',
                           duration=30)



