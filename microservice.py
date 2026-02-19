# BELOW IS JUST A TEMPLATE FOR NOW. NOTHING IS FINAL YET.

# Note:
#   The "item" objects properties are based on your own main program's
#   implementation. As long as the item have at least one property to be
#   filtered by ("category" and/or "date").

# Example of request JSON object (To be written in request.json by the
#   main program for filter.py to read)
# {
#   “option”: “category”,
#   “category”: “Health”,
#   “items”: [
#       {“item”: “Studying”, “id”: 1234, “category”: “Productivity”}, 
#       {“item”: “Exercising”, “id”: 5678, “category”:  “Health”}
#       ]
# }


# Example of response JSON object (To be written in response.json by the 
#   filter.py for main program to read)
# {
#   {
#     “status”: “success”,
#     “items”: [
#       {“item”: “Exercising”, “id”: 5678, “category”: “Health”}
#       ]
# }

# import os


# filter list of items from request_object and return correct list of items
def filter_items(requeset_object):
    return []


# Return True if request is valid, otherwise return false
def validate_request(request_object):
    """
    empty docstring
    """
    return True


if __name__ == "__main__":        
    while True:
        with open('./input/request.json', 'r', encoding='utf-8') as request:
            request_object = request.read()

        if not validate_request(request_object):
            # ...
            print("error message")

        # new_items = filter_items(request_object)

        # write new_items to as a JSON object to request.json