#!/usr/bin/env python
#

import webapp2
import handler
import backend

app = webapp2.WSGIApplication([
							('/post', handler.Post),
							('/results', handler.Results),
							('/noop', handler.Noop),
							('/bnoop', handler.BackendNoop),
							('/away', handler.Away),
							('/_ah/start', backend.Start),
							('/backend/submit', backend.Submit),
							('/backend/compute', backend.Compute),
							('/backend/noop', backend.Noop)
							])
