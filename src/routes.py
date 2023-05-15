from src.resources.default_view import DefaultView
from src.resources.programme_view import ProgrammesView
from src.resources.team_view import TeamsView
from src.resources.about_view import AboutView
from src.resources.setting_view import SettingView
from src.resources.area_view import AreasView
from src.resources.inquiries_view import InquiriesView
from src.resources.client_view import ClientsView
from src.resources.slider_view import SlidersView
from src.resources.notice_view import NoticesView
from src.resources.gallery_view import GalleriesView

from src.resources.auth import AuthView
from src.resources.user import UsersView
from src.resources.docs import DocsView
from src.extensions import apispec


def register(app):
    views = [
        UsersView,
        AuthView,
        DocsView,
        DefaultView,
        ProgrammesView,
        TeamsView,
        AboutView,
        SettingView,
        AreasView,
        InquiriesView,
        ClientsView,
        SlidersView,
        NoticesView,
        GalleriesView
    ]

    excluded_docs = [
        DocsView
    ]

    for view in views:
        view.register(app, trailing_slash=False)
        if view in excluded_docs:
            continue

        apispec.paths(view)

    jwt_scheme = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    apispec.components.security_scheme("jwt", jwt_scheme)
