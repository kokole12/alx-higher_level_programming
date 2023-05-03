const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json"
$(document).ready(function() {
    $.getJSON(url, function(user_details) {
        $("DIV#character").text(user_details.name);
    });
});
