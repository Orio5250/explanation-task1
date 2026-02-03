import streamlit as st

# クイズのデータセット
quiz_data = [
    {
        "code": "def f(x, a):\n    return x**3 - x - a",
        "question": "この関数 f(x, a) は何を定義していますか？",
        "options": ["xの3次方程式の左辺", "xの2乗を計算する式", "aの値を入力する関数", "グラフを描画する関数"],
        "answer": "xの3次方程式の左辺"
    },
    {
        "code": "while abs(R - L) >= tolerance:",
        "question": "このwhileループの終了条件は何を意味していますか？",
        "options": ["計算回数が上限に達したとき", "区間の幅が許容誤差より小さくなったとき", "解が0になったとき", "ユーザーがendと入力したとき"],
        "answer": "区間の幅が許容誤差より小さくなったとき"
    },
    {
        "code": "M = (L + R) / 2",
        "question": "この行で行っている処理は何ですか？",
        "options": ["右端の値を更新している", "左端の値を更新している", "探索区間の中間点を求めている", "誤差を計算している"],
        "answer": "探索区間の中間点を求めている"
    },
    {
        "code": "elif f(L, a) * f_M < 0:\n    R = M",
        "question": "この条件式が真（True）の場合、何がわかりますか？",
        "options": ["解が右半分の区間にある", "解が左半分の区間にある", "解がちょうどMである", "解が存在しない"],
        "answer": "解が左半分の区間にある"
    }
]

# アプリのタイトル
st.title("🐍 Pythonコード解説クイズ")
st.write("二分法のコードを1ブロックずつ読み解きましょう！")

# セッション状態の初期化（進捗管理）
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_complete = False

# クイズ終了画面
if st.session_state.quiz_complete:
    st.success(f"全問終了！あなたのスコアは {st.session_state.score} / {len(quiz_data)} です。")
    if st.button("もう一度挑戦する"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_complete = False
        st.rerun()
else:
    # 現在の問題を取得
    q = quiz_data[st.session_state.current_question]
    
    st.subheader(f"問題 {st.session_state.current_question + 1}")
    
    # コードを表示
    st.code(q["code"], language="python")
    
    # 質問と選択肢
    st.write(q["question"])
    
    # 選択肢をフォームで表示
    with st.form(key=f"quiz_form_{st.session_state.current_question}"):
        user_choice = st.radio("答えを選んでください：", q["options"], index=None)
        submit_button = st.form_submit_button(label="回答する")

        if submit_button:
            if user_choice is None:
                st.warning("選択肢を選んでください。")
            else:
                if user_choice == q["answer"]:
                    st.success("正解！✨")
                    st.session_state.score += 1
                else:
                    st.error(f"残念！正解は「{q['answer']}」でした。")
                
                # 次の問題へ進む準備
                if st.session_state.current_question + 1 < len(quiz_data):
                    st.session_state.current_question += 1
                    st.button("次の問題へ")
                else:
                    st.session_state.quiz_complete = True
                    st.button("結果を見る")
