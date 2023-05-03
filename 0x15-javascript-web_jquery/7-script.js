const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(document).ready(function () {
  $.getJSON(url, function (userDetails) {
    $('DIV#character').text(userDetails.name);
  });
});

// const request  = require('request')
// const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"

// request.get(url, (error, response, body) => {
//     if(error) {
//         console.log(error);
//     }
//     const user_name = JSON.parse(body)
//     console.log(user_name.name)
// });
