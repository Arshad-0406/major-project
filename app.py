import gradio as gr

# Replace with your real model
def generate_image(prompt):
    image_path = "output.png"
    return image_path


with gr.Blocks(
    theme=gr.themes.Soft(),
    css="""
/* Background */
body {
    background: radial-gradient(circle at top, #020617, #000);
}

/* Title */
#title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    background: linear-gradient(90deg, #00ffff, #a855f7);
    -webkit-background-clip: text;
    color: transparent;
    margin-bottom: 5px;
}

/* Subtitle */
#subtitle {
    text-align: center;
    opacity: 0.6;
    margin-bottom: 25px;
    font-size: 14px;
}

/* Card */
#card {
    max-width: 520px;
    margin: auto;
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    box-shadow: 0 0 40px rgba(0,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.08);
}

/* Textbox */
textarea {
    background: #020617 !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid #1f2937 !important;
    padding: 12px !important;
    font-size: 14px !important;
}

/* Button */
button {
    background: linear-gradient(90deg, #06b6d4, #9333ea) !important;
    border: none !important;
    border-radius: 12px !important;
    color: white !important;
    font-weight: 600 !important;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px #06b6d4;
}

/* Image */
img {
    border-radius: 12px !important;
    margin-top: 15px;
}

/* Download box */
.file {
    margin-top: 10px;
}
"""
) as demo:

    gr.Markdown("<div id='title'>🚀 AI Image Studio</div>")
    gr.Markdown("<div id='subtitle'>Turn your imagination into reality</div>")

    with gr.Column(elem_id="card"):

        prompt = gr.Textbox(
            placeholder="Describe your image...",
            lines=3
        )

        btn = gr.Button("Generate")

        output = gr.Image(type="filepath", label="Generated Image")

        download = gr.File(label="⬇ Download Image")

    def generate_and_download(prompt):
        img_path = generate_image(prompt)
        return img_path, img_path

    btn.click(
        fn=generate_and_download,
        inputs=prompt,
        outputs=[output, download]
    )

demo.launch()


