from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response  # Assuming this function handles chatbot responses

app = Flask(__name__)
CORS(app)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Chatbot page route
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')  # New page for chatbot interface

# Registration page route
@app.route('/registration')
def registration():
    return render_template('registration.html')

# Login page route
@app.route('/login')
def login():
    return render_template('login.html')

# Settings page route
@app.route('/settings')
def settings():
    return render_template('settings.html')

# Contact Us page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Admin page route
@app.route('/admin')
def admin():
    return render_template('admin.html')

# About Us page route
@app.route('/about')
def about_us():
    return render_template('about_us.html')

# Profile Update page route
@app.route('/profile-update')
def profile_update():
    return render_template('profile-update.html')

# Password Reset page route
@app.route('/password-reset')
def password_reset():
    return render_template('password-reset.html')

# Deactivate Account page route
@app.route('/deactivate-account')
def deactivate_account():
    return render_template('deactivate-account.html')

# Health Monitoring Settings page route
@app.route('/health-monitoring')
def health_monitoring():
    return render_template('health-monitoring.html')

# Chat prediction route (POST request)
@app.route('/predict', methods=['POST'])
def predict():
    # Get the message from the user input
    text = request.get_json().get("message")
    
    # Check if the message is valid
    if not text:
        return jsonify({"error": "No message provided"}), 400
    
    # Get the response from the chatbot function (get_response)
    response = get_response(text)
    
    # Send the response back to the frontend
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
