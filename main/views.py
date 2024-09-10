from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Sarah Saphira Setiawan',
        'npm' : '2306240093',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)