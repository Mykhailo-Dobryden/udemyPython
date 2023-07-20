import json

json_str = '{"id":235, "brand": "Nike", "qty":84, "status":{"isForSale":true}}'
json_array = '[{"a":1}, {"b":2}]'

sneakers = json.loads(json_str)
print(sneakers)

json_from_dict = json.dumps(sneakers, indent=4)
print(json_from_dict)
