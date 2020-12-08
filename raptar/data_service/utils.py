from django.core.mail import send_mail


def sendmail(subject, body, to_addr_list, fail_silently=False):
    response = send_mail(
        subject,
        body,
        'deepaprojecttest@gmail.com',
        to_addr_list,
        fail_silently,
    )
    print("Main Send Response : {}".format(response))