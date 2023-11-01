$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      for (const movie of data.results) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      }
    }
  });
});
