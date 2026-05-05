import streamlit as st

st.title("総務問い合わせ入力")


with st.form("inquiry_form"):
    name = st.text_input("氏名")
    question = st.text_area("問い合わせ内容", height=160)
    category = st.selectbox("カテゴリ", ["休暇", "給与", "福利厚生", "その他"])
    priority = st.radio("緊急度", ["高", "中", "低"])
    agree = st.checkbox("内容を確認しました")

    submitted = st.form_submit_button("送信する")


if submitted:
    if question.strip() == "":
        st.error("問い合わせ内容を入力してください。")
    elif not agree:
        st.warning("確認チェックをしてください。")
    else:
        st.success(f"{name}さんの問い合わせを受け付けました。")
        st.subheader("入力内容")
        st.write("名前:", name)
        st.write("カテゴリ:", category)
        st.write("緊急度:", priority)
        st.write("内容:", question)