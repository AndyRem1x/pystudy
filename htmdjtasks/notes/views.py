from django.shortcuts import render


def notes_view(request):
    notes = ["Note 1", "Note 2", "Note 3"]
    return render(request, 'index.html', {'notes': notes})
