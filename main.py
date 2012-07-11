#!/usr/bin/env python
#

import webapp2
import handler
import backend

app = webapp2.WSGIApplication([
							('/post', handler.Post),
							('/results', handler.Results),
							('/_ah/start', backend.Start),
							('/backend/submit', backend.Submit),
							('/backend/compute', backend.Compute)
							])
