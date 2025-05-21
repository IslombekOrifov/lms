from django.shortcuts import render


def dashboard(request):
    """
    Render the dashboard page.
    """
    return render(request, 'main/index.html')