import streamlit as st
import smtplib
from email.message import EmailMessage

from google import genai
from google.genai import types

from prompts import (
    SYSTEM_PROMPT,
    WELCOME_MESSAGE_TEMPLATE,
    SUMMARY_REQUEST_PROMPT
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MacroSnap | AI Nutrition Buddy",
    page_icon="🥗",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */

    .main {
        padding-top: 1rem;
    }


    /* Header */

    .macrosnap-header {
        text-align: center;
        padding: 10px 0 20px 0;
    }

    .macrosnap-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .macrosnap-subtitle {
        font-size: 17px;
        opacity: 0.75;
        margin-top: 4px;
    }


    /* Feature cards */

    .feature-card {
        padding: 15px;
        border-radius: 14px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        text-align: center;
        margin-bottom: 10px;
    }

    .feature-icon {
        font-size: 28px;
    }

    .feature-title {
        font-weight: 700;
        margin-top: 5px;
    }

    .feature-text {
        font-size: 13px;
        opacity: 0.7;
    }


    /* Summary */

    .summary-box {
        padding: 18px;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-top: 10px;
        margin-bottom: 15px;
    }


    /* Disclaimer */

    .disclaimer {
        font-size: 12px;
        opacity: 0.65;
        text-align: center;
        padding: 10px;
        margin-top: 20px;
    }


    /* Sidebar */

    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
    }


    /* Footer */

    .footer {
        text-align: center;
        font-size: 12px;
        opacity: 0.6;
        padding: 25px 0 10px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# GEMINI CONFIGURATION
# ============================================================

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]


@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)


gemini_client = get_gemini_client()


# ============================================================
# SESSION STATE
# ============================================================

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "whatsapp_number" not in st.session_state:
    st.session_state.whatsapp_number = ""

if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    st.session_state.chat = None

if "whatsapp_summary" not in st.session_state:
    st.session_state.whatsapp_summary = ""


# ============================================================
# ONBOARDING
# ============================================================

if not st.session_state.onboarded:

    st.markdown(
        """
        <div class="macrosnap-header">
            <div class="macrosnap-title">🥗 MacroSnap</div>
            <div class="macrosnap-subtitle">
                Your AI Nutrition Buddy
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Understand what you're eating with AI-powered "
        "meal analysis from text or photos."
    )

    st.divider()

    # Feature cards

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📸</div>
                <div class="feature-title">Meal Vision</div>
                <div class="feature-text">
                    Analyze food photos
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🔥</div>
                <div class="feature-title">Calories</div>
                <div class="feature-text">
                    Estimate nutrition
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📧</div>
                <div class="feature-title">Email Summary</div>
                <div class="feature-text">
                    Save your results
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.write("### 👋 Let's get started")

    with st.form("onboarding_form"):

        name = st.text_input(
            "Your Name",
            placeholder="Enter your name"
        )

        whatsapp_number = st.text_input(
            "WhatsApp Number",
            placeholder="+919876543210"
        )

        st.caption(
            "Your number is currently used as your MacroSnap "
            "profile information."
        )

        submitted = st.form_submit_button(
            "🚀 Start MacroSnap",
            use_container_width=True
        )

        if submitted:

            if not name.strip():

                st.error("Please enter your name.")

            elif not whatsapp_number.strip():

                st.error("Please enter your WhatsApp number.")

            else:

                st.session_state.user_name = name.strip()

                st.session_state.whatsapp_number = (
                    whatsapp_number.strip()
                )

                st.session_state.chat = (
                    gemini_client.chats.create(
                        model="gemini-flash-lite-latest",
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_PROMPT
                        )
                    )
                )

                welcome_message = (
                    WELCOME_MESSAGE_TEMPLATE.format(
                        name=st.session_state.user_name
                    )
                )

                st.session_state.messages = [
                    {
                        "role": "assistant",
                        "content": welcome_message
                    }
                ]

                st.session_state.whatsapp_summary = ""

                st.session_state.onboarded = True

                st.rerun()


# ============================================================
# MAIN APPLICATION
# ============================================================

else:

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="macrosnap-header">
            <div class="macrosnap-title">🥗 MacroSnap</div>
            <div class="macrosnap-subtitle">
                Welcome back, {st.session_state.user_name} 👋
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------

    with st.sidebar:

        st.markdown(
            '<div class="sidebar-title">👤 Profile</div>',
            unsafe_allow_html=True
        )

        st.write(
            f"**Name**  \n"
            f"{st.session_state.user_name}"
        )

        st.write(
            f"**WhatsApp**  \n"
            f"{st.session_state.whatsapp_number}"
        )

        st.divider()

        st.write("### ⚙️ Session")

        if st.button(
            "🔄 Start New Session",
            use_container_width=True
        ):

            st.session_state.messages = []

            st.session_state.whatsapp_summary = ""

            st.session_state.chat = (
                gemini_client.chats.create(
                    model="gemini-flash-lite-latest",
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT
                    )
                )
            )

            welcome_message = (
                WELCOME_MESSAGE_TEMPLATE.format(
                    name=st.session_state.user_name
                )
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": welcome_message
                }
            )

            st.rerun()


        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.user_name = ""

            st.session_state.whatsapp_number = ""

            st.session_state.onboarded = False

            st.session_state.messages = []

            st.session_state.chat = None

            st.session_state.whatsapp_summary = ""

            st.rerun()

        st.divider()

        st.info(
            "💡 Tip: Upload a clear photo of your meal "
            "for better food identification."
        )


    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    if len(st.session_state.messages) == 1:

        st.markdown(
            """
            **How to use MacroSnap**

            📸 Upload a photo of your meal  
            💬 Or describe what you ate  
            🔥 Get estimated calories & macros  
            📧 Generate and email your nutrition summary
            """
        )

        st.divider()


    # --------------------------------------------------------
    # CHAT HISTORY
    # --------------------------------------------------------

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


    # --------------------------------------------------------
    # CHAT INPUT
    # --------------------------------------------------------

    chat_input = st.chat_input(
        "🍽️ Tell me what you ate or upload a meal photo...",
        accept_file=True,
        file_type=["jpg", "jpeg", "png"]
    )


    if chat_input:

        user_text = chat_input.text

        uploaded_files = chat_input.files

        uploaded_file = None

        image_bytes = None


        if uploaded_files:

            uploaded_file = uploaded_files[0]

            image_bytes = uploaded_file.getvalue()


        # ----------------------------------------------------
        # USER MESSAGE
        # ----------------------------------------------------

        with st.chat_message("user"):

            if user_text:

                st.markdown(user_text)

            if uploaded_file:

                st.image(
                    image_bytes,
                    caption="🍽️ Your meal",
                    width=350
                )


        # ----------------------------------------------------
        # SAVE USER MESSAGE
        # ----------------------------------------------------

        if user_text:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": user_text
                }
            )

        elif uploaded_file:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": "📸 Meal photo uploaded"
                }
            )


        # ----------------------------------------------------
        # AI RESPONSE
        # ----------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner(
                "🔍 Analyzing your meal..."
            ):

                try:

                    if uploaded_file:

                        image_part = (
                            types.Part.from_bytes(
                                data=image_bytes,
                                mime_type=uploaded_file.type
                            )
                        )


                        if user_text:

                            prompt = user_text

                        else:

                            prompt = (
                                "Analyze this meal photo carefully. "
                                "Identify the foods visible in the image. "
                                "Estimate the calories and macros for "
                                "the meal. Include estimated calories, "
                                "protein, carbohydrates, and fat. "
                                "Mention that these are approximate "
                                "estimates because portion sizes and "
                                "ingredients may vary."
                            )


                        response = (
                            st.session_state.chat.send_message(
                                [image_part, prompt]
                            )
                        )


                    else:

                        response = (
                            st.session_state.chat.send_message(
                                user_text
                            )
                        )


                    answer = response.text


                except Exception as error:

                    answer = (
                        "Sorry, something went wrong.\n\n"
                        f"`{error}`"
                    )


            st.markdown(answer)


        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


    # ========================================================
    # NUTRITION SUMMARY
    # ========================================================

    st.divider()

    st.subheader("📊 Nutrition Summary")

    st.write(
        "Create a summary of the meals discussed "
        "during this session."
    )


    # --------------------------------------------------------
    # GENERATE SUMMARY
    # --------------------------------------------------------

    if st.button(
        "📝 Generate Nutrition Summary",
        use_container_width=True
    ):

        with st.spinner(
            "🧠 Preparing your nutrition summary..."
        ):

            try:

                summary_response = (
                    st.session_state.chat.send_message(
                        SUMMARY_REQUEST_PROMPT
                    )
                )

                whatsapp_summary = (
                    summary_response.text
                )

                st.session_state.whatsapp_summary = (
                    whatsapp_summary
                )

                st.success(
                    "✅ Nutrition summary generated!"
                )


            except Exception as error:

                st.error(
                    "Could not generate the nutrition summary."
                )

                st.code(str(error))


    # --------------------------------------------------------
    # SUMMARY DISPLAY
    # --------------------------------------------------------

    if st.session_state.whatsapp_summary:

        st.markdown(
            """
            <div class="summary-box">
            """,
            unsafe_allow_html=True
        )

        st.write("### 📋 Your Summary")

        st.text_area(
            "Nutrition Summary",
            value=st.session_state.whatsapp_summary,
            height=200,
            label_visibility="collapsed"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # EMAIL
        # ----------------------------------------------------

        st.write("### 📧 Save Your Summary")

        st.write(
            "Send this nutrition summary to your configured "
            "email address."
        )

        if st.button(
            "📧 Send Summary by Email",
            use_container_width=True
        ):

            try:

                sender_email = st.secrets[
                    "GMAIL_SENDER"
                ]

                app_password = st.secrets[
                    "GMAIL_APP_PASSWORD"
                ]

                recipient_email = st.secrets[
                    "GMAIL_RECIPIENT"
                ]


                email = EmailMessage()

                email["Subject"] = (
                    "🥗 MacroSnap Nutrition Summary"
                )

                email["From"] = sender_email

                email["To"] = recipient_email


                email_body = (
                    f"Hi {st.session_state.user_name}! 👋\n\n"
                    "Here is your MacroSnap nutrition summary:\n\n"
                    "----------------------------------------\n\n"
                    f"{st.session_state.whatsapp_summary}\n\n"
                    "----------------------------------------\n\n"
                    "Keep tracking your meals! 🥗💪\n\n"
                    "This nutrition information is an estimate "
                    "and may vary based on portion sizes and "
                    "ingredients.\n\n"
                    "— MacroSnap AI"
                )


                email.set_content(email_body)


                with smtplib.SMTP(
                    "smtp.gmail.com",
                    587
                ) as smtp:

                    smtp.starttls()

                    smtp.login(
                        sender_email,
                        app_password
                    )

                    smtp.send_message(email)


                st.success(
                    "✅ Nutrition summary sent successfully!"
                )


            except Exception as error:

                st.error(
                    "❌ Could not send the email."
                )

                st.code(str(error))


    # --------------------------------------------------------
    # DISCLAIMER
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="disclaimer">
            ⚠️ Nutrition values provided by MacroSnap are
            AI-generated estimates. Actual calories and macros
            may vary depending on ingredients, preparation,
            and portion size.
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="footer">
            🥗 MacroSnap · AI Nutrition Buddy<br>
            Powered by Gemini AI
        </div>
        """,
        unsafe_allow_html=True
    )
