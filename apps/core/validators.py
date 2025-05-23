import os
from django.core.exceptions import ValidationError


def validate_file_extension_image(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [".jpg", ".jpeg", ".png", ".svg"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")
