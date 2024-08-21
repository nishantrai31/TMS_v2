from django.db import models
class BaseModel(models.Model):
    """
    Data model to save common data used in models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    """data created date and time."""

    modified_at = models.DateTimeField(auto_now=True)
    """data update date and time."""

    class Meta:
        abstract = True