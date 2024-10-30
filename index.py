import streamlit as st
st.title("AI大数据应用产品网")


c1,c2= st.columns(2)
with c1:
    st.image("https://i.pinimg.com/736x/07/f7/06/07f706134498b6e63d2ae49e05a8170a.jpg",
             use_column_width=True)
    flag=st.button("智能回答",use_container_width=True)
    if flag:
        st.switch_page("pages/demo3.py")
with c2:
    st.image("https://i.pinimg.com/736x/07/f7/06/07f706134498b6e63d2ae49e05a8170a.jpg",
             use_column_width=True)
    flag1=st.button("智能画图",use_container_width=True)
    if flag1:
        st.switch_page("pages/textTolmage.py")
# import streamlit as st
#
# st.title("AI模型")
# c1,c2,c3,c4,c5 = st.columns(5)
# with c1:
#     flag=st.button("NO.1")
#     if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1=st.button("NO.2")
#     if flag1:
#         st.switch_page("pages/demo1.py")
#
# with c3:
#     flag2=st.button("NO.3")
#     if flag2:
#         st.switch_page("pages/demo2.py")
#
# with c4:
#     flag3=st.button("NO.4")
#     if flag3:
#         st.switch_page("pages/demo3.py")
# with c5:
#     flag4 = st.button("文生图")
#     if flag4:
#         st.switch_page("pages/textTolmage.py")


