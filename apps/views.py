from django.shortcuts import render
from .models import Comment

def main_page(request):
    if request.method == 'post':
        name = request.POST.get("name")
        email = request.POST.get("email")
        website = request.POST.get("websayt")
        telegram = request.POST.get("telegram")
        message = request.POST.get("message")

        Comment.objects.create(name=name, email=email, text=message, status=website if website else telegram)

    return render(request, 'index.html')