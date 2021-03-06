from itsdangerous import URLSafeTimedSerializer
import os


SECRET_KEY = os.environ['MALGAZER_WEB_SECRET_KEY']
SECURITY_PASSWORD_SALT = os.environ['MALGAZER_WEB_SECURITY_PASSWORD_SALT']


def generate_confirmation_token(email):
    """
    Generates a confirmation token for an email address.

    :param email:  The email to embed in the token.
    :return: The token.
    """
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    """
    This determines if the token is valid.

    :param token:  The token.
    :param expiration: The expiration, in seconds.
    :return: False if there is an issue, the email for the token if it is confirmed.
    """
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(token, salt=SECURITY_PASSWORD_SALT, max_age=expiration)
    except:
        return False
    return email
