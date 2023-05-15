from typing import List
from flask import request, send_from_directory, current_app
from typing import ClassVar, List, Dict, Union, Tuple
from src.models.programme import Programme
import os


class ProgrammeService:
    @classmethod
    def get_all(cls) -> List[Programme]:
        query = Programme.query.filter(Programme.is_deleted != True)
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Programme:
        # revision_data: Dict[str, Union[str, int]] = data.pop('revision')   # type: ignore
        programme = Programme(**data)
        programme.save()

        return programme
    #     cls._create_document_revision(document=programme, data=revision_data, file=file)

    # @classmethod
    # def _create_document_revision(cls, document: Programme, data: Dict[str, Union[str, int]], file) -> DocumentRevision:
    #     revision_no = len(document.revisions) + 1
    #     data['filename'] = cls._get_filename(file, category=category, revision_no=revision_no)
    #     data['revision_no'] = revision_no
    #     data['document_id'] = document.id
    #     data['created_by'] = current_user.id
    #     revision = DocumentRevision(**data)
    #     revision.save()


    #     # uploading file
    #     cls._upload_file(file=file, revision=revision)

    #     return revision


    @classmethod
    def get_by_id(cls, id: int):
        return Programme.query.get_or_404(id)


    @classmethod
    def update(cls, id: int, data: Dict[str, Union[str, Dict]], file) -> Programme:
        # revision_data: Dict[str, Union[str, int]] = data.pop('revision')   # type: ignore
        programme = cls.get_by_id(id)

        if file:
            old_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/programmes/' + programme.filename
            new_filename = current_app.config['IMAGE_DRIVE_ROOT'] + '/programmes/' + file.filename
            # if file:
            #     path = current_app.config['IMAGE_DRIVE_ROOT'] + '/programmes/' + file.filename
            #     file.save(path)

            if os.path.exists(old_filename):
                os.remove(old_filename)
                file.save(new_filename)
            else:
                file.save(new_filename)
        
        programme = programme.update(data)
        # cls._create_document_revision(document, data=revision_data, file=file)

        return programme

    @classmethod
    def delete(cls, id: int) -> Programme:
        # revision_data: Dict[str, Union[str, int]] = data.pop('revision')   # type: ignore
        programme = cls.get_by_id(id)
        path = current_app.config['IMAGE_DRIVE_ROOT'] + '/programmes/' + programme.filename
        if os.path.exists(path):
            os.remove(path)
        else:
            print("The file does not exist")

        data = {
            "is_deleted" : 1
        }
        programme = programme.update(data)
        # cls._create_document_revision(document, data=revision_data, file=file)

        return programme
