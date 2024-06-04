from django.shortcuts import render


def show_start_page(request):
    return render(request, 'template.html')
