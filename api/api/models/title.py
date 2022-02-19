from django.db import models


class Title(models.Model):  # model name
    """
    A model for title table
    """
    imdb_id = models.CharField(max_length=10,  # field max length
                               blank=False,  # required
                               primary_key=True,  # is a primary key
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
    imdb_rating = models.FloatField(blank=False,
                                    primary_key=False,
                                    help_text="This represents the title rating.",
                                    verbose_name="Rating",
                                    )

    def __str__(self):
        return self.title
