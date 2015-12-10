import tweepy

consumer_key = "7ximBALttdr4lhrlQdSDtXQqU";
#eg: consumer_key = "7ximBALttdr4lhrlQdSDtXQqU";


consumer_secret = "KKUewrDypYSGYzpQANGaw31ZdnraSFCKEbbmwFY1PyjqtTYVn8";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "2279847266-J4kub98YgQnbyklH9FAPQCIehnYQDfZdO5RJEws";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "PVJo20imbhOJEibm5T2CQhD2hL9eUr5aCO3k2uNfuAHvN";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



