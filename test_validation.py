import json
from microservice import validate_request


def tests():

    # Test 1: Valid request
    print("Test 1: Valid request")
    test_1 = json.dumps({
        "filters": {"category": "Productivity"},
        "items": []
    })
    print(validate_request(test_1))

    # Test 2: Invalid JSON request
    print("Test 2: Invalid JSON request")
    test_2 = "{filters: Productivity}"
    print(validate_request(test_2))

    # Test 3: Invalid filter type
    print("Test 3: Filter type not in dictionay")
    test_3 = json.dumps({
        "filters": "Productivity"
    })
    print(validate_request(test_3))

    # Test 4: Filter key unknown
    print("Test 4: Filter key unknown")
    test_4 = json.dumps({
        "filters": {"incorrect key": "value"}
    })
    print(validate_request(test_4))

    # Test 5: Filters missing
    print("Test 5: Filters missing")
    test_5 = json.dumps({"items": []})
    print(validate_request(test_5))


if __name__ == "__main__":
    tests()
