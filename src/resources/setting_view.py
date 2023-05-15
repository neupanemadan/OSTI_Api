import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.setting import SettingService
from src.schemas.setting import SettingSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class SettingView(BaseView):
    # @auth_required
    def index(self):
        setting = SettingService.get_all()
        return {
            'setting': SettingSchema(many=True).dump(setting)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/setting/' + file.filename
            file.save(path)
        setting = SettingService.create(data)

        return {
            'setting': SettingSchema().dump(setting)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        setting = SettingService.update(id, data=data, file=file)

        return {
            'setting': SettingSchema().dump(setting)
        }

    @auth_required
    def delete(self, id):
        setting = SettingService.delete(id)
        
        return {
            'setting': SettingSchema().dump(setting)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'setting')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)