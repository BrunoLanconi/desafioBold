from django.contrib import admin
from .models.title import Title


class Titles(admin.ModelAdmin):  # Adding model on admin console
    # Choosing what fields will be displayed on admin
    list_display = ("imdb_id", "title")


admin.site.register(Title, Titles)  # Registering model on admin console
