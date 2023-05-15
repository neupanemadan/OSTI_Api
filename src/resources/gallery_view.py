import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.gallery import GalleryService
from src.schemas.gallery import GallerySchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class GalleriesView(BaseView):
    # @auth_required
    def index(self):
        galleries = GalleryService.get_all()
        return {
            'galleries': GallerySchema(many=True).dump(galleries)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/galleries/' + file.filename
            file.save(path)
        gallery = GalleryService.create(data)

        return {
            'gallery': GallerySchema().dump(gallery)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        gallery = GalleryService.update(id, data=data, file=file)

        return {
            'gallery': GallerySchema().dump(gallery)
        }

    @auth_required
    def delete(self, id):
        gallery = GalleryService.delete(id)
        
        return {
            'gallery': GallerySchema().dump(gallery)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'galleries')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)