from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
from fuzzywuzzy import fuzz
from sentence_transformers import SentenceTransformer, util
import torch
from .responses import RESPONSES, DEFAULT_RESPONSE, HELP_OVERVIEW

# Load semantic model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Precompute embeddings for all response keywords
keyword_embeddings = {k: model.encode(k, convert_to_tensor=True) for k in RESPONSES.keys()}

@csrf_exempt
def chatbot_response(request):
    if request.method == "GET":
        # Show help message on first load
        if not request.session.get("chatbot_started", False):
            request.session["chatbot_started"] = True
            return JsonResponse({"response": HELP_OVERVIEW})
        return JsonResponse({"response": "Hi again! Type 'help' if you need guidance."})

    if request.method == "POST":
        data = json.loads(request.body)
        user_input = data.get("message", "").lower().strip()

        # ---- 1️⃣ Try exact keyword match ----
        for keyword, response in RESPONSES.items():
            if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
                return JsonResponse({"response": response})

        # ---- 2️⃣ Try fuzzy match ----
        fuzzy_matches = [
            (keyword, fuzz.partial_ratio(user_input, keyword))
            for keyword in RESPONSES.keys()
        ]
        best_keyword, best_score = max(fuzzy_matches, key=lambda x: x[1])

        if best_score > 80:  # Threshold for fuzzy similarity
            return JsonResponse({"response": RESPONSES[best_keyword]})

        # ---- 3️⃣ Try semantic similarity ----
        user_embedding = model.encode(user_input, convert_to_tensor=True)
        similarities = {
            k: util.pytorch_cos_sim(user_embedding, emb).item()
            for k, emb in keyword_embeddings.items()
        }
        best_semantic_keyword, best_semantic_score = max(similarities.items(), key=lambda x: x[1])

        if best_semantic_score > 0.55:  # Semantic confidence threshold
            return JsonResponse({"response": RESPONSES[best_semantic_keyword]})

        # ---- 4️⃣ Default fallback ----
        return JsonResponse({"response": DEFAULT_RESPONSE})

    return JsonResponse({"error": "Invalid request"}, status=400)
