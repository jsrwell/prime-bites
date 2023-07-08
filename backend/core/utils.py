from django.utils.text import slugify


def get_first_name_from_email(email):
    """Get the first name from the first part of the e-mail."""
    email_parts = email.split("@")
    name = email_parts[0]
    name = slugify(name)
    return name.split("-")[0]
