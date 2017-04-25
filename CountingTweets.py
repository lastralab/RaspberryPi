from twython import TwythonStreamer

C_K = "your key"
C_S = "your secret key"
A_T = "your token"
A_S = "your secret token"

tweetcount = 0
def increment():
    global tweetcount
    tweetcount = tweetcount+1

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        text = 'text'
        for text in data:
            increment()
            print(tweetcount)
            break
        if tweetcount == 3:
            print("I have to pee a lot")
            
stream = MyStreamer(C_K, C_S, A_T, A_S)
stream.statuses.filter(track="I have to pee")
