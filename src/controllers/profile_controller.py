import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Blueprint, jsonify, request
from services.profile_services import ProfileServices
from model.Profile import ProfileEntity

profile_controller = Blueprint('profile_controller', __name__)

profile_services = ProfileServices()

@profile_controller.route('/get/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id: int):
    profile = profile_services.get_profile_by_id(profile_id)
    if profile:
        return jsonify(profile.to_dict()), 200
    return jsonify({'error': 'Profile not found'}), 404

@profile_controller.route('/post/create/profile', methods=['POST'])
def create_profile():
    data = request.json
    
    body = {
        'name': data.get('name'),
        'role': data.get('role')
    }
     

    if not body.get('name'):
        return jsonify({'error': 'Name is required'}), 400
    
    profile = profile_services.save_profile(ProfileEntity(**body))
    return jsonify(profile.to_dict()), 201

@profile_controller.route('/delete/profile/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id: int):
    isDeleted = profile_services.delete_profile(profile_id)
    if isDeleted:
        return jsonify({'message': 'Profile deleted successfully'}), 200
    return jsonify({'error': 'Profile not found'}), 404

@profile_controller.route('/post/delete/many/profiles', methods=['POST'])
def delete_many_profiles():
    data = request.json
    ids = data.get('ids', [])

    if not ids:
        return jsonify({'error': 'No IDs provided'}), 400
    
    isDeleted = profile_services.delete_many_profiles(ids)
    if isDeleted:
        return jsonify({'message': 'Profiles deleted successfully'}), 200
    return jsonify({'error': 'One or more profiles not found'}), 404
