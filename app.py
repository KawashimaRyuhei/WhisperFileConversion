import gradio as gr
import openai

def create_meeting_summary(openai_key, uploaded_audio):
    openai.api_key = openai_key

    with open(uploaded_audio.name, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
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
    title="Whisper Transcription",
    description="音声ファイルをアップロードして、会議のサマリーをMarkdown形式で作成します。"
)

app.launch(debug=True)