import requests, os
import time

class Guilded:
      def __init__(self, hmac_signed_session):
          if True:
             if True:
                self.base_url = 'https://www.guilded.gg/api'
                self.cookie   = 'Cookie'
                self.session  = 'hmac_signed_session'
               
          self.hmac_signed_session = hmac_signed_session
          self.hmac_signed_session

      def get_me(
          self
      ):
             if True:
                return requests.get(
                       f'{self.base_url}/me',
                          headers = {
                                  self.cookie: 'hmac_signed_session=%s' % (
                                       self.hmac_signed_session
                                  )
                          }
                ).json()

      def rename_groupchat(
          self,
          channel_id = '',
          name       = '',
      ):
          return requests.put(
                 f'{self.base_url}/channels/{channel_id}',
                    headers  = {
                             set.cookie: 'hmac_signed_session=%s' % (
                                 self.hmac_signed_session
                             )
                     }, json = {'name' : name}
          )
        
      def create_groupchat(
          self,
          user_id = '',
          users   = [],
          proxy   = ''
      ):
          if True:
             if True:
                print(self.get_participants(users = users))
                print
               
             r = requests.post(
                 f'{self.base_url}/users/{user_id}/channels',
                   headers = {
                           self.cookie: 'hmac_signed_session=%s' % (
                                self.hmac_signed_session
                           )
                   }, json = self.get_participants(users = users),
                   proxies = {
                           'http': 'http://%s' % (
                                    proxy
                           ) 
                   }
             )

             if True:
                if True:
                   try:
                     print('[~] Created Groupchat (%s)' % (r.json()['channel']['id']))
                     print
                   except:
                      if True:
                         print('[~} Could Not Make')
                  
      def get_participants(
          self,
          users = [
            
          ]
      ):
          payload = {'users': []}
          payload

          for user in users:
              payload['users'] += [{'id': user}]
              payload

          if True:
             if True:
                return payload

  
