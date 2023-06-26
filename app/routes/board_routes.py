from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helpers import validate_model

board_bp = Blueprint("boards", __name__, url_prefix="/boards")

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return make_response(jsonify({"board": new_board.to_dict()}), 201)


@board_bp.route("/<board_id>/cards", methods=["POST"])
def add_card_to_board(board_id):
    board = validate_model(Board, board_id)

    request_body = request.get_json()
    card_ids_list = request_body["card_ids"]

    for card_id in card_ids_list:
        card = validate_model(Card, card_id)
        card.board_id = board.board_id

        db.session.commit()
    
    board_ids = [card.card_id for card in board.cards]

    return make_response(jsonify({"id": board.board_id, "board_ids": board_ids}), 200)
    

@board_bp.route("", methods=["GET"])
def read_all_boards():
    
    boards = Board.query.all()

    boards_response = [board.to_dict() for board in boards]
    
    return jsonify(boards_response), 200


@board_bp.route("<board_id>/cards",  methods=["GET"])
def get_cards_of_one_board(board_id):
    board = validate_model(Board, board_id)

    cards_response = []
    for card in board.cards:
        cards_response.append(card.to_dict())

    response_body = {
        "id": board.board_id,
        "title": board.title,
        "owner": board.owner,
        "cards": cards_response
        }

    return response_body