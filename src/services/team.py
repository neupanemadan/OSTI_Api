from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.team import Team
import os


class TeamService:
    @classmethod
    def get_all(cls) -> List[Team]:
        query = Team.query.filter(Team.is_deleted != True).order_by(Team.created_at.desc())
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Team:
        team = Team(**data)
        team.save()

        return team



    @classmethod
    def get_by_id(cls, id: int):
        return Team.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Team:
        team = cls.get_by_id(id)
        
        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/teams/' + team.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/teams/' + file.filename

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        team = team.update(data)

        return team

    @classmethod
    def delete(cls, id: int) -> Team:
        team = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/teams/' + team.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        team = team.update(data)

        return team
