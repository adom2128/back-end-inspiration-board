from app import db
from flask import abort, make_response, jsonify

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(40), nullable=False)
    likes_count = db.Column(db.Integer)
    color = db.Column(db.String, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey("board.board_id"))
    board = db.relationship("Board", back_populates="cards")

    @classmethod
    def from_dict(cls, card_data):
        try:
            new_card = Card(message=card_data["message"])
        except KeyError:
            abort(make_response(jsonify({"details": "Invalid data"}), 400))

        return new_card

    def to_dict(self):
        return dict(
                id=self.card_id,
                message=self.message,
                likes_count=self.likes_count,
                board_id=self.board_id,
            )