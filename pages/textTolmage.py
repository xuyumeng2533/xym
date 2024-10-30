# import streamlit as st
# from zhipuai import ZhipuAI
# model = ZhipuAI(aapi_key="7651a1fbab6fe9ee0526d4f9e9cc20bb.TAg4eZgUODyOZCfp")
#
# desc = st.chat_input("请输入照片的描述")
# if desc:
#     with st.chat_message("user"):
#         st.write(desc)
#     response = model.images.generations(
#         model="cogview-3-plus",
#         prompt=desc,
#     )
#     with st.chat_message("assistant"):
#         st.image(response.data[0].url,width=300)
from zhipuai import ZhipuAI
import streamlit as st
import json
st.title("AI绘画")
client = ZhipuAI(api_key="9ee0c01ef679f3b2d14f1d2e25f5371a.FZvJ83u5XiL3KJmJ")  # 请填写您自己的APIKey

if "cache" not in st.session_state:
    st.session_state.cache = []
for message in st.session_state.cache:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.image(message["content"], width=200)
description = st.chat_input("请输入图片描述")

if description:
    with st.chat_message("user"):
        st.write(description)
        st.write("正在生成图片")
    st.session_state.cache.append({"role": "user", "content": description})
    try:
        response = client.images.generations(
            model="cogview-3-plus",  # 填写需要调用的模型编码
            prompt=description,
        )
        if response and response.data and len(response.data) > 0:
            image_data = response.data[0]
            if image_data.url:
                with st.chat_message("assistant"):
                    st.image(image_data.url, width=300)
                    # 将图片url写入cache
                st.session_state.cache.append({"role": "assistant", "content": image_data.url})

            else:
                st.error("生成的图片没有URL")
        else:
            st.error("生成的图片数据为空")
    except Exception as e:
        st.error(f"发生错误: {e}")