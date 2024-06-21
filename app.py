from fastcore.all import *
from fastai.vision.all import *

import gradio as gr

learn = load_learner("hat-detector-model-local.pkl")

categories = ("No hat", "Hat")

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories, map(float,probs)))

image = gr.Image(height=192,width=192)
label = gr.Label()

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label)
intf.launch(inline=False)
