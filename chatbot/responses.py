HELP_OVERVIEW = (
    "👋 Welcome to EduSync Chatbot!\n\n"
    "Here’s what I can help you with:\n\n"
    "- Account access: login, signup, email verification, reset password\n"
    "- Course creation: create course, module, lesson, quiz, add question\n"
    "- Taking quizzes and earning certificates\n"
    "- Browsing and enrolling in courses\n"
    "- Privacy, data, and terms of service\n"
    "- Contacting support\n\n"
    "If you're not sure where to start, try typing 'help' to see what I can do!"
)

RESPONSES = {
    # Greetings
    "hello": "👋 Hi there! How can I help you today?",
    "hi": "Hello! Ready to learn something new? 😊",
    "hey": "Hey there! How’s it going?",
    "yo": "Yo! What’s up?",
    "sup": "Hey! All good? How can I help?",
    "good morning": "☀️ Good morning! Ready to learn something new?",
    "good afternoon": "🌞 Good afternoon! How can I assist?",
    "good evening": "🌙 Good evening! What brings you here?",
    "bye": "Goodbye! Have a wonderful day 🎉",
    "see ya": "👋 See you next time!",
    "later": "Catch you later! 👋",

    # Help overview
    "help": (
        "I can guide you with things like:\n\n"
        "📌 'Account' → login, signup, login failed, email verification, reset password\n"
        "📌 'Courses' → create course, add module/lesson/quiz/question\n"
        "📌 'Learning' → take quiz, certificate\n"
        "📌 'Info' → privacy, terms, support\n\n"
        "Just type what you're curious about, and I’ll help!"
    ),
    "what can you do": "Here’s a quick guide:\n\n" + HELP_OVERVIEW,
    "how to use": "Here's what I can do:\n\n" + HELP_OVERVIEW,
    "what is this": "I’m EduSync Chatbot 🤖 — I can help you with your account, courses, and quizzes!",

    # Login & signup
    "login": (
        "To log in, click the 'Login' button at the top right and enter your email + password. "
        "If you don’t have an account yet, sign up first. 👍"
    ),
    "log in": "Same as 'login' — click the 'Login' button and enter your details. 👍",
    "sign in": "You can sign in from the 'Login' button on the top right corner.",
    "signup": (
        "To sign up, click 'Login' (top right), then choose 'Create an account'. "
        "You'll get a verification email to confirm your account."
    ),
    "sign up": (
        "To sign up, click 'Login' (top right), then choose 'Create an account'. "
        "You'll get a verification email to confirm your account."
    ),
    "create account": (
        "To create a new account, go to the top right corner → click 'Login' → select 'Create an account'."
    ),
    "register": (
        "To register, go to the Login page and choose 'Create an account'. Verify your email after signing up."
    ),
    "join": "You can join by creating an account — click 'Login' → 'Create an account'.",

    "email verification": (
        "After signing up, we’ll send a verification link to your email (valid for 10 minutes). "
        "If it expires, just log in again to automatically receive a new one."
    ),
    "verify email": (
        "Check your inbox for a verification link (valid 10 minutes). If expired, log in again to resend it."
    ),
    "login failed": (
        "😕 Having trouble logging in? Double-check your email and password. "
        "If your account isn’t verified, logging in will resend the verification email. "
        "Still stuck? Contact support at 'kmh61030@gmail.com'."
    ),
    "can't login": "If you can’t log in, check your credentials or verification email. You can contact support if needed.",
    "reset password": (
        "Forgot your password? No worries! Email 'kmh61030@gmail.com', "
        "and our admin will help you reset it."
    ),
    "forgot password": "You can reset your password by emailing 'kmh61030@gmail.com'.",
    "change password": "To change or reset your password, email 'kmh61030@gmail.com'.",

    # Courses
    "create course": (
        "To create a course, head to your 'Dashboard' and click 'Create New Course'. 🚀"
    ),
    "make course": "You can make a course by going to your Dashboard → 'Create New Course'.",
    "add course": "To add a new course, go to Dashboard → 'Create New Course'.",
    "build course": "From Dashboard → click 'Create New Course' to start building.",
    "start course": "You can start by creating a new course from the Dashboard.",

    "add module": (
        "Modules organize your course. From your dashboard, select a course and click 'Add Module'."
    ),
    "create module": "To create a module, open your course → click 'Add Module'.",
    "add lesson": (
        "Lessons go inside modules. Open your course → pick a module → click 'Add Lesson'."
    ),
    "create lesson": "To create a lesson, go to a module and click 'Add Lesson'.",
    "add quiz": (
        "To add a quiz, open your course → go to the module/lesson → click 'Add Quiz'."
    ),
    "create quiz": "Go to your module or lesson → click 'Add Quiz'.",
    "add question": (
        "When you create a quiz, you'll be prompted to add questions. "
        "To add more later, go to 'View Quiz' → 'Add Question'."
    ),
    "create question": "To add questions, open your quiz → click 'Add Question'.",
    "take quiz": (
        "To take a quiz, navigate to the quiz section of your course and click 'Take Quiz'."
    ),
    "start quiz": "Go to the quiz section of your course → click 'Take Quiz' to begin.",

    # Certificates
    "certificate": (
        "🏅 To earn a certificate: complete all lessons and mark them as finished. "
        "Once done, your certificate will be available for download at the bottom of the course page."
    ),
    "get certificate": "Complete all lessons to unlock your certificate. 🏅",
    "download certificate": "Once all lessons are complete, download your certificate from the course page.",

    # Info & support
    "privacy": "🔒 We value your privacy. Check the 'Privacy Policy' link in the footer.",
    "terms": "📜 You can review our 'Terms of Service' anytime from the footer.",
    "support": "💌 Need help? Email us at 'kmh61030@gmail.com', and we’ll assist you.",
    "contact": "You can contact us at 'kmh61030@gmail.com' for support.",
    "help me": "Sure! Here’s what I can help with:\n\n" + HELP_OVERVIEW,
    "issue": "If you’re having trouble, contact support at 'kmh61030@gmail.com'.",
    "problem": "Sorry to hear that! You can email 'kmh61030@gmail.com' for help.",
}

DEFAULT_RESPONSE = (
    "🤔 Sorry, I’m not sure about that. Try typing 'help' to see what I can do!"
)
