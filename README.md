# tungsten
MMORPG Server (Websocket On Tornado)


How to run it?
=============

Active your env by the follow code, and then install the requirements.

	pip install -r requirements.txt

and then clone this 

	git clone https://github.com/land-pack/tungsten.git

and then your can run the below command.

	python app.py

test it by visit your url

	ws://localhost:1191/ws

Data structure
=============

Once client connection success
    
    {

        "status":"100",
        "stype":"ok",
        "data":{

        }
    }
[REQ 1] Client send `init` request

	{

		"req_type": "init",
		"req_code": "901",
		"req_content":{

		}
	}

[REP 1] Server response client `init` request

		"status": "101",
		"stype": "init",
		"data":{
			}
		}

[REQ 2] Client can send a `begin` request

    {
        "req_type":"begin",
        "req_code":"902",
        "req_content":{

        }
    }

[REP 2] Server response client `begin` request

	#cid@ a unique code to identify a cube during the game time
	#cube_type@ is number type range 1 to 15
	#direction@ depend on cube_type


    {
        "status": "102",
        "stype": "begin",
        "data":{
            "cube_type": "12",
            "direction": "2",
            "cid": "32"

        }

    }

Exception
=========

[REQ 2] Exception response

Reach the max limit counter of cube 

	 {
		"status": "401",
		"stype": "cube_max_limit",
		"data": {}
	}

