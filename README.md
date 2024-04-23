# Whisper File Conversion

## 概要

このアプリケーションは、音声ファイルをテキストに変換し、そのテキストを元に会議のサマリーを作成します。音声ファイルの変換には OpenAI の Whisper モデルを使用し、会議のサマリーの作成には OpenAI の GPT-3.5 モデルを使用します。

アプリケーションは以下の手順で動作します。

1. ユーザーは音声ファイルをアップロードします。
2. アプリケーションは音声ファイルをテキストに変換します。
3. アプリケーションはテキストを元に会議のサマリーを作成します。
4. アプリケーションは会議のサマリーをユーザーに表示します。

## 使い方

アプリケーションの使用方法は以下の通りです。

1. 音声ファイルをアップロードします。
2. アプリケーションは自動的に音声ファイルをテキストに変換し、会議のサマリーを作成します。
3. 会議のサマリーは画面に表示されます。

## 操作画面

![Input Interface](inputintreface.png)

## コードの説明

このアプリケーションの主要なコードは以下の通りです。

- `create_meeting_summary(openai_key, uploaded_audio)`: この関数は、音声ファイルをテキストに変換し、そのテキストを元に会議のサマリーを作成します。具体的には、OpenAI の Whisper モデルを使用して音声ファイルをテキストに変換し、そのテキストを OpenAI の GPT-3.5 モデルを使用して会議のサマリーを作成します。

- `app = gr.Interface(...)`: この部分は、Gradio を使用して Web アプリケーションを作成します。具体的には、`create_meeting_summary` 関数を呼び出し、その結果をユーザーに表示します。

- `app.launch(debug=True)`: この部分は、作成した Web アプリケーションを起動します。`debug=True` とすることで、デバッグモードを有効にします。

- `if __name__ == "__main__":`: この部分は、このスクリプトが直接実行されたときにのみ、Web アプリケーションを起動するようにします。これにより、このスクリプトが他のスクリプトからインポートされたときには、Web アプリケーションが起動しないようになります。

## 使われている技術とバージョン

アプリケーションは以下の技術を使用しています。

- OpenAI Whisper モデル
- OpenAI GPT-3.5 モデル
- Python 3.8
- Gradio 2.0.0
- emoji: ⚡
- colorFrom: yellow
- colorTo: red
- sdk: Gradio
- sdk_version: 3.50.2
- license: apache-2.0

---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
