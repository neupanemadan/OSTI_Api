from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.gallery import Gallery
import os


class GalleryService:
    @classmethod
    def get_all(cls) -> List[Gallery]:
        query = Gallery.query.filter(Gallery.is_deleted != True).order_by(Gallery.created_at.desc())
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Gallery:
        gallery = Gallery(**data)
        gallery.save()

        return gallery



    @classmethod
    def get_by_id(cls, id: int):
        return Gallery.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Gallery:
        gallery = cls.get_by_id(id)
        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/galleries/' + gallery.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/galleries/' + file.filename

            cls.checkfile(file, old_filename, new_filename)
        
        gallery = gallery.update(data)

        return gallery

    @classmethod
    def delete(cls, id: int) -> Gallery:
        gallery = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/galleries/' + gallery.filename
        cls.deletefile(path)

        data = {
            "is_deleted" : 1
        }
        gallery = gallery.update(data)

        return gallery
    
    @classmethod
    def checkfile(cls, file, old_filename, new_filename):
        if os.path.exists(old_filename):
            os.remove(old_filename)
            file.save(new_filename)
        else:
            file.save(new_filename)

    @classmethod
    def deletefile(cls, path):
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")
