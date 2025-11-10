from .responses import RESPONSES, HELP_OVERVIEW, DEFAULT_RESPONSE

def build_ai_prompt():
    """
    Convert your static responses into a system message for AI.
    """
    prompt = "You are EduSync Chatbot 🤖. Answer user questions in the same style as below.\n\n"
    
    prompt += f"HELP_OVERVIEW:\n{HELP_OVERVIEW}\n\n"
    
    prompt += "Known keywords and responses:\n"
    for k, v in RESPONSES.items():
        prompt += f"- '{k}': '{v}'\n"
    
    prompt += f"\nIf user asks something not listed above, answer helpfully, concisely, and in the same friendly tone. "\
              f"If unsure, reply like the default response: '{DEFAULT_RESPONSE}'\n"
    
    return prompt
