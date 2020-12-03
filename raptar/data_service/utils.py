from django.core.mail import send_mail


def sendmail(subject, body, from_addr, to_addr_list, fail_silently=False):
    response = send_mail(
        subject,
        body,
        from_addr,
        to_addr_list,
        fail_silently,
    )
    print("Main Send Reposne : {}".format(response))