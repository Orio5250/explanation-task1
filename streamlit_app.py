import streamlit as st

# 追加問題を含むクイズデータ
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
        "answer": "新しい関数を定義しようとしている",
        "explanation": "`def` は **define（定義する）** の略です。これに続く名前（ここでは `f`）を関数名として登録し、括弧内の引数を受け取る準備をします。"
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
        "answer": "x の 3乗（べき乗）を計算する",
        "explanation": "Pythonでは `**` は **べき乗（累乗）** を表します。`x * 3`（3倍）や `x + 3`（加算）とは明確に区別されます。"
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
        "answer": "R と L の差の絶対値が tolerance 以上である間",
        "explanation": "`while` は条件が **真 (True) である限り** 処理を繰り返します。`abs()` は絶対値を返し、`>=` は「以上」を意味します。"
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
        "answer": "大文字・小文字の区別を無視して比較できるようにするため",
        "explanation": "`.lower()` は文字列をすべて小文字に変換します。これにより、ユーザーが \"END\", \"End\", \"end\" のどれを入力しても正しく判定できるようになります。"
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
        "answer": "何も返さずに（空の値を返して）関数を終了する",
        "explanation": "`None` は Pythonにおける「値が存在しない状態」を表す特殊な値です。値を返さずに処理を終えたい場合や、失敗を知らせる際に使われます。"
    },
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
