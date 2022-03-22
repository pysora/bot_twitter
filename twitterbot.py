import tweepy

auth = tweepy.OAuthHandler("auth1",
                           "auth_secret")
auth.set_access_token("token",
                      "token_secret")

botapi = tweepy.API(auth)

try:
    botapi.verify_credentials()
    print("Auth OK")
except:
    print("Deu merda na auth mano :/")


usuario = input("Quem vc deseja responder? ")
msg = input("Oq vc deseja mandar? ")
userid = botapi.get_user(usuario)

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(f'{usuario} tweetou: {status.text}')
        try:
            for tweet in tweepy.Cursor(botapi.user_timeline, id=usuario).items(1):
                botapi.update_status(f'@{usuario} {msg}', tweet.id)

        except tweepy.TweepError as e:
            print(e.reason)



streamListener = StreamListener()
myStream = tweepy.Stream(auth=botapi.auth, listener=streamListener)
myStream.filter(follow=[userid.id_str], is_async=True)


