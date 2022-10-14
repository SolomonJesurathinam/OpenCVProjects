from io import BytesIO, BufferedReader
import streamlit as st
import CartoonifyImage
import numpy as np
import cv2
import PencilSketch

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
    srt_enco = img_enco.tostring()  # bytes
    img_BytesIO = BytesIO(srt_enco)  # _io.BytesIO
    img_BufferedReader = BufferedReader(img_BytesIO)  # _io.BufferedReader
    st.download_button(label="Download", data=img_BufferedReader, file_name=imgname+".png", mime="image/png")

radio_checker = st.radio(label="Projects",options=("Cartoonify Image","Pencil Sketch"))

if radio_checker == "Cartoonify Image":
    image = st.file_uploader("Upload a picture")
    if image is not None:
        bytes_data = image.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
        st.image(CartoonifyImage.resize_func(cv2_img))
        st.success("Play around with the parameters to find the right combination")
        blur = st.slider("blur",min_value=1,max_value=21,step=2,value=3)
        edge = st.slider("edge",min_value=3,max_value=21,step=2,value=9)
        bFilter = st.slider("bFilter",min_value=1,max_value=21,step=2,value=5)
        Catroonify()

if radio_checker == "Pencil Sketch":
    image = st.file_uploader("Upload a picture")
    if image is not None:
        bytes_data = image.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
        st.image(CartoonifyImage.resize_func(cv2_img))
        blur = st.slider("blurValue",min_value=3,max_value=301,step=2,value=21)
        pencil= PencilSketch.PencilnBlack(cv2_img,blurValue=blur)
        color_img = cv2.cvtColor(pencil, cv2.COLOR_BGR2RGB)
        st.image(color_img)
        download(color_img,"pencilSketch")