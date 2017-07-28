import redis
import ujson 
from grand import RandManage

r = redis.Redis("127.0.0.1", 6379)
key_name = "the_game_data_key"


def gen_rand():
	rb = RandManage()
	a = [0, 0.03, 0.055, 0.06, 0.05, 0.045, 0.11, 0.11, 0.1, 0.1,0.1,0.09,0.05,0.06, 0.02,0.02]
	lst = []
	for i in range(200):
		d = rb.by_weight(a, percentage=10000)
		lst.append(d)
		r.rpush(key_name, d)




class MessageManager(object):

	def req_init(self, data):
		print 'catch init type'
		if r.exists(key_name):
			r.delete(key_name)
		gen_rand()

		data= {
		"status": "101",
		"stype": "init",
		"data":{
			}
		}
		return data


	def req_begin(self, data):

		print 'catch begin type'
		data= {
		"status": "102",
		"stype": "begin",
		"data":{
		    "cube_type": r.lpop(key_name),
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