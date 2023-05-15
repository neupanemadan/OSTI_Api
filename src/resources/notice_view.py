import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.notice import NoticeService
from src.schemas.notice import NoticeSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class NoticesView(BaseView):
    # @auth_required
    def index(self):
        notices = NoticeService.get_all()
        return {
            'notices': NoticeSchema(many=True).dump(notices)
        }
    
    def get(self, id):
        notice = NoticeService.get_by_id(id)
        print('-------------------')
        print(id)
        print(notice)
        if not notice:
            return {'errors': 'notice not found'}, 422

        return {
            'notice': NoticeSchema().dump(notice)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/notices/' + file.filename
            file.save(path)
        notice = NoticeService.create(data)

        return {
            'notice': NoticeSchema().dump(notice)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        notice = NoticeService.update(id, data=data, file=file)

        return {
            'notice': NoticeSchema().dump(notice)
        }

    @auth_required
    def delete(self, id):
        notice = NoticeService.delete(id)
        
        return {
            'notice': NoticeSchema().dump(notice)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'notices')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)