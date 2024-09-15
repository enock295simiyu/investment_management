import logging

from django.db import models
from model_utils.models import UUIDModel, TimeStampedModel

from investment.middleware import get_current_user

log = logging.getLogger(__name__)


# Create your models here.
class BaseModel(UUIDModel, TimeStampedModel):
    """
    Shared logic
    """
    created_by = models.CharField(max_length=64, db_index=True, null=True, blank=True, editable=False)
    modified_by = models.CharField(max_length=64, db_index=True, null=True, blank=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        current_user = get_current_user()

        if current_user:
            username = current_user.username
            if not self.created_by:
                self.created_by = username
            else:
                self.modified_by = username
        super(BaseModel, self).save(*args, **kwargs)
