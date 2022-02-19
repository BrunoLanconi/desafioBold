from django.contrib import admin
from .models.episode import Episode
from .models.genre import Genre
from .models.season import Season
from .models.title import Title


class Titles(admin.ModelAdmin):  # Adding model on admin console
    # Choosing what fields will be displayed on admin
    list_display = ("imdb_id", "title")


class Seasons(admin.ModelAdmin):
    list_display = ("title", )


class Episodes(admin.ModelAdmin):
    list_display = ("title_id", "episodes", "title")


class Genres(admin.ModelAdmin):
    list_display = ("genres", "name")


admin.site.register(Episode, Episodes)  # Registering model on admin console
admin.site.register(Genre, Genres)
admin.site.register(Season, Seasons)
admin.site.register(Title, Titles)
