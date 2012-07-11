from google.appengine.ext import db

#
# Datastore model classes
#

class LeaderBoard(db.Model):
	INSTANCE = "current"
	
	timestamp = db.DateTimeProperty(auto_now=True)
	all_scores = db.ListProperty(int, default=[], indexed=False)

	@classmethod
	def load(cls):
		return LeaderBoard.get_by_key_name(LeaderBoard.INSTANCE)