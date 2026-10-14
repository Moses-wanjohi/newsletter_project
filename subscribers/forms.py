from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):

  class Meta:
    model = Subscriber
    fields = ['email']
    widgets = {
        'email': forms.EmailInput(
            attrs={
                'class': (
                    'w-full px-4 py-2 border rounded-lg focus:outline-none'
                    ' focus:ring-2 focus:ring-blue-500'
                ),
                'placeholder': 'Enter your email address',
            }
        )
    }

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if Subscriber.objects.filter(email=email).exists():
      raise forms.ValidationError(
          'This email address is already subscribed to the newsletter.'
      )
    return email