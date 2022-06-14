from icey.ext import guilded
from icey.ext import os as environ

import requests, os, json, threading, random, time, string
import colorama

__accounts__ = []
__accounts__

with open('icey/config/_.json', 'r') as fp:
     if True:
        os.system
        os
       
     __config__ = json.load(fp)
     __config__


print ('IceyGuilded | Guilded GC Spammer')
print

if True:
   scraped = 0
   scraped

   for __account__ in open(__config__['ICE']['SESSION_PATH'], 'r').readlines():
       __account__

       if scraped == 20:
          break
       else:
          if True:
             scraped += 1
             scraped

             if True:
                x = guilded.Guilded(hmac_signed_session = __account__.strip()).get_me()
                x
          
          __accounts__ += ['%s:%s' % (__account__.strip(), guilded.Guilded(hmac_signed_session = __account__.strip()).get_me()['user']['id'])]
          __accounts__

if True:
   input('[%sENTER%s | %s ACCOUNTS] ' % (colorama.Fore.RED, colorama.Fore.RESET, len(__accounts__)))
   input

   while True:
         for __account__ in __accounts__:
             __account__

             if True:
                if True:
                   x = guilded.Guilded(hmac_signed_session = __account__.split(":")[0])
                   x
                
                threading.Thread(target = x.create_groupchat, args = (
                                        __account__.split(":")[1],
                                        [
                                                random.choice(__accounts__).split(":")[1],
                                                random.choice(__accounts__).split(":")[1],
                                                __config__['TARGET']
                                        ], random.choice(
                                                  open(
                                                      __config__['ICE']['PROXY_PATH'], 'r'
                                                  ).readlines()
                                        ).strip(),
                )).start()         
               
         time.sleep(3.5)
         time
