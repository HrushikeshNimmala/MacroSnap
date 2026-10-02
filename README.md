# 🥗 MacroSnap — AI Nutrition Buddy

MacroSnap is an AI-powered nutrition assistant that helps users understand what they are eating through **text descriptions and meal photos**.

It uses **Google Gemini AI** to identify foods and provide approximate calorie and macronutrient estimates. Users can also generate a nutrition summary and send it to their email using **Gmail SMTP**.

---

## ✨ Features

* 📸 AI-powered meal photo analysis
* 💬 Natural-language food and nutrition conversations
* 🔥 Estimated calorie calculation
* 💪 Protein, carbohydrate and fat estimates
* 📝 Automatic nutrition summary generation
* 📧 Send nutrition summaries through Gmail
* 👤 Simple user onboarding
* 🔄 Start a new nutrition-tracking session
* 📱 Clean and responsive Streamlit interface
* 🔐 API credentials stored securely using Streamlit secrets

---

## 🧠 How It Works

```text
User
 │
 ├── Describes a meal
 │
 └── Uploads a meal photo
          │
          ▼
     MacroSnap
          │
          ▼
      Gemini AI
          │
          ▼
 Food Identification
          │
          ▼
 Calories + Macros
          │
          ▼
 Nutrition Summary
          │
          ▼
      Gmail SMTP
          │
          ▼
      User Email
```

---

## 🛠️ Technology Stack

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Python        | Application development             |
| Streamlit     | Web application interface           |
| Google Gemini | AI text and image analysis          |
| Gmail SMTP    | Email delivery                      |
| Twilio        | WhatsApp integration/testing        |
| Git & GitHub  | Version control and project hosting |

---

## 📂 Project Structure

```text
AI-Vision-ChatBot/
│
├── .streamlit/
│   ├── secrets.toml
│   └── secrets.toml.example
│
├── app.py
├── prompts.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd AI-Vision-ChatBot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

Create:

```text
.streamlit/secrets.toml
```

Add your private credentials:

```toml
GEMINI_API_KEY = "your-gemini-api-key"

TWILIO_ACCOUNT_SID = "your-twilio-account-sid"
TWILIO_AUTH_TOKEN = "your-twilio-auth-token"
TWILIO_WHATSAPP_FROM = "whatsapp:+your-twilio-number"
TWILIO_WHATSAPP_TO = "your-whatsapp-number"

GMAIL_SENDER = "your-gmail@gmail.com"
GMAIL_APP_PASSWORD = "your-gmail-app-password"
GMAIL_RECIPIENT = "recipient@gmail.com"
```

**Never commit your real `secrets.toml` file to GitHub.**

The repository includes:

```text
.streamlit/secrets.toml.example
```

as a safe configuration template.

---

## ▶️ Run the Application

Start MacroSnap with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📸 Using MacroSnap

### Step 1 — Start

Enter your name and WhatsApp number.

### Step 2 — Describe your meal

For example:

```text
I ate two rotis with chicken curry and a bowl of rice.
```

MacroSnap will provide an approximate nutrition estimate.

### Step 3 — Upload a meal photo

Upload a JPG, JPEG or PNG image of your meal.

Gemini analyzes the image and estimates:

* Food items
* Calories
* Protein
* Carbohydrates
* Fat

### Step 4 — Generate Summary

Click:

**📝 Generate Nutrition Summary**

MacroSnap creates a combined summary of the conversation.

### Step 5 — Email the Summary

Click:

**📧 Send Summary by Email**

The nutrition summary is delivered through Gmail SMTP.

---

## ⚠️ Nutrition Disclaimer

MacroSnap provides **AI-generated estimates**, not medically verified nutritional information.

Actual calories and macronutrients may vary depending on:

* Portion size
* Ingredients
* Cooking method
* Recipe
* Food preparation

MacroSnap should not be used as a substitute for professional medical or dietary advice.

---

## 🔐 Security

Private credentials should be stored in:

```text
.streamlit/secrets.toml
```

The file is excluded from Git using `.gitignore`.

Never expose:

* Gemini API keys
* Twilio Auth Tokens
* Gmail App Passwords
* Other private credentials

---

## 🚀 Future Improvements

Potential future enhancements include:

* 📊 Daily nutrition dashboard
* 📅 Meal history
* 🎯 Personalized calorie goals
* 📈 Weekly nutrition analytics
* 🥗 Personalized meal recommendations
* 👥 User accounts
* 📱 Improved mobile experience
* 💬 Production WhatsApp integration
* 🗄️ Database-backed meal history
* 🔔 Nutrition reminders

---

## 👨‍💻 Project

**MacroSnap — AI Nutrition Buddy**

Built using Python, Streamlit, Gemini AI and Gmail SMTP.

> Eat smarter. Track better. 🥗💪
