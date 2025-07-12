from flask import Blueprint, jsonify, request
from services.profile.ProfileServices import ProfileServices

profile_controller = Blueprint('profile_controller', __name__)

@profile_controller.route('/post/create/profile', methods=['POST'])
def register_profile():
    profile_data = request.json
    profile = {
        "name": profile_data.get("name"),
    }

    profile_service = ProfileServices()
    profile_entity = profile_service.insert_profile(profile)
    
    return jsonify({
        "user_id": profile_entity.user_id,
        "name": profile_entity.name,
        "createdAt": profile_entity.createdAt.isoformat()
    }), 201


@profile_controller.route('/get/profile/<string:user_id>', methods=['GET'])
def get_profile(user_id):
    profile_service = ProfileServices()
    profile_entity = profile_service.get_profile(user_id)


    if profile_entity:

        response = jsonify({
            "user_id": profile_entity.user_id,
            "name": profile_entity.name,
            "createdAt": profile_entity.createdAt.isoformat()
        })

        print(f"Profile found: {response.get_json()}")

        return response, 200
    
    return jsonify({"error": "Profile not found"}), 404