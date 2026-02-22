import json
import time


def filter_items(items, filters):
    """
    Filter items by filters' properties

    Parameters:
        items (list): A list of item (dict)
        filters (dict): Contain "category" and/or "date" properties

    Returns:
        list: Contain item(s) that matched the filters properties' values
    """
    return [
        item for item in items
        if ("category" not in filters or
            item["category"] == filters["category"])
        and ("date" not in filters or item["date"] == filters["date"])
    ]


def validate_request(request_object):
    """
    Validates JSON request file:
    - reads JSON
    - checks if filters are valid

    returns True for filtering
    returns False for error
    """
    # load JSON
    try:
        data = json.loads(request_object)
    except json.JSONDecodeError:
        print("JSON request is not valid")
        return False

    # check if filter exists and is a dictionary
    filters = data.get("filters")
    if not filters:
        print("'filters' is missing")
        return False
    elif not isinstance(filters, dict):
        print("'filters' must be a dictionary")
        return False

    # filter options
    filter_options = ["category", "date"]

    for key in filters:
        if key not in filter_options:
            print(f"Filter not known: '{key}'")
            return False

    # check filters are strings
    if "category" in filters and not isinstance(filters["category"], str):
        print("'category' must be a string")
        return False

    if "date" in filters and not isinstance(filters["date"], str):
        print("'date' must be a string")
        return False

    return True


if __name__ == "__main__":
    while True:
        with open('./input/request.json', 'r', encoding='utf-8') as request:
            request_object = request.read()

        # main() structure and flow
        # Assignee: Eduardo
        # Issue: #5

        # Skip if empty
        if not request_object.strip():
            time.sleep(0.1)
            continue

        # Validate request
        validation_result = validate_request(request_object)

        if validation_result:
            # Get items and filters from request
            parsed_request = json.loads(request_object)
            items = parsed_request.get("items", [])
            filters = parsed_request.get("filters", {})

            # Valid: filter items and write success response
            filtered_items = filter_items(items, filters)
            response = {
                "status": "success",
                "new_items": filtered_items
            }
        else:
            # Invalid: write failure response with original items
            response = {
                "status": "failure",
                "items": items
            }

        # Write response
        with open('./output/response.json', 'w', encoding='utf-8') as file:
            json.dump(response, file, indent=4)

        time.sleep(0.1)
