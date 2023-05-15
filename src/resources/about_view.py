import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.about import AboutService
from src.schemas.about import AboutSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class AboutView(BaseView):
    # @auth_required
    def index(self):
        about = AboutService.get_all()
        return {
            'about': AboutSchema(many=True).dump(about)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/about/' + file.filename
            file.save(path)
        about = AboutService.create(data)

        return {
            'about': AboutSchema().dump(about)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        about = AboutService.update(id, data=data, file=file)

        return {
            'about': AboutSchema().dump(about)
        }

    @auth_required
    def delete(self, id):
        about = AboutService.delete(id)
        
        return {
            'about': AboutSchema().dump(about)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'about')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)