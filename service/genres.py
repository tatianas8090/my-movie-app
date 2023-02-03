from models.genres import Genres as Genres

class GenreService():
    def __init__(self,db) -> None:
        self.db = db

    def get_genres(self):
        result = self.db.query(Genres).all()
        return result

    def get_genre_by_id(self, id: int):
        result = self.db.query(Genres).filter(Genres.id == id).first()
        return result

    def create_genre(self,genre:Genres):
        genre = Genres(
        gen_title = genre.gen_title,
        
          
        )
        self.db.add(genre)
        self.db.commit()
        return

    def update_genre(self,id:int, genre:Genres):
        genre_entity = self.db.query(Genres).filter(Genres.id == id).first()
        genre_entity.gen_title = genre.gen_title
        self.db.commit()
        return

    def delete_genre(self, id: int):
        genre= self.get_genre_by_id(id)
        if not genre:
            return None
        self.db.delete(genre)
        self.db.commit()
        return genre
