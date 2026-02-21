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
            items["category"] == filters["category"])
        and ("date" not in filters or items["date" == filters["date"]])
    ]


# Return True if request is valid, False otherwise
def validate_request(request_object):
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

        # Parse JSON
        try:
            parsed_request = json.loads(request_object)
        except json.JSONDecodeError:
            time.sleep(0.1)
            continue

        # Get items and filters from request
        items = parsed_request.get("items", [])
        filters = parsed_request.get("filters", {})

        # Validate request
        validation_result = validate_request(parsed_request)

        if validation_result:
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
