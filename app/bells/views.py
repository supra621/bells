from django.shortcuts import render


def test_view(request):
    context = {}
    return render(request, 'home.html', context)
