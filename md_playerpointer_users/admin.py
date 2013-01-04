"""Admin classes for the ``md-playerpointer-users`` app."""
from django.contrib import admin

from md_playerpointer_users.models import UserCount


admin.site.register(UserCount)
