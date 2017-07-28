import ujson 


class MessageManager(object):

	def req_begin(self, data):
		print 'catch begin type'
		data= {
		"status": "101",
		"stype": "begin",
		"data":{
		    "cube_type": "12",
		    "direction": "2",
		    "cid": "32"

			}
		}
		return data

	def req_default(self, data):
		print 'catch default type'
		data= {
		"status": "100",
		"stype": "ok",
		"data":{
			}
		}
		return data

message_manager = MessageManager()


class MessageDispatcher(object):
	"""
	Dispatcher request message by stype
	"""

	@classmethod
	def dis(cls, data):
		req_type = data.get("req_type") or "default"
		req_type = "req_" + req_type
		resp = getattr(message_manager, req_type)(data)
		try:
			data = ujson.dumps(resp)
		except:
			print 'resp error data'
		return data