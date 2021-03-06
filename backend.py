
from google.appengine.api import background_thread, logservice 
from threading import Lock
import webapp2
import time
import model
import logging

logger = logging.getLogger(__name__)

# singleton in-memory structure, holds array of ints
leaderboard = []
leaderboard_lock = Lock()

def add_to_leaderboard(value):
	global leaderboard
	global leaderboard_lock
	
	with leaderboard_lock:
		leaderboard.append(value)

def compute_leaderboard():
	logger.debug("Computing leaderboard")
	
	global leaderboard
	global leaderboard_lock
	
	with leaderboard_lock:
		old = leaderboard
		leaderboard = []
	
	lead = model.LeaderBoard(key_name=model.LeaderBoard.INSTANCE, all_scores=old)
	lead.put()
	
def timer_loop():
	while True:
		now = time.time()
		then = now - (now % 180) + 180
		seconds = then - now
		logger.debug("Next calculation in " + str(seconds) + " seconds")
		logservice.flush()
		time.sleep(seconds)
		
		compute_leaderboard()

#
#
class Start(webapp2.RequestHandler):
	def get(self):
		background_thread.start_new_background_thread(timer_loop, [])
		
#
#
class Submit(webapp2.RequestHandler):
	def get(self):
		strvalue = self.request.get('value')
		
		# You wanted an int in the LeaderBoard but the input value looks like a float.  Just gonna chop it.  
		intvalue = int(strvalue.split('.')[1])
		
		add_to_leaderboard(intvalue)
		self.response.write("done")

#	
# This is just to force cycling by hand on dev instance.  Not relevant to production.
#
class Compute(webapp2.RequestHandler):
	def get(self):
		compute_leaderboard()
		self.response.write("done")
		
#
#
class Noop(webapp2.RequestHandler):
	def get(self):
		self.response.write("noop")

