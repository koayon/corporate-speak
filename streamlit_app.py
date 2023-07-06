import openai
import streamlit as st

st.set_page_config(page_title="Corporate Speak", page_icon="assets/favicon/Karen.jpg")

with st.sidebar:
    st.title("Corporate Speak")
    st.write(
        "Star on [GitHub](www.github.com/koayon/corporate-speak) to support this project!"
    )
    st.write("Created by [Kola Ayonrinde](www.kolaayonrinde.com)")

openai.api_key = st.secrets["OPENAI_API_KEY"]
# base_prompt = "Can you rephrase this in corporate language: /n/n"
base_prompt = "Can you rephrase following text in corporate language. Please be concise and diplomatic. Here's the text to be rephrased: /n/n"
# new_base_prompt = "You are CorporateGPT, a language model trained by OpenAI to write in the style of a startup manager. Can you rephrase this in corporate language: /n/n"

st.title("🧑‍💼 Corporate Speak")

with st.expander("About This App"):
    "This app uses AI to help you write those pesky Teams messages and emails."
    "Now you can sound like a corporate slave without worrying about how to phrase everything."
    "Which leaves more time for grinding away and selling your soul."
    "Enjoy!"

with st.form("written_form"):
    user_input = st.text_input(
        "What do you want to say?", placeholder="I don't think that's a great idea"
    )
    submit_button = st.form_submit_button("Submit")

# listen, submit_listen, _ = st.columns([1,1,3])
# with listen:
#   listen_button = st.button("Tap to speak")
#   if listen_button:
#     "🔈 Listening..."
# with submit_listen:
#   audio_capture_button = st.button("Send audio")


@st.cache_data
def corporatify(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": base_prompt + user_input},
        ],
    )

    return response["choices"][0]["message"]["content"]  # type: ignore


# if audio_capture_button:
#   user_input = audio_capture_button
audio_capture_button = False

if submit_button or audio_capture_button:
    result = corporatify(user_input)
    # streamlit columns
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Instead of saying...")
        st.write(user_input)
    with col2:
        st.subheader("Try saying...")
        st.write(result)

    st.success(
        "You can now sound like a corporate slave. Congrats! Don't forget to slay xo",
        icon="👑",
    )
else:
    st.info("Please enter some text above!", icon="☝️")
