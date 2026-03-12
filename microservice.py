import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent


def filter_items(items: list[dict], filters: dict[str, str]) -> list[dict]:
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


def validate_request(request_object: str) -> bool:
    """
    Validates JSON request file:
    - reads JSON
    - checks if filters are valid

    returns True for filtering
    returns False for error
    """
    try:
        data = json.loads(request_object)
    except json.JSONDecodeError:
        print("JSON request is not valid")
        return False

    filters = data.get("filters")
    if not filters:
        print("'filters' is missing")
        return False
    elif not isinstance(filters, dict):
        print("'filters' must be a dictionary")
        return False

    filter_options = ["category", "date"]

    for key in filters:
        if key not in filter_options:
            print(f"Filter not known: '{key}'")
            return False

    if "category" in filters and not isinstance(filters["category"], str):
        print("'category' must be a string")
        return False

    if "date" in filters and not isinstance(filters["date"], str):
        print("'date' must be a string")
        return False

    return True


def process_request(request_path: str, response_path: str) -> None:
    """
    Read request, validates request, and writes response.

    Args:
        request_path: file path to request.json
        response_path: file path to response.json
    """
    with open(request_path, 'r', encoding='utf-8') as request:
        request_object = request.read()

    if not request_object.strip():
        return

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
        }

    with open(response_path, 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4)


class RequestHandler(FileSystemEventHandler):
    def __init__(self, request_path: str, response_path: str) -> None:
        self.request_path = request_path
        self.response_path = response_path

    def on_modified(self, event: FileModifiedEvent) -> None:
        if event.src_path.endswith('request.json'):
            process_request(self.request_path, self.response_path)


if __name__ == "__main__":
    REQUEST_PATH = './input/request.json'
    RESPONSE_PATH = './output/response.json'
    WATCH_DIR = './input'

    event_handler = RequestHandler(REQUEST_PATH, RESPONSE_PATH)
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_DIR, recursive=False)
    observer.start()
    print("Watching request.json for changes...")

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
