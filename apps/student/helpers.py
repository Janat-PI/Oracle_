from django.core.mail import send_mail


def send_message_for_student(from_email: str, message: str, to_email: str):

    send_mail(
        'Это со ШКОЛЫ тебе ПИС...',
        message,
        from_email,
        [to_email]
        )



def post_send_email_for_student(sender, created: bool, instance, *args, **kwargs):

    if created:
        send_message_for_student(
            "test@gmail.com",
            "привет тебя зарегали на сайте",
            instance.email
        )