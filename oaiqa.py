# 必要なライブラリをインポートします
import streamlit as st
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
load_dotenv(".env")

# Azure OpenAIのAPIキーを設定します
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = os.getenv("AZURE_API_VERSION")
)
model = os.getenv("AZURE_OPENAI_MODEL")

def get_answer(question):
    # messageにopenaiのchatメッセージを入力します
    # roleはuserです
    messages = [{"role": "user", "content": question}]

    # Azure OpenAIに質問を送信し、応答を取得します
    response = client.chat.completions.create(
        model = model,
        messages = messages
    )
    # 応答からテキストを抽出します
    answer = response.choices[0].message # response['choices'][0]['message']
    return answer

# Streamlitアプリケーションをセットアップします
st.title('Azure OpenAI Translation and Q&A App (Powered by GPT-4)')

# 質問の選択肢を定義します
option = st.selectbox(
   "Select language",
   ("English to Japanese", "Japanese to English", "Question and Answer"),
   index=None,
   placeholder='Select',
)

user_question = st.text_area('Text:', height=100)

if user_question:
    if option == "English to Japanese":
        user_question = "Translate from English to Japanese: " + user_question
    elif option == "Japanese to English":
        user_question = "Translate from Japanese to English: " + user_question
    else:
        user_question = user_question

    answer = get_answer(user_question)
    st.write('Answer:')
    st.write(answer.content)
