from django.contrib import admin
from .models.episode import Episode
from .models.genre import Genre
from .models.language import Language
from .models.season import Season
from .models.title import Title


class Episodes(admin.ModelAdmin):  # Adding model on admin console
    # Choosing what fields will be displayed on admin
    list_display = ("episode_owner_title", "episode_owner_season", "title")
    list_display_links = ("title",)


class Genres(admin.ModelAdmin):
    list_display = ("genre_owner_title", "name")
    list_display_links = ("name",)


class Languages(admin.ModelAdmin):
    list_display = ("language_owner_title", "name")
    list_display_links = ("name", )


class Seasons(admin.ModelAdmin):
    list_display = ("season_owner_title", "season_number", )
    list_display_links = ("season_owner_title", "season_number", )


class Titles(admin.ModelAdmin):
    list_display = ("imdb_id", "title")


admin.site.register(Episode, Episodes)  # Registering model on admin console
admin.site.register(Genre, Genres)
admin.site.register(Language, Languages)
admin.site.register(Season, Seasons)
admin.site.register(Title, Titles)
