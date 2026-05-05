import streamlit as st
import pandas as pd

st.title("問い合わせ管理アプリ")

if "data" not in st.session_state:
    st.session_state.data = []

with st.form("form"):
    name = st.text_input("氏名")
    question = st.text_area("問い合わせ内容")
    category = st.selectbox("カテゴリ", ["休暇", "給与", "福利厚生", "その他"])
    submitted = st.form_submit_button("送信")

if submitted:
    if question.strip() == "":
        st.error("内容を入力してください")
    else:
        st.success("登録しました")
        st.session_state.data.append({
            "名前": name,
            "カテゴリ": category,
            "内容": question
        })

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.subheader("問い合わせ履歴")
    st.dataframe(df)