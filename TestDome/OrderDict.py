import json
def sort_by_price_ascending(json_string):
    parsed = json.loads(json_string)
    return sorted(parsed, key= lambda item: (item['price'], item['name']))


print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))