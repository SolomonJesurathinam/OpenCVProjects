from io import BytesIO, BufferedReader
import streamlit as st
import CartoonifyImage
import numpy as np
import cv2
import PencilSketch
import ImageColorization

st.title("Open CV Projects")

def Catroonify():
    cartoon = CartoonifyImage.output(cv2_img, blur=blur, edge=edge, bFilter=bFilter)
    color_img = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
    st.image(color_img)
    # Download button
    download(color_img,"cartoonify")

def download(img,imgname):
    im_rgb = img[:, :, [2, 1, 0]]  # numpy.ndarray
    ret, img_enco = cv2.imencode(".png", im_rgb)  # numpy.ndarray
    srt_enco = img_enco.tobytes()  # bytes
    img_BytesIO = BytesIO(srt_enco)  # _io.BytesIO
    img_BufferedReader = BufferedReader(img_BytesIO)  # _io.BufferedReader
    st.download_button(label="Download", data=img_BufferedReader, file_name=imgname+".png", mime="image/png")

def load_img():
    image = st.file_uploader("Upload a picture")
    if image is not None:
        bytes_data = image.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
        return cv2_img


radio_checker = st.radio(label="Projects",options=("Colorize B/W","Cartoonify Image","Pencil Sketch"))
if radio_checker == "Cartoonify Image":
    cv2_img = load_img()
    if cv2_img is not None:
        st.image(CartoonifyImage.resize_func(cv2_img))
        st.success("Play around with the parameters to find the right combination")
        blur = st.slider("blur",min_value=1,max_value=21,step=2,value=3)
        edge = st.slider("edge",min_value=3,max_value=21,step=2,value=9)
        bFilter = st.slider("bFilter",min_value=1,max_value=21,step=2,value=5)
        Catroonify()

if radio_checker == "Pencil Sketch":
    cv2_img = load_img()
    if cv2_img is not None:
        st.image(CartoonifyImage.resize_func(cv2_img))
        blur = st.slider("blurValue",min_value=3,max_value=301,step=2,value=21)
        pencil= PencilSketch.PencilnBlack(cv2_img,blurValue=blur)
        color_img = cv2.cvtColor(pencil, cv2.COLOR_BGR2RGB)
        st.image(color_img)
        download(color_img,"pencilSketch")

if radio_checker == "Colorize B/W":
    cv2_img = load_img()
    if cv2_img is not None:
        st.image(cv2_img)
        LightnessValue = st.slider("Lightness Value",min_value=28,max_value=80,value=50,help="Tune the value based on your preference")
        colorized = ImageColorization.ImageFunction(cv2_img,LightnessValue)
        colorized = cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB)
        st.image(colorized)
        download(colorized,"colorized")