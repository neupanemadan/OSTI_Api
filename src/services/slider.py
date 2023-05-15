from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.slider import Slider
import os


class SliderService:
    @classmethod
    def get_all(cls) -> List[Slider]:
        query = Slider.query.filter(Slider.is_deleted != True)
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Slider:
        slider = Slider(**data)
        slider.save()

        return slider



    @classmethod
    def get_by_id(cls, id: int):
        return Slider.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Slider:
        slider = cls.get_by_id(id)
        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/sliders/' + slider.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/sliders/' + file.filename

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        slider = slider.update(data)

        return slider

    @classmethod
    def delete(cls, id: int) -> Slider:
        slider = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/sliders/' + slider.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        slider = slider.update(data)

        return slider
