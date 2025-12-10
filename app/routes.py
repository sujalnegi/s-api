from flask import Blueprint, render_template, session, redirect, url_for, request
from functools import wraps
import markdown

routes = Blueprint("routes", __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "uid" not in session:
            return redirect(url_for("routes.login"))
        return f(*args, **kwargs)
    return decorated_function

@routes.route("/")
def home():
    return redirect(url_for("routes.dashboard"))

@routes.route("/login")
def login():
    return render_template("login.html")

@routes.route("/register")
def register():
    return render_template("register.html")

@routes.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@routes.route("/writer", methods=["GET", "POST"])
@login_required
def writer():
    generated_content = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            try:
                import google.generativeai as genai
                from flask import current_app
                
                api_key = current_app.config.get("GEMINI_API_KEY")
                print(f"DEBUG: API Key present: {bool(api_key)}")
                
                if not api_key:
                    generated_content = "Error: GEMINI_API_KEY not found in configuration."
                else:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.5-flash-lite')
                    response = model.generate_content(prompt)
                    generated_content = markdown.markdown(response.text)
            except Exception as e:
                generated_content = f"Error: {str(e)}"
                
    return render_template("writer.html", generated_content=generated_content)

@routes.route("/summarizer", methods=["GET", "POST"])
@login_required
def summarizer():
    generated_summary = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            try:
                import google.generativeai as genai
                from flask import current_app
                
                api_key = current_app.config.get("GEMINI_API_KEY")
                
                if not api_key:
                    generated_summary = "Error: GEMINI_API_KEY not found in configuration."
                else:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.5-flash-lite')
                    
                    word_count = len(text.split())
                    if word_count < 500:
                        constraint = "Provide 5 or fewer bullet points."
                    elif word_count < 1000:
                        constraint = "Provide between 6 and 10 bullet points."
                    else:
                        constraint = "Provide between 10 and 15 bullet points."
                        
                    prompt = f"Summarize the following text in precise bullet points. {constraint}\n\n{text}"
                    response = model.generate_content(prompt)
                    generated_summary = markdown.markdown(response.text)
            except Exception as e:
                generated_summary = f"Error: {str(e)}"
                
    return render_template("summarizer.html", generated_summary=generated_summary)

@routes.route("/code-explain", methods=["GET", "POST"])
@login_required
def code_explain():
    explanation = None
    if request.method == "POST":
        code = request.form.get("code")
        if code:
            try:
                import google.generativeai as genai
                from flask import current_app
                
                api_key = current_app.config.get("GEMINI_API_KEY")
                
                if not api_key:
                    explanation = "Error: GEMINI_API_KEY not found in configuration."
                else:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.5-flash-lite')
                    prompt = f"Explain the following code snippet in simple terms:\n\n{code}"
                    response = model.generate_content(prompt)
                    explanation = markdown.markdown(response.text, extensions=['fenced_code', 'codehilite'])
            except Exception as e:
                explanation = f"Error: {str(e)}"
                
    return render_template("code_explain.html", explanation=explanation)

@routes.route("/grammar", methods=["GET", "POST"])
@login_required
def grammar():
    corrected_text = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            try:
                import google.generativeai as genai
                from flask import current_app
                
                api_key = current_app.config.get("GEMINI_API_KEY")
                
                if not api_key:
                    corrected_text = "Error: GEMINI_API_KEY not found in configuration."
                else:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.5-flash-lite')
                    prompt = f"Correct the grammar and improve the style of the following text:\n\n{text}"
                    response = model.generate_content(prompt)
                    corrected_text = markdown.markdown(response.text)
            except Exception as e:
                corrected_text = f"Error: {str(e)}"
                
    return render_template("grammar.html", corrected_text=corrected_text)

@routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("routes.login"))
