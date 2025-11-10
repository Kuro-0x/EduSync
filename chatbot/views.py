from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, os, requests
from .ai_prompt import build_ai_prompt
from .responses import DEFAULT_RESPONSE, HELP_OVERVIEW

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SYSTEM_PROMPT = build_ai_prompt()

@csrf_exempt
def chatbot_response(request):
    if request.method == "GET":
        # Show help overview on first load
        if not request.session.get("chatbot_started", False):
            request.session["chatbot_started"] = True
            return JsonResponse({"response": HELP_OVERVIEW})
        return JsonResponse({"response": "Hi again! Type 'help' if you need guidance."})

    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message", "").strip()

        ai_response = get_ai_response(user_input)
        return JsonResponse({"response": ai_response})

    return JsonResponse({"error": "Invalid request"}, status=400)


def get_ai_response(user_input):
    """
    Call OpenRouter AI to generate a response.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "X-Title": "EduSync Chatbot"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("AI Error:", e)
        return DEFAULT_RESPONSE
