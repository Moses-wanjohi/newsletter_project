from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SubscriberForm


def subscribe(request):
  success_message = None

  if request.method == 'POST':
    form = SubscriberForm(request.POST)
    if form.is_valid():
      subscriber = form.save()

      # Send confirmation email
      subject = 'Welcome to Our Newsletter!'
      message = (
          'Hi,\n\nThank you for subscribing to our newsletter! We are excited'
          ' to share our latest updates with you.\n\nBest regards,\nThe Team'
      )
      email_from = settings.DEFAULT_FROM_EMAIL
      recipient_list = [subscriber.email]

      try:
        send_mail(subject, message, email_from, recipient_list)
        success_message = (
            'Thank you for subscribing! A confirmation email has been sent.'
        )
      except Exception:
        success_message = (
            'Subscribed successfully, but confirmation email delivery failed.'
        )

      form = SubscriberForm()  
  else:
    form = SubscriberForm()

  return render(
      request,
      'subscribe.html',
      {'form': form, 'success_message': success_message},
  )