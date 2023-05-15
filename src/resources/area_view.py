import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.area import AreaService
from src.schemas.area import AreaSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class AreasView(BaseView):
    # @auth_required
    def index(self):
        areas = AreaService.get_all()
        return {
            'areas': AreaSchema(many=True).dump(areas)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/areas/' + file.filename
            file.save(path)
        area = AreaService.create(data)

        return {
            'area': AreaSchema().dump(area)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        area = AreaService.update(id, data=data, file=file)

        return {
            'area': AreaSchema().dump(area)
        }

    @auth_required
    def delete(self, id):
        area = AreaService.delete(id)
        
        return {
            'area': AreaSchema().dump(area)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'areas')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)