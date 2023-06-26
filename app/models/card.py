from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(40), nullable=False)
    likes_count = db.Column(db.Integer)
    color = db.Column(db.String, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey("board.board_id"))
    board = db.relationship("Board", back_populates="card")



    def to_dict(self):
        card_dict = dict(
                id = self.id,
                message = self.message,
                likes_count = self.likes_count,
                board_id = self.board_id
            )

        return card_dict 