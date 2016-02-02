import json
import requests


# This script is used to update the emote mapping we use to get the emote id 
# so we can then send a request if the emote is not stored locally. 
# Since the format of the json from the api call is the like the follow
# {
#     meta : {...},
#     images : {
#         id : {
#             code : emote_name,
#             ...
#         }
#         ...
#     }
    
# }
# Since we only need the id to make the class we convert it to the following
# {
#     code : id,
#     code2 : id,
# }


url = "http://twitchemotes.com/api_cache/v2/images.json"

res = requests.get(url)
id_map = res.json()
emote_map = {}
i = 0
for id in list(id_map["images"].keys()):
    code = id_map["images"][id]["code"]
    emote_map[code] = id
    
with open("src/config/emote2id.json","w") as f:
    json.dump(emote_map,f)
    
    
res.close()    