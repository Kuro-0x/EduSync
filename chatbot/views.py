import os, json, requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai_prompt import build_ai_prompt
from .responses import DEFAULT_RESPONSE, HELP_OVERVIEW

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
SYSTEM_PROMPT = build_ai_prompt()


@csrf_exempt
def chatbot_response(request):
    """
    GET  → return welcome message
    POST → process message and return AI response
    """

    # Initialize chat history in session if missing
    if "chat_history" not in request.session:
        request.session["chat_history"] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    if request.method == "GET":
        welcome_msg = HELP_OVERVIEW
        request.session["chat_history"].append(
            {"role": "assistant", "content": welcome_msg}
        )
        request.session.save()
        return JsonResponse({"response": welcome_msg})

    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message", "").strip()

        if not user_input:
            return JsonResponse({"response": DEFAULT_RESPONSE})

        # Add user message to history
        history = request.session["chat_history"]
        history.append({"role": "user", "content": user_input})

        # Get AI response
        ai_msg = get_ai_response(history)

        # Append AI message to chat history
        history.append({"role": "assistant", "content": ai_msg})
        request.session["chat_history"] = history
        request.session.save()

        return JsonResponse({"response": ai_msg})

    return JsonResponse({"error": "Invalid request"}, status=400)


def get_ai_response(chat_history):
    """Send the entire chat history to OpenRouter"""

    if not OPENROUTER_API_KEY:
        print("Missing OpenRouter API key.")
        return DEFAULT_RESPONSE

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "X-Title": "EduSync Chatbot"
    }

    payload = {
        "model": "openai/gpt-oss-20b:free",  
        "messages": chat_history,
        "temperature": 0.7,
    }

    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=15)

        print("Status:", resp.status_code)
        print("Raw:", resp.text[:300])

        data = resp.json()
        msg = data.get("choices", [{}])[0].get("message", {}).get("content")
        return msg.strip() if msg else DEFAULT_RESPONSE

    except Exception as e:
        print("AI Error:", e)
        return DEFAULT_RESPONSE
