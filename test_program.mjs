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
    }
];

const exampleFilters = {
    category: "Health"
};


async function requestFilterItems(items, filters) {
    const requestObject = { filters, items };
    const jsonRequest = JSON.stringify(requestObject, null, 4);

    await writeFile('./input/request.json', jsonRequest);
}

async function processResponse() {
    const json_response = await readFile('./output/response.json', 'utf8');
    const result = JSON.parse(json_response);

    if (result.status === 'success') {
        console.log("Items were filtered successfully. Displaying filtered items:");
        console.log(result.items);
    } else{
        console.log("Microservice failed to process request. Displaying original items:");
        console.log(result.items);
    }
}

async function main() {
    // Writes request with list of items and filters
    await requestFilterItems(testItems, exampleFilters);

    // Reads response and print results with 100 ms delay
    setTimeout(processResponse, 100);

}

await main();