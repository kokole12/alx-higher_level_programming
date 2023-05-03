const url = "https://fourtonfish.com/hellosalut/?lang=fr"
$(document).ready(function() {
    $.getJSON(url, function(greeting) {
        $("DIV#hello").text(greeting.hello);
    });
});
