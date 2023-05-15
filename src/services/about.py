from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.about import About
import os


class AboutService:
    @classmethod
    def get_all(cls) -> List[About]:
        query = About.query
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> About:
        about = About(**data)
        about.save()

        return about



    @classmethod
    def get_by_id(cls, id: int):
        return About.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> About:
        about = cls.get_by_id(id)

        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/about/' + about.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/about/' + file.filename

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        about = about.update(data)

        return about

    @classmethod
    def delete(cls, id: int) -> About:
        about = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/about/' + about.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        about = about.update(data)

        return about
