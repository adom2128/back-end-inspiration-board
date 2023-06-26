from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

<<<<<<< HEAD
board_bp = Blueprint("boards", __name__, url_prefix="/boards")

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return make_response(jsonify({"board": new_board.to_dict()}), 201)
=======
# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")


@board_bp.route("", methods=["GET"])
def read_all_boards():
    
    boards = Board.query.all()

    board_response = []
    
    for board in boards:
        board_response.append(board.to_dict())

    return jsonify(board_response), 200
>>>>>>> 23508a16e65dcf3396a7b5da2d338a392091fcf4
