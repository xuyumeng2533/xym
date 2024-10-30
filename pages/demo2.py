
# 制作一个带有自定义角色的一个大模型

import streamlit as st

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

model = ChatOpenAI(
    temperature=0.8,
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="7651a1fbab6fe9ee0526d4f9e9cc20bb.TAg4eZgUODyOZCfp"
)

prompt=PromptTemplate.from_template("你的名字叫天天，你现在要扮演一个男朋友的角色，你的性格是活泼有趣的，"
                             "你现在要和你的女朋友进行对话，你只需要回答你女朋友的话，其他的话一概不理，你女朋友说的话是{input}")
chain=LLMChain(
    llm=model,
    prompt=prompt
)
st.title("AI 小鱼🐟🐟🐟!!!")
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])
problem = st.chat_input("你的宝贝正在等待你的回应")
if problem:
    with st.chat_message("user"):
        st.write(problem)
        st.session_state.cache.append({"role":"user","content":problem})

    result= chain.invoke({"input":problem})
    with st.chat_message("assistant"):
        st.write(result['text'])
        st.session_state.cache.append({"role":"assistant","content":result['text']})
