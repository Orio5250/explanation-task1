import streamlit as st

# 追加問題を含むクイズデータ
quiz_data = [
    # --- 既存の問題（一部省略して追加分を重点的に記載） ---
    {
        "code": "def f(x, a):",
        "question": "Pythonの文法において、この `def` キーワードは何を行っていますか？",
        "options": ["変数 f に x と a を代入している", "新しい関数を定義しようとしている", "既存の関数 f を呼び出している", "条件分岐を開始している"],
        "answer": "新しい関数を定義しようとしている",
        "explanation": "`def` は **define（定義する）** の略です。これに続く名前を関数名として登録します。"
    },
    # --- 新規追加問題 1: 辞書の安全な取得 ---
    {
        "code": "value = data.get('key', 0)",
        "question": "この `.get()` メソッドを使う最大のメリットは何ですか？",
        "options": [
            "辞書の中に 'key' がなくてもエラーにならず、0 を返してくれる",
            "辞書の内容をすべて削除して 0 にリセットする",
            "辞書の中から 'key' という単語を検索して画面に表示する",
            "辞書を数値データに変換する"
        ],
        "answer": "辞書の中に 'key' がなくてもエラーにならず、0 を返してくれる",
        "explanation": "通常の `data['key']` だとキーが存在しない時にプログラムが強制終了しますが、`.get()` なら安全にデフォルト値を返せます。"
    },
    # --- 新規追加問題 2: リストのスライス ---
    {
        "code": "items = [10, 20, 30, 40, 50]\nprint(items[1:4])",
        "question": "このコードを実行したとき、表示される内容はどれですか？",
        "options": [
            "[10, 20, 30]",
            "[20, 30, 40]",
            "[20, 30, 40, 50]",
            "[10, 40]"
        ],
        "answer": "[20, 30, 40]",
        "explanation": "スライス `[開始:終了]` は、開始インデックスを含み、**終了インデックスを含まない**のがルールです。インデックスは0から始まるので、1番目(20)から3番目(40)までが取り出されます。"
    },
    # --- 新規追加問題 3: 例外処理 ---
    {
        "code": "try:\n    res = requests.get(url)\nexcept Exception as e:\n    print(e)",
        "question": "この `try...except` 構文の役割は何ですか？",
        "options": [
            "エラーが起きそうな処理を試し、失敗してもプログラムを止めずに処理する",
            "プログラムを3回繰り返して実行する",
            "通信が成功するまで無限に待ち続ける",
            "コードを暗号化して保護する"
        ],
        "answer": "エラーが起きそうな処理を試し、失敗してもプログラムを止めずに処理する",
        "explanation": "ネットワークエラーなどの「想定外のトラブル」が起きても、アプリ全体をクラッシュさせずにエラーメッセージを出すなどの対応が可能になります。"
    }
]

# --- UI実装部分は前述のコードと同様（quiz_dataを差し替えるだけ） ---
# --- Streamlit UI ---
st.set_page_config(page_title="Python Syntax Quiz", layout="centered")

st.title("🧩 Python文法解読クイズ")
st.caption("コードの「純粋な挙動」を正確に理解できているかチェックしましょう。")

# セッション状態の初期化
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.finished = False
    st.session_state.answered = False  # 回答済みかどうかを管理

if not st.session_state.finished:
    q = quiz_data[st.session_state.step]
    
    st.markdown(f"### 問題 {st.session_state.step + 1} / {len(quiz_data)}")
    st.code(q["code"], language="python")
    
    # 選択肢の表示
    choice = st.radio("このコードが命令していることは？", q["options"], index=None, key=f"radio_{st.session_state.step}", disabled=st.session_state.answered)

    if not st.session_state.answered:
        # 回答ボタン
        if st.button("回答を確定", type="primary"):
            if choice:
                st.session_state.answered = True
                st.rerun()
            else:
                st.warning("選択肢を選んでください。")
    else:
        # 回答後の解説表示
        if choice == q["answer"]:
            st.success(f"🎯 **正解です！**")
            if st.session_state.step == 0: # 最初の正解時にスコア加算
                 st.session_state.score += 1
        else:
            st.error(f"❌ **不正解です...**")
            st.write(f"正解は: **{q['answer']}**")
        
        # 解説文の表示
        st.info(f"**解説:** {q['explanation']}")
        
        # 次のボタン
        button_label = "次の問題へ" if st.session_state.step + 1 < len(quiz_data) else "結果を見る"
        if st.button(button_label):
            # スコア集計（ラジオボタンの選択が正解だった場合）
            if choice == q["answer"]:
                st.session_state.score += 1
            
            if st.session_state.step + 1 < len(quiz_data):
                st.session_state.step += 1
                st.session_state.answered = False
                st.rerun()
            else:
                st.session_state.finished = True
                st.rerun()

else:
    # リザルト画面
    st.balloons()
    st.header("🏁 終了！お疲れ様でした。")
    
    # スコアに応じたメッセージ
    score_ratio = st.session_state.score / len(quiz_data)
    if score_ratio == 1.0:
        st.success("完璧です！Pythonの基本文法がしっかり身についています。")
    elif score_ratio >= 0.6:
        st.info("良い調子です！間違えた箇所を復習して完璧を目指しましょう。")
    else:
        st.warning("基礎をもう一度確認してみましょう。一歩ずつ進めば大丈夫です！")

    st.metric("あなたの正解数", f"{st.session_state.score} / {len(quiz_data)}")
    
    if st.button("最初から解き直す"):
        st.session_state.step = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.session_state.answered = False
        st.rerun()
