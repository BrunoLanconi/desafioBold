from django.db import models
from .season import Season
from .title import Title


class Episode(models.Model):  # model name
    """
    A model for episode table
    """
    imdb_id = models.CharField(max_length=10,
                               blank=False,
                               primary_key=True,
                               help_text="This represents the episode ID.",
                               verbose_name="Episode ID",
                               )
    title_id = models.ForeignKey(Title,
                                 on_delete=models.CASCADE,
                                 blank=False,
                                 help_text="This represents the episode owner title.",
                                 verbose_name="Episode owner title",
                                 )
    title = models.CharField(max_length=96,
                             blank=False,
                             primary_key=False,
                             help_text="This represents the title presentation name.",
                             verbose_name="Title name",
                             )
    episode_number = models.IntegerField(blank=False,
                                         primary_key=False,
                                         help_text="This represents the episode number.",
                                         verbose_name="Episode number",
                                         )
    released = models.CharField(max_length=10,
                                blank=False,
                                primary_key=False,
                                help_text="This represents the title launch date.",
                                verbose_name="Launch date",
                                )
    runtime = models.IntegerField(blank=False,
                                  primary_key=False,
                                  help_text="This represents the episode runtime.",
                                  verbose_name="Runtime",
                                  )
    plot = models.CharField(max_length=256,
                            blank=False,
                            primary_key=False,
                            help_text="This represents the episode plot.",
                            verbose_name="Plot",
                            )
    poster = models.URLField(blank=False,
                             primary_key=False,
                             help_text="This represents the episode image URL.",
                             verbose_name="Poster URL",
                             )
    imdb_rating = models.FloatField(blank=False,
                                    primary_key=False,
                                    help_text="This represents the episode rating.",
                                    verbose_name="Rating",
                                    )
    episodes = models.ForeignKey(Season,
                                 on_delete=models.CASCADE,
                                 related_name="episodes",
                                 help_text="This represents the episode owner season.",
                                 verbose_name="Episode owner",
                                 )

    def __str__(self):
        return self.title
