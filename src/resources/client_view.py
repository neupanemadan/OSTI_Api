import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.client import ClientService
from src.schemas.client import ClientSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class ClientsView(BaseView):
    # @auth_required
    def index(self):
        clients = ClientService.get_all()
        return {
            'clients': ClientSchema(many=True).dump(clients)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/clients/' + file.filename
            file.save(path)
        client = ClientService.create(data)

        return {
            'client': ClientSchema().dump(client)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        client = ClientService.update(id, data=data, file=file)

        return {
            'client': ClientSchema().dump(client)
        }

    @auth_required
    def delete(self, id):
        client = ClientService.delete(id)
        
        return {
            'client': ClientSchema().dump(client)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'clients')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)