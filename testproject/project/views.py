from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def sendmail(request):
	subject = "Example subject"
	from_email = settings.EMAIL_HOST_USER
	subject = 'Example subject'
	from_email = settings.EMAIL_HOST_USER
	to_email = ['from_email', 'otheremail']

	message = "%s" % ("Messages")

	send_mail(subject,
			from_email,
			to_email,
			fail_silently=False)