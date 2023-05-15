import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.team import TeamService
from src.schemas.team import TeamSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class TeamsView(BaseView):
    # @auth_required
    def index(self):
        teams = TeamService.get_all()
        return {
            'teams': TeamSchema(many=True).dump(teams)
        }

    @auth_required
    def post(self):
        file = request.files.get('file')
        data = json.loads(request.form['data'])
        if file:
            path = current_app.config['IMAGE_DRIVE_ROOT'] + '/teams/' + file.filename
            file.save(path)
        team = TeamService.create(data)

        return {
            'team': TeamSchema().dump(team)
        }

    @auth_required
    def put(self, id):
        data = json.loads(request.form['data'])
        file = request.files.get('file')

        team = TeamService.update(id, data=data, file=file)

        return {
            'team': TeamSchema().dump(team)
        }

    @auth_required
    def delete(self, id):
        team = TeamService.delete(id)
        
        return {
            'team': TeamSchema().dump(team)
        }


    @route('/<filename>')
    def download(self, filename: str):
        directory = os.path.join(current_app.config['IMAGE_DRIVE_ROOT'], 'teams')
        return send_from_directory(directory=directory, path=filename, as_attachment=True)