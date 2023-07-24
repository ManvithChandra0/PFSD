from django.shortcuts import render, redirect
from .forms import BioDataForm

def add_bio_data(request):
    if request.method == 'POST':
        form = BioDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html',)
    else:
        form = BioDataForm()
    return render(request, 'biodata.html', {'form': form})