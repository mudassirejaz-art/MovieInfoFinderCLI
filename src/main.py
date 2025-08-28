import argparse
from omdb_api import fetch_movie
from utils import export_to_csv
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(description="Movie Info Finder CLI")
    parser.add_argument("--movie", required=True, help="Movie title to search")
    parser.add_argument("--export", action="store_true", help="Export result to CSV")
    args = parser.parse_args()

    movie_data, error = fetch_movie(args.movie)
    if error:
        print(f"❌ Error: {error}")
        return

    keys = ["Title", "Year", "Genre", "Director", "Actors", "imdbRating", "Plot"]
    table = [[k, movie_data.get(k, "")] for k in keys]
    print(tabulate(table, headers=["Field", "Value"], tablefmt="fancy_grid"))

    if args.export:
        export_to_csv(movie_data)

if __name__ == "__main__":
    main()
