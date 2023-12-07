from django.shortcuts import render


def test_app_view(request):
    context = {}
    return render(request, 'core/home.html', context)
