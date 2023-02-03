from models.reviewer import Reviewer as reviewerModel

class ReviewerService():
    def __init__(self,db) -> None:
        self.db = db

    def get_reviewer(self) -> reviewerModel:
        result = self.db.query(reviewerModel).all()
        return result

    def create_reviewer(self,reviewer:reviewerModel):
        new_reviewer = reviewerModel(
        rev_id = reviewer.rev_id,
        rev_name = reviewer.rev_name
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return