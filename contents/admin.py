from django.contrib import admin
from contents import models as content_models


@admin.register(content_models.Content)
class ContentAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        "slug": ("title",),
    }

    list_display = (
        "title",
        "rating",
        "released",
        "media_type",
        "count_reviews",
    )

    list_filter = ("media_type",)

    ordering = ("-released",)
