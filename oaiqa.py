# 必要なライブラリをインポートします
import streamlit as st
import openai
import os

# Azure OpenAIのAPIキーを設定します
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_version = "2023-07-01-preview"
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
deployname="gpt4-32k"

def get_answer(question):
    # messageにopenaiのchatメッセージを入力します
    # roleはuserです
    messages = [{"role": "user", "content": question}]

    # Azure OpenAIに質問を送信し、応答を取得します
    response = openai.ChatCompletion.create(
        engine=deployname,
        messages=messages
    )
    # 応答からテキストを抽出します
    answer = response['choices'][0]['message']
    return answer

# Streamlitアプリケーションをセットアップします
st.title('Azure OpenAI Translation App')

option = st.selectbox(
   "Select language?",
   ("English to Japanese", "Japanese to English", "none"),
   index=None,
   placeholder='Select',
)

st.write('Enter:')
user_question = st.text_input('Text:')
if option == "English to Japanese":
    user_question = "Translate from English to Japanese: " + user_question
elif option == "Japanese to English":
    user_question = "Translate from Japanese to English: " + user_question
else:
    user_question = user_question

if user_question:
    answer = get_answer(user_question)
    st.write('Answer:', answer['content'])
