import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.slider import SliderService
from src.schemas.slider import SliderSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class SlidersView(BaseView):
    # @auth_required
    def index(self):
        sliders = SliderService.get_all()
        return {
            'sliders': SliderSchema(many=True).dump(sliders)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/sliders/' + file.filename
            file.save(path)
        slider = SliderService.create(data)

        return {
            'slider': SliderSchema().dump(slider)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        slider = SliderService.update(id, data=data, file=file)

        return {
            'slider': SliderSchema().dump(slider)
        }

    @auth_required
    def delete(self, id):
        slider = SliderService.delete(id)
        
        return {
            'slider': SliderSchema().dump(slider)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'sliders')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)