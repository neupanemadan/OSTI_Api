from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.client import Client
import os


class ClientService:
    @classmethod
    def get_all(cls) -> List[Client]:
        query = Client.query.filter(Client.is_deleted != True)
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Client:
        client = Client(**data)
        client.save()

        return client



    @classmethod
    def get_by_id(cls, id: int):
        return Client.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Client:
        client = cls.get_by_id(id)
        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/clients/' + client.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/clients/' + file.filename

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        client = client.update(data)

        return client

    @classmethod
    def delete(cls, id: int) -> Client:
        client = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/clients/' + client.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        client = client.update(data)

        return client
