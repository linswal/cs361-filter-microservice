## Description

This microservice filters a list of items (objects) from JSON files.
The main program requests items to be filtered by "category" and/or "date".
This microservice returns only the items with the matching value(s) for the corresponding filters.

## How to programmatically request data

The user will request data for the microservice through a main program's user
interface. The main program will call a function that will open and write the 
request object in input/request.json. An example request is shown below:

Example call in main program: `requestFilterItems(items, filters)`
Example items array (in Javascript):
```
const items = [
    {
        // Required properties for filtering
        category: "categoryName",       // String
        date: "YYYY-MM-DD",             // String

        // Optional properties (include all properties that is part of an item)
        name: "nameOfItem"              // String
        // ... more optional fields 
    },
    // ... more items
]
```

The call `requestFilterItems(items, filters)` will write the following 
request object (in JSON format) in input/request.json:
```
{
    "filters": {                        // Object (required) - must contain at least one of the properties
        "category": "categoryName",     // String (optional)
        "date": "YYYY-MM-DD"            // String (optional)
    },
    "items": [...]                      // Array (required)
}
```

## How to programmatically receive data

Once the microservice is running, it constantly scans the request.json file for any changes.
If the main program writes a request in request.json and it passes the validation from the microservice,
the microservice will filter the items array found in the request and return the matching items.

If the request is valid, the microservice will call: `filter_items(items, filters)` and
write the following response object in output/response.json:
```
{
    "status": "success",                // String (required)
    "new_items": [...]                  // Array (required)
}
```

Otherwise if the request is invalid, the following response object will be written instead:
```
{
    "status": "failure",                // String (required)
    "items": [...]                      // Array of original items (required)
}
```

Once the response object is written in response.json, the main program processes the response. 

## UML Sequence Diagram

