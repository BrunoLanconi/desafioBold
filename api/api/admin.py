from django.contrib import admin
from .models.title import Title
from .models.season import Season
from .models.episode import Episode


class Titles(admin.ModelAdmin):  # Adding model on admin console
    # Choosing what fields will be displayed on admin
    list_display = ("imdb_id", "title")


class Seasons(admin.ModelAdmin):
    list_display = ("title_id", "title")


class Episodes(admin.ModelAdmin):
    list_display = ("title_id", "season_id", "title")


admin.site.register(Title, Titles)  # Registering model on admin console
admin.site.register(Season, Seasons)
admin.site.register(Episode, Episodes)
