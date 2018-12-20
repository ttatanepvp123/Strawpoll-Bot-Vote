import requests
import _thread
import time

print(
"""
   _____ _                                  _ _ 
  / ____| |                                | | |
 | (___ | |_ _ __ __ ___      ___ __   ___ | | |
  \___ \| __| '__/ _` \ \ /\ / / '_ \ / _ \| | |
  ____) | |_| | | (_| |\ V  V /| |_) | (_) | | |
 |_____/ \__|_|  \__,_| \_/\_/ | .__/ \___/|_|_|
                               | |BOT VOTE V0.1.0
                               |_|      
    By Ttatanepvp123
"""
)
global id_strawpoll, amount, id_votes, i, finish
finish = False
i = 0
amount = int(input("amount vote : "))
id_votes = input("id vote option : ").split(",")
number_thread = int(input("thread : "))

def woker():
    global id_strawpoll, amount, id_votes, i, finish
    while amount > i:
        for id_vote in id_votes:
            success = False
            while success != True:
                try:
                    r = requests.post('https://www.strawpoll.me/1', data={
                        "data-form-type": "poll-vote",
                        "data-poll-id": "0",
                        "data-no-prevent-dupe": "",
                        "data-created-epoch": "1537219479",
                        "novalidate": "novalidate",
                        "options": id_vote
                    })
                    if r.status_code == 200:
                        success = True
                except:
                    pass
        i += 1
    finish = True

def vote_per_second():
    global i, vps
    before = 0
    vps = 0
    while amount > i:
        vps = i - before
        before = i
        time.sleep(1)

def displayer():
    global id_strawpoll, amount, id_votes, i, finish, vps
    print("Targets : {}".format(id_votes))
    before_str = ""
    while amount > i:
        current_str = "Votes : {}/{} | V/s : {}".format(i,amount,vps)
        print(current_str+" "*(len(current_str)-len(before_str)),end="\r")
        before_str = current_str

_thread.start_new_thread(vote_per_second,())
_thread.start_new_thread(displayer,())
for index in range(number_thread):
    _thread.start_new_thread(woker,())

while not finish:
    pass