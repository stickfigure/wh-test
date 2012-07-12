
from datetime import datetime
from google.appengine.api import backends
from webapp2_extras import json
import webapp2
import random
import urllib2

import model


# turn datetime 12:52 into 52.94356237562356, where 52 is minutes and everything after . is random
def make_random():
	minute = datetime.now().minute
	return minute + random.random()
			
#
#
class Post(webapp2.RequestHandler):
	def get(self):
		url = backends.get_url("leaders") + "/backend/submit?value=" + str(make_random())
		result = urllib2.urlopen(url)
		self.response.write(result.read())


#
#
class Results(webapp2.RequestHandler):
	def get(self):
		leaderboard = model.LeaderBoard.load()
		
		self.response.content_type = "application/json"
		self.response.write(json.encode(leaderboard.all_scores))
		

#
#
class Noop(webapp2.RequestHandler):
	def get(self):
		self.response.write("noop")

