from django.contrib import admin
from .models.sample import Sample


class Samples(admin.ModelAdmin):  # Adding model on admin console
    # Choosing what fields will be displayed on admin
    list_display = ("id", "name")


admin.site.register(Sample, Samples)  # Registering model on admin console
