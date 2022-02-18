"""
title field max_length was based on
https://www.overthinkingit.com/2011/05/17/statistical-analysis-of-movie-title-lengths/
"""

from django.db import models


class Sample(models.Model):  # model name
    """
    A model for title table
    """
    imdb_id = models.CharField(max_length=10,  # field max length
                               blank=False,  # required
                               primary_key=True,  # not is a primary key
                               help_text="This represents the title ID.",  # field guide
                               verbose_name="Title ID",  # human readable field definition
                               )  # field definition
    title = models.CharField(max_length=96,
                             blank=False,
                             primary_key=False,
                             help_text="This represents the title presentation name.",
                             verbose_name="Title name",
                             )
    released = models.DateField(max_length=10,
                                blank=False,
                                primary_key=False,
                                help_text="This represents the title launch date.",
                                verbose_name="Launch date",
                                )
    genre
    plot
    language
    poster
    imdb_rating
    total_seasons

    def __str__(self):
        return self.name
