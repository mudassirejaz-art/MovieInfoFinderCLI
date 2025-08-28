import csv

def export_to_csv(movie_data, filename="movies.csv"):
    keys = ["Title", "Year", "Genre", "Director", "Actors", "imdbRating", "Plot"]
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerow({k: movie_data.get(k, "") for k in keys})
        print(f"✅ Movie info exported to {filename}")
    except Exception as e:
        print(f"❌ Error exporting CSV: {e}")
