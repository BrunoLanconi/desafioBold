from django.contrib import admin
from .models.episode import Episode
from .models.genre import Genre
from .models.release import TitleRelease, EpisodeRelease
from .models.season import Season
from .models.title import Title


class Episodes(admin.ModelAdmin):  # Adding model on admin console
    list_display = ("title_id", "episodes", "title")  # Choosing what fields will be displayed on admin


class Genres(admin.ModelAdmin):
    list_display = ("genres", "name")


class TitleReleases(admin.ModelAdmin):
    list_display = ("title_release", )


class EpisodeReleases(admin.ModelAdmin):
    list_display = ("episode_release", )


class Seasons(admin.ModelAdmin):
    list_display = ("season_number", )


class Titles(admin.ModelAdmin):
    list_display = ("imdb_id", "title")


admin.site.register(Episode, Episodes)  # Registering model on admin console
admin.site.register(Genre, Genres)
admin.site.register(TitleRelease, TitleReleases)
admin.site.register(EpisodeRelease, EpisodeReleases)
admin.site.register(Season, Seasons)
admin.site.register(Title, Titles)
