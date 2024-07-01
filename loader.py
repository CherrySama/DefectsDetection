"""
-------------------------------------------------
   @File Name:     loader.py
   @Author:        Yinghao.He
   @Date:          2024/5/24
   @Description: load models or data for detection
-------------------------------------------------
"""
from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image
import tempfile
import time
import os

def _display_detected_frames(model, st_frame, image):
    """
    Description: Display the detected objects on a video frame using the YOLOv8 model.
    param: model (YOLOv8): An instance of the `YOLOv8` class containing the YOLOv8 model.
    param: st_frame (Streamlit object): A Streamlit object to display the detected video.
    param: image (numpy array): A numpy array representing the video frame.
    return: None
    """
    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720 * (9 / 16))))

    # Predict the objects in the image using YOLOv8 model
    res = model.predict(image)

    # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )


@st.cache_resource
def load_model(model_path):
    model = YOLO(model_path)
    return model


def infer_uploaded_image(model):
    """
    Execute inference for uploaded image
    :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
    :return: None
    """
    # source_img = st.sidebar.file_uploader(
    #     label="Choose an image...",
    #     type=("jpg", "jpeg", "png", 'bmp', 'webp')
    # )
    st.sidebar.title("Choose an Image...")
    choice = st.sidebar.selectbox("Detected Option",
                                  ["Example", "Upload"])
    if choice == "Example":
        images = os.listdir("./img")
        images.sort()
        source_img = st.sidebar.selectbox("Type of Defect", images)
    elif choice == "Upload":
        source_img = st.sidebar.file_uploader(
        label="Upload an image...",
        type=("jpg", "jpeg", "png", 'bmp', 'webp'))
        
    st.balloons()
    col1, col2 = st.columns(2)

    with col1:
        if source_img:
            if choice == "Example":
                uploaded_image = Image.open(os.path.join("img", source_img))
            else:
                uploaded_image = Image.open(source_img)
            # adding the uploaded image to the page with caption
            st.image(
                image=uploaded_image,
                caption="Uploaded Image",
                use_column_width=True
            )

    if source_img:
        if st.button("Execution"):
            start_time = time.time()
            with st.spinner("Running..."):
                res = model.predict(uploaded_image)
                end_time = time.time()
                execution_time = end_time - start_time
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]

                with col2:
                    st.image(res_plotted,
                             caption="Detected Image",
                             use_column_width=True)
                    try:
                        with st.expander("Detection Results"):
                            for box in boxes:
                                st.write("posision: ",box.xywh)
                    except Exception as ex:
                        st.write("No image is uploaded yet!")
                        st.write(ex)


def infer_uploaded_video(model):
    """
    Execute inference for uploaded video
    :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
    :return: None
    """
    source_video = st.sidebar.file_uploader(
        label="Choose a video..."
    )
    st.balloons()
    
    if source_video:
        st.video(source_video)

    if source_video:
        if st.button("Execution"):
            with st.spinner("Running..."):
                try:
                    tfile = tempfile.NamedTemporaryFile()
                    tfile.write(source_video.read())
                    vid_cap = cv2.VideoCapture(
                        tfile.name)
                    st_frame = st.empty()
                    while (vid_cap.isOpened()):
                        success, image = vid_cap.read()
                        if success:
                            _display_detected_frames(model,
                                                     st_frame,
                                                     image
                                                     )
                        else:
                            vid_cap.release()
                            break
                except Exception as e:
                    st.error(f"Error loading video: {e}")


def infer_uploaded_webcam(model):
    """
    Execute inference for webcam.
    :param model: An instance of the `YOLOv8` class containing the YOLOv8 model.
    :return: None
    """
    try:
        flag = st.button(
            label="Stop running"
        )
        st.balloons()
        vid_cap = cv2.VideoCapture(0)  # local camera
        st_frame = st.empty()
        while not flag:
            success, image = vid_cap.read()
            if success:
                _display_detected_frames( 
                    model,
                    st_frame,
                    image
                )
            else:
                vid_cap.release()
                break
    except Exception as e:
        st.error(f"Error loading video: {str(e)}")