from flask import Blueprint, jsonify
from model.Profile import ProfileEntity, Base
from services.supabase import get_engine


profile_controller = Blueprint('profile_controller', __name__)

@profile_controller.route('/create/table', methods=['GET'])
def register_profile():
    engine = get_engine()
    Base.metadata.create_all(engine)
    return jsonify({"message": "Tabela de perfis criada com sucesso!"}), 201
