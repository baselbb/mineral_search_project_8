import random
import pickle


from django.shortcuts import render
from django.db.models import Q


from minerals.models import Mineral

m = Mineral.objects.all()
random_mineral = random.choice(m)


def index(request):
    """Landing 'home' page view to display list of all mineral names"""
    minerals = m
    return render(request, 'index.html', {'minerals': minerals, 'random_mineral': random_mineral})


# Lists minerals for a selected letter search
def mineral_letter(request, letter):
    minerals = m.filter(name__istartswith=letter.lower())
    return render(request, 'index.html', {'minerals': minerals,
                                          'active_letter': letter,
                                          'random_mineral': random_mineral})


# Text Search minerals by name and other mineral categories
def mineral_search(request):
    term = request.GET.get("q")
    minerals = m.filter(
        Q(name__icontains=term) |
        Q(group__icontains=term) |
        Q(image_caption=term)
    )

    return render(request, 'index.html', {'minerals': minerals,
                                          'random_mineral': random_mineral})


# Search by mineral group
def mineral_group(request, group):
    minerals = m.filter(group__icontains=group)
    return render(request, 'index.html', {'minerals': minerals,
                                          'random_mineral': random_mineral})


# Search by mineral color
def mineral_color(request, color):
    minerals = m.filter(color__icontains=color)
    return render(request, 'index.html', {'minerals': minerals,
                                          'random_mineral': random_mineral})


