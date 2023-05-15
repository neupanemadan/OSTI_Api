from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.setting import Setting
import os


class SettingService:
    @classmethod
    def get_all(cls) -> List[Setting]:
        query = Setting.query
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Setting:
        setting = Setting(**data)
        setting.save()

        return setting



    @classmethod
    def get_by_id(cls, id: int):
        return Setting.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Setting:
        setting = cls.get_by_id(id)

        old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/setting/' + setting.filename
        if file:
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/setting/' + file.filename

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        setting = setting.update(data)

        return setting

    @classmethod
    def delete(cls, id: int) -> Setting:
        setting = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/setting/' + setting.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        setting = setting.update(data)

        return setting
