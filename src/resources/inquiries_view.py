import json
import os
from flask import request, send_from_directory, current_app
from webargs.flaskparser import parser
from src.resources.base import BaseView
from src.services.inquiries import InquiryService
from src.schemas.inquiries import InquiriesSchema
from flask_classful import route
from src.decorators.acl_decorators import auth_required


class InquiriesView(BaseView):
    @auth_required
    def index(self):
        inquiries = InquiryService.get_all()
        return {
            'inquiries': InquiriesSchema(many=True).dump(inquiries)
        }

    # @auth_required
    def post(self):
        print("---------------------")
        print("---------------------")
        data = request.get_json()
        print("000000000000000000-^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(data)
        inquiry = InquiryService.create(data)

        return {
            'inquiry': InquiriesSchema().dump(inquiry)
        }

    @auth_required
    def delete(self, id):
        inquiry = InquiryService.delete(id)
        
        return {
            'inquiry': InquiriesSchema().dump(inquiry)
        }

