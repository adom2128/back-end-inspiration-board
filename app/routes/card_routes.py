from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from .routes_helpers import validate_model

cards_bp = Blueprint('cards', __name__, url_prefix="/cards")

@cards_bp.route("/<card_id>", methods=["PUT"])
def update_card(card_id):

    card = validate_model(Card, card_id)
    request_body = request.get_json()

    card.likes_count = request_body["likes_count"]

    db.session.commit()

    return make_response({"card": card.to_dict()}), 200



@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return make_response(jsonify(f"Card {card_id} sucessfully deleted"))

