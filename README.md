# Movie Info Finder CLI 🎬

A **production-ready CLI tool** to fetch detailed movie information from the OMDb API.

---

## Features ✅

* Search movie by name using CLI arguments
* Display detailed info: Title, Year, Genre, Director, Actors, IMDb Rating, Plot
* Optional export to CSV for record keeping
* Clean console output using table format
* Error handling for invalid movie names or API key issues

---

## Setup 🔧

1. Clone this repository:

```bash
git clone https://github.com/mudassirejaz-art/MovieInfoFinderCLI
cd MovieInfoFinderCLI
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Get a free OMDb API key: [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx)
5. Add your API key in `src/omdb_api.py`:

```python
API_KEY = "YOUR_API_KEY"
```

---

## Usage 💻

Search for a movie:

```bash
python src/main.py --movie "Inception"
```

Search and export to CSV:

```bash
python src/main.py --movie "Inception" --export
```

---

## Example Output

```
Field      Value
Title      Inception
Year       2010
Genre      Action, Adventure, Sci-Fi
Director   Christopher Nolan
Actors     Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page
imdbRating 8.8
Plot       A thief who steals corporate secrets through the use of dream-sharing technology...
```

---

## Notes 📌

* Make sure your API key is active and correctly entered
* Works best in Python 3.8+
* CLI tool handles basic errors but ensure internet connection for API calls

---

## License 📝

MIT License
