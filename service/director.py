from models.director import Director as DirectorModel

class DirectorService():
    def __init__(self, db) -> None:
        self.db = db
        

    def get_director(self) -> DirectorModel:
        result = self.db.query(DirectorModel).all()
        return result

    def get_director_by_id(self, id: int):
        result = self.db.query(DirectorModel).filter(DirectorModel.id == id).first()
        return result

    def create_director(self,director:DirectorModel):
        director = DirectorModel(
        dir_fname = director.dir_fname,
        dir_lname = director.dir_lname,
          
        )
        self.db.add(director)
        self.db.commit()
        return

    def update_director(self,id:int, director:DirectorModel):
        director_entity = self.db.query(DirectorModel).filter(DirectorModel.id == id).first()
        director_entity= director.dir_fname
        director_entity= director.dir_lname
        self.db.commit()
        return

    def delete_director(self, id: int):
        director= self.get_director_by_id(id)
        if not director:
            return None
        self.db.delete(director)
        self.db.commit()
        return director