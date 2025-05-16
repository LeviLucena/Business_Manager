from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import ask_deepseek
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

@login_required
def chat_view(request):
    resposta = None
    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()
        if user_message:
            resposta = ask_deepseek(user_message, os.getenv("DEEPSEEK_API_KEY"))
    return render(request, 'chat/chat.html', {
        'resposta': resposta,
        'now': datetime.now()
    })
