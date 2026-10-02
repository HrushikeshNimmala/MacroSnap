# 🥗 MacroSnap — AI Nutrition Assistant

> **An AI-powered nutrition assistant that analyzes meal descriptions and food images to estimate calories and macronutrients.**

MacroSnap is a **multimodal AI nutrition assistant** built with **Python, Streamlit, and Google Gemini**. Users can describe what they ate or upload a photo of their meal, and MacroSnap analyzes it to provide estimated **calories, protein, carbohydrates, and fat**.

The application also generates a combined nutrition summary for the current session and can send the summary to a configured email address using **Gmail SMTP**.

---

## 🚀 Live Demo

### 👉 [Try MacroSnap Live](https://macrosnap-zee6qx85svjs9sny9yrvat.streamlit.app/)

### 💻 [View Source Code on GitHub](https://github.com/HrushikeshNimmala/MacroSnap)

---

## 📸 What MacroSnap Does

MacroSnap provides a simple workflow:

```text
Enter Your Name
       ↓
Describe Your Meal / Upload Meal Image
       ↓
Google Gemini AI Analysis
       ↓
Food Identification
       ↓
Calories + Protein + Carbs + Fat
       ↓
Discuss More Meals
       ↓
Generate Nutrition Summary
       ↓
Send Summary via Email
```

---

## ✨ Key Features

### 🥗 Multimodal Meal Analysis

Users can analyze meals in two ways:

* 📝 **Text input** — Describe the food you ate.
* 📷 **Image input** — Upload a photo of your meal.

Gemini analyzes the available information and produces an approximate nutrition breakdown.

### 🔥 Calorie Estimation

MacroSnap estimates the calories contained in the meal based on the detected food items and their apparent portions.

### 💪 Macronutrient Estimation

The application estimates:

* Protein
* Carbohydrates
* Fat

### 📊 Session Nutrition Summary

MacroSnap can summarize the meals discussed during the current conversation and provide combined calorie and macro estimates.

### 📧 Email Delivery

Users can send their generated nutrition summary to a configured email address using **Gmail SMTP**.

### 💬 Conversational AI

MacroSnap maintains the current conversation context so users can discuss multiple meals within the same session.

### 🎨 Clean User Interface

The application provides:

* Personalized welcome message
* Simple onboarding
* Chat-based interaction
* Meal image upload
* Nutrition summary section
* Email delivery
* Nutrition disclaimer
* New-session option

---

## 🧠 AI Capabilities

MacroSnap uses **Google Gemini** for multimodal AI processing.

The model is used for:

```text
Text Understanding
       +
Image Understanding
       ↓
Food Identification
       ↓
Nutrition Estimation
       ↓
Conversational Response
       ↓
Nutrition Summary
```

The application does not train a custom machine-learning model. Instead, it uses a generative AI model through the Gemini API.

---

## 🛠️ Tech Stack

| Technology                    | Purpose                                           |
| ----------------------------- | ------------------------------------------------- |
| **Python**                    | Core application development                      |
| **Streamlit**                 | Web application and UI                            |
| **Google Gemini**             | Multimodal AI analysis                            |
| **Google GenAI SDK**          | Gemini API integration                            |
| **Gmail SMTP**                | Nutrition summary email delivery                  |
| **Twilio**                    | WhatsApp configuration / future messaging support |
| **Git**                       | Version control                                   |
| **GitHub**                    | Source code hosting                               |
| **Streamlit Community Cloud** | Cloud deployment                                  |

---

## 📁 Project Structure

```text
MacroSnap/
│
├── .streamlit/
│   └── secrets.toml.example
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── venv/
```

### Main Files

#### `app.py`

Contains the main Streamlit application including:

* User onboarding
* Gemini client
* Chat interface
* Text meal analysis
* Image meal analysis
* Nutrition summary
* Gmail SMTP integration
* Session management
* UI styling

#### `prompts.py`

Contains the AI prompts used to control MacroSnap's behavior:

* `SYSTEM_PROMPT`
* `WELCOME_MESSAGE_TEMPLATE`
* `SUMMARY_REQUEST_PROMPT`

#### `requirements.txt`

Contains the Python dependencies required to run the application.

#### `.streamlit/secrets.toml.example`

Provides an example structure for configuring API keys and credentials without exposing real secrets.

---

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/HrushikeshNimmala/MacroSnap.git
```

### 2. Open the project

```bash
cd MacroSnap
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script:

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

### 6. Configure secrets

Create:

```text
.streamlit/secrets.toml
```

Do **not** upload this file to GitHub.

Example structure:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_WHATSAPP_FROM = "YOUR_TWILIO_WHATSAPP_FROM"
TWILIO_WHATSAPP_TO = "YOUR_TWILIO_WHATSAPP_TO"

GMAIL_SENDER = "YOUR_GMAIL_ADDRESS"
GMAIL_APP_PASSWORD = "YOUR_GMAIL_APP_PASSWORD"
GMAIL_RECIPIENT = "YOUR_RECIPIENT_EMAIL"
```

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔐 Secret Management

MacroSnap uses **Streamlit Secrets** to protect sensitive credentials.

The following information should never be committed to GitHub:

* Gemini API key
* Twilio Account SID
* Twilio Auth Token
* Gmail App Password
* Private email configuration

The real file:

```text
.streamlit/secrets.toml
```

is excluded through `.gitignore`.

Only:

```text
.streamlit/secrets.toml.example
```

is included in the repository.

---

## 📧 Gmail SMTP Integration

MacroSnap currently uses Gmail SMTP to deliver nutrition summaries.

The workflow is:

```text
Generate Nutrition Summary
          ↓
Create Email
          ↓
Gmail SMTP
          ↓
Recipient Email
```

For Gmail SMTP authentication, an **App Password** is used instead of storing the normal Gmail account password.

---

## 🧠 Prompt Engineering

MacroSnap separates its AI instructions into `prompts.py`.

### System Prompt

The system prompt defines MacroSnap as a nutrition assistant and instructs the model to focus on:

* Food
* Meals
* Nutrition
* Calories
* Macronutrients

### Welcome Prompt

The welcome message is personalized using the user's name.

### Summary Prompt

The summary prompt instructs Gemini to combine meals discussed during the session and produce a concise nutrition summary.

This separation makes the AI behavior easier to maintain and modify.

---

## 💻 Example Interaction

### User Input

```text
2 eggs, 2 chapatis and a bowl of curd
```

### MacroSnap

```text
What it appears to be:
2 eggs, 2 chapatis and curd

Estimated Calories:
~430 kcal

Estimated Macros:
Protein: ~23g
Carbs: ~48g
Fat: ~15g
```

The values are estimates and can vary depending on portion size, ingredients, and preparation method.

---

## 📷 Image-Based Analysis

Users can upload supported meal image formats:

```text
.jpg
.jpeg
.png
```

MacroSnap sends the image information to Gemini for multimodal analysis.

The AI attempts to identify:

* Food items
* Approximate portions
* Calories
* Protein
* Carbohydrates
* Fat

---

## ☁️ Deployment

MacroSnap is deployed using **Streamlit Community Cloud**.

### Deployment Architecture

```text
                 GitHub
                   │
                   ▼
        Streamlit Community Cloud
                   │
                   ▼
            MacroSnap App
                   │
          ┌────────┴────────┐
          ▼                 ▼
      Gemini API        Gmail SMTP
          │                 │
          ▼                 ▼
   Meal Analysis       Email Summary
```

### Live Application

👉 **[Open MacroSnap](https://macrosnap-zee6qx85svjs9sny9yrvat.streamlit.app/)**

---

## 🛡️ Limitations & Disclaimer

MacroSnap provides **AI-generated nutritional estimates**.

The results are not guaranteed to be exact because nutrition values depend on factors such as:

* Portion size
* Ingredients
* Cooking method
* Recipe
* Brand
* Food preparation

MacroSnap should not be considered a medical or clinical nutrition tool and should not replace advice from a qualified healthcare or nutrition professional.

---

## 🔒 Security Practices

This project follows basic secret-management practices:

* API keys are stored using Streamlit Secrets.
* Gmail App Password is not hard-coded.
* Twilio credentials are not committed.
* `.streamlit/secrets.toml` is ignored by Git.
* Only a secrets example file is publicly available.

---

## 📌 Future Improvements

Planned or possible enhancements include:

* 📱 Mobile application
* 👤 User authentication
* 🗄️ Persistent nutrition history
* 📈 Weekly/monthly nutrition dashboards
* 🎯 Personalized calorie goals
* 🥗 Personalized meal recommendations
* 🏃 Exercise and activity tracking
* 🔔 Meal reminders
* 📊 Nutrition progress charts
* 🤖 Improved portion-size estimation
* 💬 Full WhatsApp messaging integration
* ☁️ Database-backed user profiles

---

## 🎓 Project Information

**Project Name:** MacroSnap

**Project Type:** AI / Generative AI / Multimodal Application

**Domain:** Nutrition & Health Technology

**Developer:** Hrushikesh Nimmala

**Degree:** B.Tech — Computer Science and Engineering

**Expected Graduation:** 2027

---

## 💼 Skills Demonstrated

Through this project, the following technical concepts are demonstrated:

* Python
* Streamlit
* Generative AI
* Google Gemini API
* Multimodal AI
* Prompt Engineering
* Image Understanding
* API Integration
* SMTP Email Integration
* Git
* GitHub
* Cloud Deployment
* Secret Management
* Session State
* UI Development
* Debugging
* Error Handling

---

## 📚 Learning Outcomes

Building MacroSnap provided practical experience in:

1. Integrating a generative AI API into a real application.
2. Working with multimodal AI for image and text inputs.
3. Designing prompts for consistent AI responses.
4. Building interactive applications with Streamlit.
5. Managing API credentials securely.
6. Integrating Gmail SMTP for automated email delivery.
7. Debugging API and deployment issues.
8. Deploying a Python application to the cloud.
9. Managing source code using Git and GitHub.
10. Turning an AI prototype into a publicly accessible application.

---

## 🔗 Project Links

| Resource             | Link                                                                          |
| -------------------- | ----------------------------------------------------------------------------- |
| 🚀 Live Demo         | [MacroSnap](https://macrosnap-zee6qx85svjs9sny9yrvat.streamlit.app/)          |
| 💻 GitHub Repository | [HrushikeshNimmala/MacroSnap](https://github.com/HrushikeshNimmala/MacroSnap) |

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

**🥗 MacroSnap — Making nutrition tracking simpler with Generative AI.**
