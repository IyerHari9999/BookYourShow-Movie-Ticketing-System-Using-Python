import requests
from bs4 import BeautifulSoup

if __name__!='__main__':
    class Movie:
        def __init__(self,title,cast,rating,poster=None):
            self.title=title
            self.cast=cast
            self.rating=rating
            self.poster=poster

    def getMovieList():         #return movielist
        global movieList
        return movieList

    url = 'https://www.imdb.com/chart/top/'
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')

    movie_tag = soup.select('td.titleColumn a')
    rating_tag = soup.select('td.posterColumn span[name=ir]')

    cast = [tag['title'] for tag in movie_tag]  # list that contains the cast
    titles = [tag.text for tag in movie_tag]  # list of movie titles
    ratings = [float(tag['data-value']) for tag in rating_tag]  # list of ratings of movies
    n = len(titles)  # no of movies scrapped
    # this displays the top 10 movies of imdb with no random condition

    movieList=[]
    for i in range(5):
        # i=random.randrange(0,n)
        print(f'Movie: {titles[i]}\nRating: {ratings[i]:.1f}\nCast: {cast[i]}')
        print()

    for i in range(5):
        movieList.append(Movie(titles[i],cast[i],ratings[i]))

    print(movieList[0].cast)

