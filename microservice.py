import json


# filter list of items from request_object and return correct list of items
# items (array) of item (dict)
# filters (dict)
def filter_items(items, filters):
    return [
        item for item in items
        if ("category" not in filters or
            items.get["category"] == filters["category"])
        and ("date" not in filters or item.get("date") == filters["date"])
    ]


# Feel free to change this function to only return True or False and make another
# function to write the response object if you'd like!
def validate_request(request_object):
    """
    Validates JSON request file:
    - reads JSON
    - checks if filters are valid

    returns True for filtering
    returns False for error
    """
    errors = []

    # load JSON
    try:
        data = json.loads(request_object)
    except json.JSONDecodeError:
        return False, ["JSON request is not valid"]

    # check if filter exists and is a dictionary
    filters = data.get("filters", {})
    if not isinstance(filters, dict):
        return False, ["'filters' must be a dictionary"]

    # filter options
    filter_options = ["category", "date"]

    for key in filters:
        if key not in filter_options:
            errors.append(f"Filter not known: '{key}'")

    # check filters are strings
    if "category" in filters and not isinstance(filters["category"], str):
        errors.append("'category' must be a string")

    if "date" in filters and not isinstance(filters["date"], str):
        errors.append("'date' must be a string")

    # check for errors
    if errors:
        return False, errors

    return True, filters


    # return {}   # or return booleans


if __name__ == "__main__":
    while True:
        with open('./input/request.json', 'r', encoding='utf-8') as request:
            request_object = request.read()

        # ...
