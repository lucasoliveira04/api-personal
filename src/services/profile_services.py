import os 
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from repository.base_repository import BaseRepository
from model.Profile import ProfileEntity
from config.db import Session

class ProfileServices:
    def __init__(self):
        self.session = Session()

        self.repository = BaseRepository(self.session, ProfileEntity)

    def get_profile_by_id(self, profile_id: int | str) -> ProfileEntity:
        return self.repository.find_by_id(profile_id)
    
    def save_profile(self, profile: ProfileEntity) -> ProfileEntity:
        return self.repository.save(profile)
    
    def get_all(self) -> list[ProfileEntity]:
        return self.repository.find_all()
    
    def delete_profile(self, id : int | str) -> bool:
        try:
            self.repository.delete_by_id(id)
            return True
        except ValueError:
            return False
        
    def delete_many_profiles(self, ids: list[int | str]) -> bool:
        try:
            for id in ids:
                if not self.repository.find_by_id(id):
                    continue

                self.repository.delete_by_id(id)
            return True
        except ValueError:
            return False
            