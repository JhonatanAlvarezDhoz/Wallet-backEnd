from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime
from django.conf import settings


def send_email(user, business, receiver="isaacxzx@gmail.com"):
    msg_plain = render_to_string(
        'email.txt', {'some_params': ""})
    msg_html = render_to_string(
        'email.html', {
            "user": user,
            "business": business.first,
            "time": datetime.now(),
        })

    send_mail(
        'email title',
        msg_plain,
        settings.EMAIL_HOST_USER,
        [receiver],
        html_message=msg_html,
    )


def send_email_to_recovery_password(user, token):
    msg_plain = render_to_string(
        'email.txt', {'some_params': ""})
    msg_html = render_to_string(
        'token_email.html', {
            "user": user,
            "token": token,
        })

    try:
        send_mail(
            'code to recovery password',
            msg_plain,
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=msg_html,
        )
    except Exception as e:
        print(e)