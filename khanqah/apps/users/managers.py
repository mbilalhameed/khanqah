from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):

        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('You must provide a valid email address'))

    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        print(username, first_name, last_name, email, password)

        if not username:
            raise ValueError(_("User must submit a username"))
        if not first_name:
            raise ValueError(_("User must submit a First Name"))
        if not last_name:
            raise ValueError(_("User must submit a Last Name"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)

        else:
            raise ValueError(_("Base User Account: An Email is required "))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):

        if not password:
            raise ValueError(_("Superusers must have a password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin Account: An email address is required"))

        user = self.create_user(
            username=username, email=email,
            password=password, first_name=first_name,
            last_name=last_name, **extra_fields
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)

        return user
