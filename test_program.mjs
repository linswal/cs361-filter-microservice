import { readFile, writeFile } from 'fs/promises'


// Example array of items to be filtered
const testItems = [
    {
        name: "Studying",
        category: "Productivity",
        date: "2026-01-10",
        time: "14:30",
        id: 1234
    },
    {
        name: "Jogging",
        category: "Health",
        date: "2026-02-20",
        time: "9:10",
        id: 5678
    },
    {
        name: "Cleaning",
        category: "Productivity",
        date: "2026-02-20",
        time: "10:30",
        id: 9012
    }
];

const exampleFilters = {
    category: "Productivity"
    // , 
    // date: "2026-02-20"
};


async function requestFilterItems(items, filters) {
    const requestObject = { filters, items };
    const jsonRequest = JSON.stringify(requestObject, null, 4);

    console.log("========== REQUEST SENT ================");
    console.log("Sent request to filter items by: ");
    console.log(exampleFilters); 
    await writeFile('./input/request.json', jsonRequest);
}

async function processResponse() {
    const json_response = await readFile('./output/response.json', 'utf8');
    const result = JSON.parse(json_response);
    
    if (result.status === 'success') {
        console.log("========== RESPONSE PROCESSED ==========");
        console.log("Successfully filtered items. Displaying new items:");
        console.log(result.new_items);
    } else{
        console.log("Microservice failed to process request. Displaying original items:");
        console.log(result.items);
    }
}

async function main() {
    // Writes request with list of items and filters
    await requestFilterItems(testItems, exampleFilters);

    // Reads response and print results with 300 ms delay
    setTimeout(processResponse, 300);

}

await main();