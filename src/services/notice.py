from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.notice import Notice
import os
import datetime


class NoticeService:
    @classmethod
    def get_all(cls) -> List[Notice]:
        query = Notice.query.filter(Notice.is_deleted != True).order_by(Notice.created_at.desc())
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Notice:
        data['date']= datetime.date.today()
        notice = Notice(**data)
        notice.save()

        return notice



    @classmethod
    def get_by_id(cls, id: int):
        return Notice.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Notice:
        notice = cls.get_by_id(id)
        data['date']= datetime.date.today()
        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/notices/' + notice.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/notices/' + file.filename

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        notice = notice.update(data)

        return notice

    @classmethod
    def delete(cls, id: int) -> Notice:
        notice = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/notices/' + notice.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        notice = notice.update(data)

        return notice
