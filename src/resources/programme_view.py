import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.programme import ProgrammeService
from src.schemas.programme import ProgrammeSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class ProgrammesView(BaseView):
    # @auth_required
    def index(self):
        programmes = ProgrammeService.get_all()
        return {
            'programmes': ProgrammeSchema(many=True).dump(programmes)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/programmes/' + file.filename
            file.save(path)
        # data = parser.parse(ProgrammeSchema(), request)
        programme = ProgrammeService.create(data)

        return {
            'programme': ProgrammeSchema().dump(programme)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        programme = ProgrammeService.update(id, data=data, file=file)

        return {
            'programme': ProgrammeSchema().dump(programme)
        }

    @auth_required
    def delete(self, id):
        programme = ProgrammeService.delete(id)
        
        return {
            'programme': ProgrammeSchema().dump(programme)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'programmes')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)