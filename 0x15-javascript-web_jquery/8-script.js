const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data) => {
    const ulElement = $('UL#list_movies');
    data.results.forEach(movie => {
        ulElement.append(`<li>${movie.title}</li>`);
    });
});