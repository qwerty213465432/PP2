
def high5_5(movie):
    return movie["imdb"] > 5.5


def filthigh5_5(movies):
    return [movie for movie in movies if high5_5(movie)]


def cat(movies, category):
    return [movie for movie in movies if movie["category"] == category]


def avg(movies):
    if not movies:
        return 0
    total = sum(movie["imdb"] for movie in movies)
    return total / len(movies)


def avgcat(movies, category):
    catmov= cat(movies, category)
    return avg(catmov)













"Dictionary of movies"


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

high5_5({"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"})
filthigh5_5(movies)
cat(movies, "Romance")
avg(movies)
avgcat(movies, "Romance")


"""

print(high5_5({"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}))  # True

print(filthigh5_5(movies))

print(cat(movies, "Romance"))

print(avg(movies))

print(avgcat(movies, "Romance"))

"""