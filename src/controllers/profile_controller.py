from flask import Blueprint, jsonify, request
from services.profile.ProfileServices import ProfileServices

profile_controller = Blueprint('profile_controller', __name__)

@profile_controller.route('/post/create/profile', methods=['POST'])
def register_profile():
    profile_data = request.json
    profile = {
        "name": profile_data.get("name"),
        "role": profile_data.get("role", "admin") 
    }

    profile_service = ProfileServices()
    profile_entity = profile_service.insert_profile(profile)
    
    return jsonify({
        "user_id": profile_entity.user_id,
        "name": profile_entity.name,
        "role": profile_entity.role,
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
            "role": profile_entity.role,
            "createdAt": profile_entity.createdAt.isoformat()
        })

        print(f"Profile found: {response.get_json()}")

        return response, 200
    
    return jsonify({"error": "Profile not found"}), 404


@profile_controller.route('/put/profile/<string:user_id>', methods=['PUT'])
def update_profile(user_id):
    profile_data = request.json

    profile = {
        "name": profile_data.get("name"),
        "role": profile_data.get("role", "admin") 
    }

    profile_service = ProfileServices()
    profile_entity = profile_service.update_profile(user_id, profile)

    if profile_entity:
        return jsonify({
            "user_id": profile_entity.user_id,
            "name": profile_entity.name,
            "role": profile_entity.role,
            "createdAt": profile_entity.createdAt.isoformat()
        }), 200
    
    return jsonify({"error": "Profile not found"}), 404

@profile_controller.route('/delete/profile/<string:user_id>', methods=['DELETE'])
def delete_profile(user_id):
    profile_service = ProfileServices()
    success = profile_service.delete_profile(user_id)

    if success:
        return jsonify({"message": "Profile deleted successfully"}), 200
    
    return jsonify({"error": "Profile not found"}), 404