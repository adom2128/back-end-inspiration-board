from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")


@board_bp.route("", methods=["GET"])
def read_all_boards():
    
    boards = Board.query.all()

    board_response = []
    
    for board in boards:
        board_response.append(board.to_dict())

    return jsonify(board_response), 200