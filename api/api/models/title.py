"""
title field max_length was based on
https://www.overthinkingit.com/2011/05/17/statistical-analysis-of-movie-title-lengths/
"""

from django.db import models


class Title(models.Model):  # model name
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
    released = models.CharField(max_length=10,
                                blank=False,
                                primary_key=False,
                                help_text="This represents the title launch date.",
                                verbose_name="Launch date",
                                )
    genre = models.CharField(max_length=64,
                             blank=False,
                             primary_key=False,
                             help_text="This represents the title genre.",
                             verbose_name="Genre",
                             )
    plot = models.CharField(max_length=256,
                            blank=False,
                            primary_key=False,
                            help_text="This represents the title plot.",
                            verbose_name="Plot",
                            )
    language = models.CharField(max_length=32,
                                blank=False,
                                primary_key=False,
                                help_text="This represents the title language.",
                                verbose_name="Language",
                                )
    poster = models.URLField(blank=False,
                             primary_key=False,
                             help_text="This represents the title image URL.",
                             verbose_name="Poster URL",
                             )
    imdb_rating = models.FloatField(max_length=6,
                                    blank=False,
                                    primary_key=False,
                                    help_text="This represents the title rating.",
                                    verbose_name="Rating",
                                    )
    total_seasons = models.IntegerField(max_length=3,
                                        blank=False,
                                        primary_key=False,
                                        help_text="This represents the title number of seasons.",
                                        verbose_name="Number of seasons",
                                        )

    def __str__(self):
        return self.title
