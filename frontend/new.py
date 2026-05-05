import streamlit as st

# -----------------------------
# Title
# -----------------------------
st.title("総務問い合わせ入力アプリ")
st.write("社員からの問い合わせを入力してください。")

# -----------------------------
# Session State (history store)
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# Form
# -----------------------------
with st.form("inquiry_form"):

    name = st.text_input("氏名")
    category = st.selectbox("カテゴリ", ["休暇", "給与", "福利厚生", "その他"])
    priority = st.radio("緊急度", ["高", "中", "低"])
    question = st.text_area("問い合わせ内容", height=160)

    submitted = st.form_submit_button("送信する")

# -----------------------------
# Submit Action
# -----------------------------
if submitted:

    if question.strip() == "":
        st.error("問い合わせ内容を入力してください。")

    else:
        st.success("問い合わせを受け付けました。")

        st.subheader("入力内容")
        st.write("👤 氏名:", name)
        st.write("📂 カテゴリ:", category)
        st.write("⚡ 緊急度:", priority)
        st.write("📝 内容:", question)

        # save history
        st.session_state.history.append({
            "氏名": name,
            "カテゴリ": category,
            "緊急度": priority,
            "内容": question
        })

# -----------------------------
# History Section
# -----------------------------
st.divider()
st.subheader("📋 問い合わせ履歴")

if len(st.session_state.history) == 0:
    st.info("まだ履歴はありません。")
else:
    for i, item in enumerate(st.session_state.history, start=1):
        st.write(f"--- 問い合わせ {i} ---")
        st.write("👤", item["氏名"])
        st.write("📂", item["カテゴリ"])
        st.write("⚡", item["緊急度"])
        st.write("📝", item["内容"])