import media
import fresh_tomatoes

# creating movies (instances of the class Movie)
schindlers=media.Movie("Schindler's List",
                       "In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.",
                       "https://www.o-cinema.org/wp-content/uploads/2015/06/schindlers-list-52e73e7ba8e35-260x371.jpg",
                       "https://www.youtube.com/watch?v=gG22XNhtnoY")

avengers=media.Movie("Avengers",
                       "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

john_wick=media.Movie("John Wick Chapter 2",
                       "After returning to the criminal underworld to repay a debt, John Wick discovers that a large bounty has been put on his life.",
                       "http://www.dvdsreleasedates.com/posters/300/J/John-Wick-Chapter-Two-2017.jpg",
                       "https://www.youtube.com/watch?v=XGk2EfbD_Ps")

now=media.Movie("Now you see me",
                       "An F.B.I. Agent, and an Interpol Detective, track a team of illusionists, who pull off bank heists during their performances, and reward their audiences with the money.",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Now_You_See_Me_2_poster.jpg/220px-Now_You_See_Me_2_poster.jpg",
                       "https://www.youtube.com/watch?v=4OtM9j2lcUA")

inception=media.Movie("Inception",
                       "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=8hP9D6kZseM")

wolverine=media.Movie("X-Men Orgins: Wolverine",
                       "A look at Wolverine's early life, in particular his time with the government squad Team X and the impact it will have on his later years.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BZWRhMzdhMzEtZTViNy00YWYyLTgxZmUtMTMwMWM0NTEyMjk3XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=kd6zYnHwQWA")

list=[schindlers,avengers,john_wick,now,inception,wolverine]

fresh_tomatoes.open_movies_page(list) #generate the file (.html) that show the movies information
