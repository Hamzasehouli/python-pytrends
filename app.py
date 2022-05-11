from pytrends.request import TrendReq

from threading import Timer

from datetime import datetime





pytrends = TrendReq(hl='en-US', tz=360)

kwList = ["down","is down","not working","stopped","does not work"]

platfomrsList = ["facebook","instagram","whatsapp","reddit","google","discord","trello","telegram",
"twitter","shopify","tik tok","gmail","youtube","github","bing","stripe","paypal","ebay","udemy",
"cousera","edx","google maps","firebase","twitch","linkedin","netflix","disney","amazon","kik","spotify","aws","stream",
"facebook messenger","yahoo mail","battlefield","call of duty","snapchat","tinder","glovo","stack overflow","shein",
"indeed","sololearn","airbnb","zoom","clubhouse","canva","9gag","iq option","booking","expedia","binance","uber", "gcash"]

pureData =[]

run = True
def test():
 global run
 for p in kwList:
  pytrends.build_payload([p], timeframe='now 1-H')




#   results= pytrends.related_queries().values()
  filtered = []
  for r in list(pytrends.related_queries().values()):
   if(hasattr(r['rising'], 'to_dict')):
    filtered.append(r['rising'].to_dict())


  queries = []
  values = []

  for r in filtered: 
   queries = queries + list(r['query'].values())
   values = values + list(r['value'].values())



 

  for i in range(len(queries)):
   for k in platfomrsList:
    if(values[i]>10 and k in queries[i]):
     now = datetime.now()

     current_time = now.strftime("%H:%M:%S,%b/%y")
     pureData.append({'query':queries[i],'rate':values[i], 'time':current_time}) 
 if(len(pureData)!=0):    
  print(pureData)

 
 if run:
	 Timer(10, test).start()

test()