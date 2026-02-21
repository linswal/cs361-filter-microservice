import json
import time

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
        is_valid = validation_result if isinstance(validation_result, bool) else bool(validation_result)
        
        if is_valid:
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