# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Andrew
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory:
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def is_phrase_in(self, text):
        parsed = text.lower()
        for p in string.punctuation:
            parsed = ''.join([i if i != p else ' ' for i in parsed])
        for ch in text.lower():
            if ch in string.punctuation:
                parsed.replace(ch, ' ')

        parsed = [s.strip() for s in parsed.split()]
        phrase_list = self.phrase.split()

        if len(phrase_list) > len(parsed):
            return False
        return any([parsed[i:i+len(phrase_list)] == phrase_list for i in range(len(parsed)-len(phrase_list)+1)])

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, news):
        return super().is_phrase_in(news.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        super().__init__(phrase)

    def evaluate(self, news):
        return super().is_phrase_in(news.get_description())

# TIME TRIGGERS

# Problem 5
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    def __init__(self, time):
        d, b, Y, t = time.split()
        H, M, S = t.split(':')
        self.time = datetime.strptime("{} {} {} {}:{}:{}".format(d, b, Y, H, M, S), "%d %b %Y %H:%M:%S").replace(tzinfo=None)

# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        super().__init__(time)

    def evaluate(self, news):
        return self.time > news.get_pubdate().replace(tzinfo=None)

class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        super().__init__(time)

    def evaluate(self, news):
        return self.time < news.get_pubdate().replace(tzinfo=None)

# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, T):
        self.T = T
    
    def evaluate(self, news):
        return not self.T.evaluate(news)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, news):
        return self.T1.evaluate(news) and self.T2.evaluate(news)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2

    def evaluate(self, news):
        return self.T1.evaluate(news) or self.T2.evaluate(news)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered = []
    for s in stories:
        for T in triggerlist:
            if T.evaluate(s):
                filtered.append(s)
                break
    return filtered



#======================
# User-Specified Triggers
#======================
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!
    t_classes = {'DESCRIPTION': DescriptionTrigger, 'TITLE': TitleTrigger, 'BEFORE': BeforeTrigger, 'AFTER': AfterTrigger, 'AND': AndTrigger, 'OR': OrTrigger, 'NOT': NotTrigger}
    t_list = []
    t_dict = {}
    for line in lines:
        args = line.split(',')
        print(args)
        if args[0].startswith('t'):
            if args[1] in ['OR', 'AND']:
                t_dict[args[0]] = t_classes[args[1]](t_dict[args[2]], t_dict[args[3]])
            else:
                t_dict[args[0]] = t_classes[args[1]](args[2])
        elif args[0].startswith('ADD'):
            for k in args[1:]:
                t_list.append(t_dict[k])
    return t_list



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        # t = "Google & Yahoo Top News"
        t = "Google Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

