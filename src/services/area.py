from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.area import Area
import os


class AreaService:
    @classmethod
    def get_all(cls) -> List[Area]:
        query = Area.query.filter(Area.is_deleted != True)
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Area:
        area = Area(**data)
        area.save()

        return area



    @classmethod
    def get_by_id(cls, id: int):
        return Area.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Area:
        area = cls.get_by_id(id)
        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/areas/' + area.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/areas/' + file.filename

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        area = area.update(data)

        return area

    @classmethod
    def delete(cls, id: int) -> Area:
        area = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/areas/' + area.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        area = area.update(data)

        return area
