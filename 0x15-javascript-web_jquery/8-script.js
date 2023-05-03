const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(document).ready(function () {
  $.getJSON(url, function (movies) {
    movies.results.forEach(function (movie) {
      $('<li>').text(movie.title).appendTo('UL#list_movies');
    });
  });
});
