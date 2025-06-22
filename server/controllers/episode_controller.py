from flask import Blueprint, jsonify, request, abort
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.app import db

bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@bp.route('', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    data = [{"id": e.id, "date": e.date.isoformat(), "number": e.number} for e in episodes]
    return jsonify(data), 200

@bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [
        {
            "id": app.id,
            "guest_id": app.guest_id,
            "guest_name": app.guest.name,
            "rating": app.rating
        }
        for app in episode.appearances
    ]
    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number,
        "appearances": appearances
    }), 200

# JWT-protected route — make sure you wrap this later with @jwt_required()
@bp.route('/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({"message": f"Episode {id} deleted"}), 200