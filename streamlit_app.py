import streamlit as st

# クイズデータ：純粋なコードの意味（挙動）にフォーカス
quiz_data = [
    {
        "code": "def f(x, a):",
        "question": "Pythonの文法において、この `def` キーワードは何を行っていますか？",
        "options": [
            "変数 f に x と a を代入している",
            "新しい関数を定義しようとしている",
            "既存の関数 f を呼び出している",
            "条件分岐を開始している"
        ],
        "answer": "新しい関数を定義しようとしている"
    },
    {
        "code": "x**3",
        "question": "この `**` という演算子はどういう計算を意味しますか？",
        "options": [
            "x を 3倍する",
            "x を 3回足す",
            "x の 3乗（べき乗）を計算する",
            "x を 3回繰り返す文字列にする"
        ],
        "answer": "x の 3乗（べき乗）を計算する"
    },
    {
        "code": "while abs(R - L) >= tolerance:",
        "question": "この `while` 文が繰り返される「条件」を正確に説明しているのはどれですか？",
        "options": [
            "R と L の差の絶対値が tolerance 以上である間",
            "R と L の差が tolerance と等しくなるまで",
            "R と L の差が tolerance 未満になった瞬間だけ",
            "変数 tolerance が 0 になるまで"
        ],
        "answer": "R と L の差の絶対値が tolerance 以上である間"
    },
    {
        "code": "user_input.lower() == \"end\"",
        "question": "`.lower()` メソッドを使用する主な目的は何ですか？",
        "options": [
            "入力された文字数をカウントするため",
            "入力が数値かどうかを判定するため",
            "大文字・小文字の区別を無視して比較できるようにするため",
            "文字列を末尾から読み取るため"
        ],
        "answer": "大文字・小文字の区別を無視して比較できるようにするため"
    },
    {
        "code": "return None",
        "question": "関数内で `return None` が実行されると、何が起こりますか？",
        "options": [
            "エラーが発生してプログラムが止まる",
            "何も返さずに（空の値を返して）関数を終了する",
            "数値の 0 を返す",
            "関数を最初からやり直す"
        ],
        "answer": "何も返さずに（空の値を返して）関数を終了する"
    }
]

# --- Streamlit UI ---
st.set_page_config(page_title="Python Syntax Quiz", layout="centered")

st.title("🧩 Python文法解読クイズ")
st.caption("コードの「純粋な挙動」を正確に理解できているかチェックしましょう。")

if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.finished = False

if not st.session_state.finished:
    q = quiz_data[st.session_state.step]
    
    st.markdown(f"### 問題 {st.session_state.step + 1} / {len(quiz_data)}")
    st.code(q["code"], language="python")
    
    # フォームを使用して再描画を制御
    with st.form(key=f"form_{st.session_state.step}"):
        choice = st.radio("このコードが命令していることは？", q["options"], index=None)
        submitted = st.form_submit_button("回答を確定")
        
        if submitted:
            if choice == q["answer"]:
                st.session_state.score += 1
                st.success("正解です！")
            else:
                st.error(f"不正解です。正解は: {q['answer']}")
            
            # 次のステップへ
            if st.session_state.step + 1 < len(quiz_data):
                st.session_state.step += 1
                st.form_submit_button("次の問題へ")
            else:
                st.session_state.finished = True
                st.form_submit_button("結果を見る")
else:
    st.balloons()
    st.header("リザルト")
    st.metric("正解数", f"{st.session_state.score} / {len(quiz_data)}")
    
    if st.button("最初から解き直す"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.rerun()
