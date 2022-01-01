from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm


# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    context = {
        'meetups': meetups,
    }
    return render(request, "meetups/index.html", context)


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == "GET":
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        context = {
            'selected_meetup': selected_meetup,
            'meetup_found': True,
            'form': registration_form,
        }
        return render(request, 'meetups/meetup-details.html', context)
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {'meetup_found': False})


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    context = {
        'meetup' : meetup,
    }
    return render(request, 'meetups/registration-success.html', context)
