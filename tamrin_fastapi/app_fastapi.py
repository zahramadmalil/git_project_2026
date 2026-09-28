from fastapi_offline import FastAPIOffline
import app_db

app = FastAPIOffline()





# ---------- دریافت همه فیلم‌ها (GET) ----------
@app.get('/movies/')
def get_all_movies():
    rows = app_db.select_all_records()
    movies = []
    for row in rows:
        movies.append({
            'id': row[0],
            'title': row[1],
            'year': row[2],
            'country': row[3],
            'imdb_rate': row[4]
        })
    return {'movies': movies}


# ---------- دریافت یک فیلم بر اساس id (GET) ----------
@app.get('/movies/{movie_id}')
def get_movie(movie_id: int):
    row = app_db.select_record_by_id(movie_id)
    if row is None:
        return {'error': f'movie with id {movie_id} not found'}
    return {
        'id': row[0],
        'title': row[1],
        'year': row[2],
        'country': row[3],
        'imdb_rate': row[4]
    }


# ---------- افزودن فیلم جدید (POST) ----------
@app.post('/movies/add/')
def add_movie(title: str, year: str, country: str, imdb_rate: float):
    app_db.insert_record(title, year, country, imdb_rate)
    return {'message': f'movie "{title}" added successfully'}


# ---------- حذف فیلم بر اساس id (DELETE) ----------
@app.delete('/movies/delete/{movie_id}')
def delete_movie(movie_id: int):
    row = app_db.select_record_by_id(movie_id)
    if row is None:
        return {'error': f'movie with id {movie_id} not found'}
    app_db.delete_record_by_id(movie_id)
    return {'message': f'movie with id {movie_id} deleted successfully'}


# ---------- آپدیت فیلم بر اساس id (PUT) ----------
@app.put('/movies/update/{movie_id}')
def update_movie(movie_id: int, year: str, imdb_rate: float):
    row = app_db.select_record_by_id(movie_id)
    if row is None:
        return {'error': f'movie with id {movie_id} not found'}
    app_db.update_record_by_id(movie_id, year, imdb_rate)
    return {'message': f'movie with id {movie_id} updated successfully'}