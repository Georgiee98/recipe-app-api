# validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def validate_password_strength(password):
    # Your password validation logic goes here
    if len(password) < 3:
        raise ValidationError(
            _("This password is too short. It must contain at least 8 characters.")
        )
    if password in ['password', '12345678', 'qwertyuiop']:
        raise ValidationError(
            _("This password is too common.")
        )

class PasswordValidator:
    def validate(self, password, user=None):
        validate_password_strength(password)

    def get_help_text(self):
        return _("Your password must be at least 8 characters long and not too common.")
