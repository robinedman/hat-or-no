import gradio as gr

def greet(name, intensity):
    return f"Hello there, {name}!{'!'*int(intensity)}"

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"]
)

demo.launch()