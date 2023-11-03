from django.core.exceptions import ValidationError
import os


def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensins = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensins:
        raise ValidationError('Unssuported file extension. Allowed only: ' + str(valid_extensins))

