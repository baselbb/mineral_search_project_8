from django.shortcuts import get_object_or_404, render
from .models import Mineral
import random


# Details view for each mineral, pk is the primary key
def mineral_detail(request, pk):
    """Mineral 'detail' view to display mineral details"""
    mineral = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    # create a random mineral variable to pass the template
    random_mineral = random.choice(minerals)

    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral,
                                                            'random_mineral': random_mineral})



