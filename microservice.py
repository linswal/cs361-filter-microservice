# filter list of items from request_object and return correct list of items
# items (array) of item (dict)
# filters (dict)
def filter_items(items, filters):
    return [
        item for item in items
        if ("category" not in filters or
            items["category"] == filters["category"])
        and ("date" not in filters or items["date" == filters["date"]])
    ]


# Feel free to change this function to only return True or False and make another
# function to write the response object if you'd like!
def validate_request(request_object):
    return {}   # or return booleans


if __name__ == "__main__":
    while True:
        with open('./input/request.json', 'r', encoding='utf-8') as request:
            request_object = request.read()

        # ...
