from requests import put
import json
import sys 
url = f"http://{input()}/users/{input()}"
data = json.dumps({x.split("=")[0]: x.split("=")[1].strip() for x in sys.stdin})
put(url, data)

