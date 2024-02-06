from django.contrib import admin
from .models import Excerpt
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Excerpt)
class ExcerptAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
