"""
Test for main() structure and flow (Issue #5)
Assignee: Eduardo

Uses mock to stub validate_request() and filter_items(),
so we can test main() logic independently.
"""

import json
from unittest.mock import patch

# Paths
INPUT = './input/request.json'
OUTPUT = './output/response.json'


def write_test_request(filters, items):
    """Write a test request to input/request.json"""
    request = {
        "filters": filters,
        "items": items
    }
    with open(INPUT, 'w', encoding='utf-8') as file:
        json.dump(request, file, indent=4)


def read_response():
    """Read response from output/response.json"""
    with open(OUTPUT, 'r', encoding='utf-8') as file:
        return json.load(file)


def mock_filter_items(items, filters):
    """
    Stub filter_items that actually works.
    Used for testing main() flow only.
    """
    return [
        item for item in items
        if ("category" not in filters or item["category"] == filters["category"])
        and ("date" not in filters or item["date"] == filters["date"])
    ]


def process_one_request():
    """
    Run one iteration of the main logic.
    This mimics what happens inside the while loop.
    """
    import microservice
    
    with open(INPUT, 'r', encoding='utf-8') as request:
        request_object = request.read()
    
    if not request_object.strip():
        return
    
    try:
        parsed_request = json.loads(request_object)
    except json.JSONDecodeError:
        return
    
    items = parsed_request.get("items", [])
    filters = parsed_request.get("filters", {})
    
    validation_result = microservice.validate_request(parsed_request)
    is_valid = validation_result if isinstance(validation_result, bool) else bool(validation_result)
    
    if is_valid:
        filtered_items = microservice.filter_items(items, filters)
        response = {
            "status": "success",
            "new_items": filtered_items
        }
    else:
        response = {
            "status": "failure",
            "items": items
        }
    
    with open(OUTPUT, 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4)


# Test data
test_items = [
    {
        "name": "Studying",
        "category": "Productivity",
        "date": "2026-01-10",
        "time": "14:30",
        "id": 1234
    },
    {
        "name": "Jogging",
        "category": "Health",
        "date": "2026-02-20",
        "time": "9:10",
        "id": 5678
    },
    {
        "name": "Meditation",
        "category": "Health",
        "date": "2026-01-15",
        "time": "7:00",
        "id": 9012
    }
]


print("=" * 50)
print("Test main() structure and flow (Issue #5)")
print("Using mocks for validate_request() and filter_items()")
print("=" * 50)
print()

# Patch both validate_request and filter_items
with patch('microservice.validate_request', return_value=True):
    with patch('microservice.filter_items', side_effect=mock_filter_items):
    
        # Test 1: Filter by category
        print("Test 1: Filter by category 'Health'")
        write_test_request({"category": "Health"}, test_items)
        process_one_request()
        response = read_response()
        print(f"Response status: {response['status']}")
        if response['status'] == 'success':
            print(f"Filtered items: {len(response['new_items'])} items")
            for item in response['new_items']:
                print(f"  - {item['name']} ({item['category']})")
        print(f"Expected: 2 items (Jogging, Meditation)")
        print()

        # Test 2: Filter by date
        print("Test 2: Filter by date '2026-01-10'")
        write_test_request({"date": "2026-01-10"}, test_items)
        process_one_request()
        response = read_response()
        print(f"Response status: {response['status']}")
        if response['status'] == 'success':
            print(f"Filtered items: {len(response['new_items'])} items")
            for item in response['new_items']:
                print(f"  - {item['name']} ({item['date']})")
        print(f"Expected: 1 item (Studying)")
        print()

        # Test 3: Filter by category AND date
        print("Test 3: Filter by category 'Health' AND date '2026-02-20'")
        write_test_request({"category": "Health", "date": "2026-02-20"}, test_items)
        process_one_request()
        response = read_response()
        print(f"Response status: {response['status']}")
        if response['status'] == 'success':
            print(f"Filtered items: {len(response['new_items'])} items")
            for item in response['new_items']:
                print(f"  - {item['name']} ({item['category']}, {item['date']})")
        print(f"Expected: 1 item (Jogging)")
        print()

        # Test 4: No matching items
        print("Test 4: Filter with no matches (category 'Work')")
        write_test_request({"category": "Work"}, test_items)
        process_one_request()
        response = read_response()
        print(f"Response status: {response['status']}")
        if response['status'] == 'success':
            print(f"Filtered items: {len(response['new_items'])} items")
        print(f"Expected: 0 items")
        print()

# Test 5: Invalid request (validate returns False)
print("Test 5: Invalid request (validate_request returns False)")
with patch('microservice.validate_request', return_value=False):
    with patch('microservice.filter_items', side_effect=mock_filter_items):
        write_test_request({"category": "Health"}, test_items)
        process_one_request()
        response = read_response()
        print(f"Response status: {response['status']}")
        if response['status'] == 'failure':
            print(f"Original items returned: {len(response['items'])} items")
        print(f"Expected: status 'failure', 3 original items")
        print()

print("=" * 50)
print("Tests complete!")
print("=" * 50)