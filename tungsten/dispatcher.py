import traceback
import random
import redis
import ujson
from grand import RandManage
from gdata import direction_conf
from gdata import percentage_conf

r = redis.Redis("127.0.0.1", 6379)
key_name = "the_game_data_key"


def gen_rand():
    rb = RandManage()

    lst = []
    for i in range(200):
        d = rb.by_weight(percentage_conf, percentage=10000)
        lst.append(d)
        r.rpush(key_name, d)


class MessageManager(object):

    def req_init(self, data):
        print 'catch init type'
        if r.exists(key_name):
            r.delete(key_name)
        gen_rand()

        data = {
            "status": "101",
            "stype": "init",
            "data": {
            }
        }
        return data

    def req_begin(self, data):

		left_cube = r.llen(key_name) or 0
		cube_type = r.lpop(key_name) or -1
		print 'lef', left_cube

		if left_cube > 0:
			cube_type = int(cube_type)
			direction_number_size = direction_conf[
			cube_type-1] if cube_type > 0 else 0
			direction_value = random.randrange(1, direction_number_size+1)
			cube_id = "000000{}{}{}".format(
			left_cube,  cube_type, direction_value)
			cube_id = "1" + "{}".format(cube_id)[-8:]
			data = {
			"status": "102",
			"stype": "begin",
			"data": {
			    "cube_type": cube_type,
			    "direction": direction_value,
			    "cid": cube_id
				}
			}
		else:
			data = {
				"status": "401",
				"stype": "cube_max_limit",
				"data": {}
			}
		return data

    def req_default(self, data):
        print 'catch default type'
        data = {
            "status": "100",
            "stype": "ok",
            "data": {
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
            print traceback.format_exc()
            data = 'error_resp'
        return data
