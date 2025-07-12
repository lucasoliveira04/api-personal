import sys
import os
from services.supabase import get_engine, get_session
from model.Profile import ProfileEntity

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class ProfileServices:
    def __init__(self):
        self.engine = get_engine()
        self.session = get_session()

    def insert_profile(self, profile_data: dict):
        new_profile = ProfileEntity(**profile_data)
       
        self.session.add(new_profile)
        self.session.commit()
        self.session.refresh(new_profile)
        self.session.close()

        return new_profile
    
    def get_profile(self, user_id: str) -> ProfileEntity | bool:
        profile = self.session.query(ProfileEntity).filter(ProfileEntity.user_id == user_id).first()
        if profile:
            return profile
        self.session.close()
        return False

    def update_profile(self, user_id: str, profile_data: dict) -> bool | ProfileEntity:
        profile = self.session.query(ProfileEntity).filter(ProfileEntity.user_id == user_id).first()

        if profile:
            for key, value in profile_data.items():
                setattr(profile, key, value)

            self.session.commit()
            self.session.refresh(profile)
            self.session.close() 
            return profile
        
        self.session.close()
        return False
    