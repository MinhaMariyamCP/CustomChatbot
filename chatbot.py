import streamlit as st

st.title("🤖 Clara 💫 - Study Chatbot")

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Response logic
def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hi", "hello", "hey"]:
        return "Hey! 😊 I'm Clara, your study buddy. What do you need help with?"

    elif "how are you" in user_input:
        return "I'm doing great! Ready to help you study 💪"

    elif "your name" in user_input:
        return "I'm Clara 💫 your personal study chatbot!"

    elif "c programming" in user_input:
        return "C is a powerful programming language used for system and application development."

    elif "python" in user_input:
        return "Python is an easy and powerful language used in AI, web, and data science."

    elif "data structure" in user_input:
        return "Data structures help organize data efficiently like arrays, stacks, and queues."

    elif "stack" in user_input:
        return "Stack follows LIFO (Last In First Out)."

    elif "queue" in user_input:
        return "Queue follows FIFO (First In First Out)."

    elif "algorithm" in user_input:
        return "An algorithm is a step-by-step method to solve a problem."

    elif "exam" in user_input:
        return "Don’t stress! Break topics and revise step by step 📚"

    elif "lazy" in user_input:
        return "Start with just 5 minutes. That’s the trick 💪"

    elif "bye" in user_input:
        return "Goodbye 👋 All the best!"

    else:
        return "Hmm 🤔 I’m still learning. Try asking something related to studies!"

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
prompt = st.chat_input("Ask Clara something...")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    reply = get_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
