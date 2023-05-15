from typing import List
from flask import current_app
from typing import List, Dict, Union
from src.models.inquiries import Inquiry
import os


class InquiryService:
    @classmethod
    def get_all(cls) -> List[Inquiry]:
        query = Inquiry.query.filter(Inquiry.is_deleted != True)
        return query.all()

    @classmethod
    def create(cls, data: Dict[str, Union[str, Dict]]) -> Inquiry:
        inquiry = Inquiry(**data)
        inquiry.save()

        return inquiry



    @classmethod
    def get_by_id(cls, id: int):
        return Inquiry.query.get_or_404(id)



    @classmethod
    def delete(cls, id: int) -> Inquiry:
        inquiry = cls.get_by_id(id)

        data = {
            "is_deleted" : 1
        }
        inquiry = inquiry.update(data)

        return inquiry
