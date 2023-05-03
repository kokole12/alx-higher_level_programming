const { error } = require('console')
const request  = require('request')
const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"

request.get(url, (error, response, body) => {
    if(error) {
        console.log(error);
    }
    console.log(body);
});
