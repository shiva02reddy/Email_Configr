from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    if request.method == "POST":

        name = request.POST.get('name')
        mail = request.POST.get('mail')
        desc = request.POST.get('desc')

        print("Name:", name)
        print("Recipient:", mail)
        print("Description:", desc)

        if not mail:
            return HttpResponse("Recipient email is missing!")

        result = send_mail(
            'Complaint Received',
            f'''
            Hello {name},

            Your complaint has been received.

            Complaint Details:
            {desc}

            Regards,
            Help Team
            ''',
            settings.EMAIL_HOST_USER,
            [mail],
            fail_silently=False
        )

        print("Email status:", result)

        return HttpResponse("Email sent successfully!")

    return render(request, 'index.html')