'''
记忆
'''
#制作聊天界面
import streamlit as st
from langchain_openai import ChatOpenAI
#引用提示词对象
from langchain.prompts import PromptTemplate
#链对象
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
#解决重新加载的问题  重新加载的时候保证聊天记录不会清空
#构建大模型 智谱
model=ChatOpenAI(
    temperature=0.8,#创新性
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="7651a1fbab6fe9ee0526d4f9e9cc20bb.TAg4eZgUODyOZCfp",

)
#记忆
# memory=ConversationKGMemory(memery_key="history")
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="history")
else:
    st.session_state.memory = st.session_state.memory
#提示词对象
prompt=PromptTemplate.from_template("你的名字是天天，你现在是一个好脾气，情商高，三观正,身材颜值在线的男朋友."
                                    "你现在要和你的女朋友对话，内容是{input}，你要做出回应，历史对话为{history}")
#关联
chain=LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)
st.title("AI 小雨🌧🌧🌧!!!")
#构建缓存保存聊天记录
if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message["content"])

#创建聊天输入框
problem =st.chat_input("你的宝贝正在等待你的回应")
#确定问题被输入
if problem:
#输入问题 、调用大模型回答问题 、将大模型回答的问题输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})
    result=chain.invoke({"input":problem})
    with st.chat_message("assistant"):
         st.write(result['text'])
    st.session_state.cache.append({"role": "assistant", "content": result['text']})