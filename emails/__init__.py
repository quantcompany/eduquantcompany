from threading import Thread

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


# def send_mail_wrapper(*args, **kwargs):
#     try:
#         send_mail(**kwargs)
#     except Exception as ex:
#         print('Error sending email:')
#         print(ex)


def send(subject, message, recipients, html, async=True):
    kwargs = {
        'subject': subject,
        'message': message,
        'from_email': None,
        'recipient_list': recipients,
        'fail_silently': True,
        'html_message': html
    }

    if async:
        t = Thread(target=send_mail, kwargs=kwargs)
        t.daemon = True
        t.start()
        return 1
    else:
        return send_mail(**kwargs)

def send_verification_email(verification, site):
    subject = 'Verification Email'
    message = ''
    html = render_to_string('emails/verification.html', {'verification': verification, 'site': site})
    recipients = [verification.user.email]
    return send(subject, message, recipients, html)


def send_contact_email(data, site):
    subject = 'Contact Form "{0}"'.format(data['name'])
    message = 'A user has submitted a contact form.'
    html = render_to_string('emails/contact.html', {'data': data})
    recipients = [settings.DEFAULT_FROM_EMAIL]
    return send(subject, message, recipients, html)

# def send_report_email(patient, report_type, addresses, site):
#     assert report_type in ['medical', 'patient'], 'Invalid report type'
#
#     subject = 'Trippletherapy {0} Report'.format(report_type.capitalize())
#     message = ''
#     html = render_to_string('report_emails/{0}.html'.format(report_type), {'site': site, 'patient': patient})
#     recipients = addresses
#     return send(subject, message, recipients, html)
