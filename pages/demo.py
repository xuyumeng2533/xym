import streamlit as st

from langchain_openai import ChatOpenAI
model= ChatOpenAI(temperature = 0.8,
                  model="glm-4-plus",
                  base_url="https://open.bigmodel.cn/api/paas/v4/",
                  api_key="7651a1fbab6fe9ee0526d4f9e9cc20bb.TAg4eZgUODyOZCfp")


st.title('AI demo小程序')
problem = st.chat_input("请输入你的问题")
if problem:
    with st.chat_message("user"):
        st.write(problem)
    result = model.invoke(problem)
    with st.chat_message("assistant"):
        st.write(result.content)