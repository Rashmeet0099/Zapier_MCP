"""import streamlit as st
from zapier_integration import send_to_zapier_mcp, fetch_all_registrations_from_sheet
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Registration Chatbot", layout="centered")
st.title("🤖 Registration Chatbot using Zapier MCP")

# Session state setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "mode" not in st.session_state:
    st.session_state.mode = None  # Modes: "register", "show", None

# Display chat history
for sender, message in st.session_state.chat_history:
    st.chat_message(sender).write(message)

# Chat input
user_input = st.chat_input("Type 'register' or 'show all registrations'")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(("user", user_input))

    command = user_input.strip().lower()

    if command == "register":
        st.session_state.mode = "register"

    elif command == "show all registrations":
        st.session_state.mode = "show"
        with st.spinner("Fetching registrations..."):
            result = fetch_all_registrations_from_sheet()

            if isinstance(result, str):  # error message
                st.chat_message("bot").write(result)
                st.session_state.chat_history.append(("bot", result))
            else:
                if not result:
                    msg = "📭 No registrations found."
                    st.chat_message("bot").write(msg)
                    st.session_state.chat_history.append(("bot", msg))
                else:
                    st.chat_message("bot").write("📋 All Registered Users:")
                    for i, row in enumerate(result, 1):
                        formatted = f"{i}. {row['name']} | {row['email']} | {row['dob']}"
                        st.chat_message("bot").write(formatted)
                        st.session_state.chat_history.append(("bot", formatted))

        st.session_state.mode = None

    else:
        msg = "❓ Please type 'register' to add a user or 'show all registrations' to view entries."
        st.chat_message("bot").write(msg)
        st.session_state.chat_history.append(("bot", msg))

# Registration form flow
if st.session_state.mode == "register":
    with st.chat_message("bot"):
        st.subheader("📋 User Registration Form")

        with st.form("registration_form", clear_on_submit=True):
            name = st.text_input("Enter your Name")
            email = st.text_input("Enter your Email")
            dob = st.date_input("Enter your Date of Birth")

            submitted = st.form_submit_button("Submit Registration")

            if submitted:
                if name and email and dob:
                    with st.spinner("Submitting to Zapier MCP..."):
                        send_to_zapier_mcp(name, email, str(dob))
                        st.chat_message("bot").write("✅ Registration successful!")
                        st.session_state.chat_history.append(("bot", "✅ Registration successful!"))
                        st.session_state.mode = None
                        st.rerun()
                else:
                    st.warning("⚠️ Please fill in all fields.")  """
                    
# main.py

import streamlit as st
from zapier_integration import send_to_zapier_mcp, fetch_all_registrations_via_mcp, TOOL_MAP
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Zapier MCP Chatbot", layout="centered")
st.title("🤖 Zapier MCP Registration Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "mode" not in st.session_state:
    st.session_state.mode = None

if "selected_tool" not in st.session_state:
    st.session_state.selected_tool = list(TOOL_MAP.keys())[0]

# Tool selection
with st.sidebar:
    st.subheader("🔧 Select Tool")
    st.session_state.selected_tool = st.selectbox("Choose a Zapier tool:", list(TOOL_MAP.keys()))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.chat_message(sender).write(message)

# Chat input
user_input = st.chat_input("Type 'register' or 'show all registrations'")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(("user", user_input))

    command = user_input.strip().lower()

    if command == "register":
        st.session_state.mode = "register"

    elif command == "show all registrations":
        st.session_state.mode = "show"
        with st.spinner("Fetching from Zapier MCP..."):
            result = fetch_all_registrations_via_mcp(st.session_state.selected_tool)
            st.chat_message("bot").write(result)
            st.session_state.chat_history.append(("bot", result))
        st.session_state.mode = None

    else:
        msg = "❓ Type 'register' to add a user or 'show all registrations' to view entries."
        st.chat_message("bot").write(msg)
        st.session_state.chat_history.append(("bot", msg))

# Registration form
if st.session_state.mode == "register":
    with st.chat_message("bot"):
        st.subheader("📋 Register a New User")

        with st.form("registration_form", clear_on_submit=True):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            dob = st.date_input("Date of Birth")

            submitted = st.form_submit_button("Submit Registration")

            if submitted:
                if name and email and dob:
                    with st.spinner("Sending to Zapier MCP..."):
                        response = send_to_zapier_mcp(name, email, str(dob), st.session_state.selected_tool)
                        st.chat_message("bot").write("✅ Registration successful!")
                        st.session_state.chat_history.append(("bot", "✅ Registration successful!"))
                        st.session_state.mode = None
                        st.rerun()
                else:
                    st.warning("⚠️ Please fill in all fields.")

