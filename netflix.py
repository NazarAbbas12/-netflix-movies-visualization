
import pandas as pd
import matplotlib.pyplot as plt


netflix_df = pd.read_csv("netflix_data.csv")


netflix_movies = netflix_df[netflix_df["type"] == "Movie"]

netflix_movies = netflix_movies.dropna(subset=["release_year", "duration", "country", "genre", "date_added"])

# MOVIE DURATION IN 90s
movies_1990s = netflix_movies.query("1990 <= release_year < 2000")

plt.figure(figsize=(8, 5))
plt.hist(movies_1990s["duration"], bins=20, color="skyblue", edgecolor="black")
plt.title("Movies Duration in 1990s")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("movie_duration_1990s.png", dpi=300)
plt.show()

# MOVIES PER YEAR
plt.figure(figsize=(8, 5))
plt.hist(netflix_movies["release_year"], bins=20, color="lightcoral", edgecolor="black")
plt.title("Distribution of Movies by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Movies")
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("movies_per_year.png", dpi=300)
plt.show()

# TOP MOVIE-PRODUCING COUNTRIES
top_countries = netflix_movies["country"].value_counts().head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_countries.index, top_countries.values, color="steelblue")
plt.title("Top 10 Movie-Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("top_movie_countries.png", dpi=200)
plt.show()

# TOP MOVIE GENRES
top_genres = netflix_movies["genre"].value_counts().head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_genres.index, top_genres.values, color="mediumseagreen")
plt.title("Top 10 Movie Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("top_movie_genres.png", dpi=200)
plt.show()

# MOVIES OVER TIME
netflix_movies["year_added"] = pd.to_datetime(netflix_movies["date_added"]).dt.year
yearly_counts = netflix_movies["year_added"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.plot(yearly_counts.index, yearly_counts.values, marker="o", linestyle="-", color="darkorange")
plt.title("Movies Added to Netflix Over Time")
plt.xlabel("Year Added")
plt.ylabel("Number of Movies")
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig("movies_added_over_time.png", dpi=300)
plt.show()
