from django.db import models
from .title import Title
from .episode import Episode


class TitleRelease(models.Model):
    """
    A model for title release table
    """
    day = models.PositiveSmallIntegerField(blank=True,
                                           null=True,
                                           help_text="This represents the title release day.",
                                           verbose_name="Title release day",
                                           )
    month = models.PositiveSmallIntegerField(blank=True,
                                             null=True,
                                             help_text="This represents the title release month.",
                                             verbose_name="Title release month",
                                             )
    year = models.PositiveSmallIntegerField(blank=True,
                                            null=True,
                                            primary_key=False,
                                            help_text="This represents the title release year.",
                                            verbose_name="Title release year",
                                            )
    release_owner_title = models.ForeignKey(Title,
                                            on_delete=models.CASCADE,
                                            related_name="released",
                                            help_text="This represents the release owner title.",
                                            verbose_name="Release owner title",
                                            )

    def __str__(self):
        return str(self.release_owner_title)


class EpisodeRelease(models.Model):
    """
    A model for episode release table
    """
    day = models.PositiveSmallIntegerField(blank=True,
                                           null=True,
                                           primary_key=False,
                                           help_text="This represents the episode release day.",
                                           verbose_name="Episode release day",
                                           )
    month = models.PositiveSmallIntegerField(blank=True,
                                             null=True,
                                             primary_key=False,
                                             help_text="This represents the episode release month.",
                                             verbose_name="Episode release month",
                                             )
    year = models.PositiveSmallIntegerField(blank=True,
                                            null=True,
                                            primary_key=False,
                                            help_text="This represents the episode release year.",
                                            verbose_name="Episode release year",
                                            )
    release_owner_episode = models.ForeignKey(Episode,
                                              on_delete=models.CASCADE,
                                              related_name="released",
                                              help_text="This represents the release owner episode.",
                                              verbose_name="Release owner episode",
                                              )

    def __str__(self):
        return str(self.release_owner_episode)
