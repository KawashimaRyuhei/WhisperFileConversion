import gradio as gr
import openai

def create_meeting_summary(openai_key, uploaded_audio):
    openai.api_key = openai_key
    transcript = openai.Audio.transcribe("whisper-1", open(uploaded_audio, "rb"))
    system_template = """会議の書き起こしが渡されます。

この会議のサマリーをMarkdown形式で作成してください。サマリーは、以下のような形式で書いてください。

- 会議の目的
- 会議の内容
- 会議の結果"""

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_template},
            {"role": "user", "content": transcript.text}
        ]
    )
    response_text = completion.choices[0].message.content
    return response_text

inputs = [
    gr.Textbox(lines=1, label="openai_key"),
    gr.Audio(type="filepath", label="音声ファイルをアップロード")
]

outputs = gr.Textbox(label="会議サマリー")

app = gr.Interface(
    fn=create_meeting_summary,
    inputs=inputs,
    outputs=outputs,
    title="会議サマリー生成アプリ",
    description="音声ファイルをアップロードして、会議のサマリーをMarkdown形式で作成します。"
)

app.launch(debug=True)