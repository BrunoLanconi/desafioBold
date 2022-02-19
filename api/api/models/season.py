from django.db import models
from .title import Title


class Season(models.Model):  # model name
    """
    A model for season table
    """
    title = models.CharField(max_length=96,
                             blank=False,
                             primary_key=False,
                             help_text="This represents the season title presentation name.",
                             verbose_name="Season title name",
                             )
    season_number = models.PositiveSmallIntegerField(blank=False,
                                                     primary_key=False,
                                                     help_text="This represents the season number.",
                                                     verbose_name="Season number",
                                                     )
    seasons = models.ForeignKey(Title,  # Foreign key class
                                on_delete=models.CASCADE,  # What happens when deleted
                                related_name="seasons",
                                help_text="This represents the season owner title.",
                                verbose_name="Season owner",
                                )  # Sets a foreign key

    def __str__(self):
        return self.title
