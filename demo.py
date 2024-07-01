"""
-------------------------------------------------
   @File Name:     demo.py
   @Author:        Yinghao.He
   @Date:          2024/5/24
   @Description: UI for YOLOv8
-------------------------------------------------
"""
from pathlib import Path
from PIL import Image
import streamlit as st
import config
from loader import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

# setting page layout
st.set_page_config(
    page_title="Defects Detection for YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
    )

# main page heading
st.title("Defects Detectioin UI for YOLOv8")

# lobby of the UI
def main():
    # Render the readme as markdown using st.markdown.
    readme_text = st.markdown(open("README.md",encoding='utf-8').read(), unsafe_allow_html=True)
    
    st.sidebar.title("Lobby")
    mode = st.sidebar.selectbox("Choose the mode", 
                                ["Instruction", "Run the Demo"])
    if mode == "Instruction":
        st.sidebar.success("Please follow the instruction to start to train your own EBM-YOLOv8 model.")
    elif mode == "Run the Demo":
        readme_text.empty()
        runUI()


def runUI():
    # sidebar
    st.sidebar.header("YOLOv8 Model Config")

    # model options
    task_type = st.sidebar.selectbox(
        "Select Task",
        ["Detection"]
    )

    model_type = None
    if task_type == "Detection":
        model_type = st.sidebar.selectbox(
            "Select Model",
            config.DETECTION_MODEL_LIST
        )
    else:
        st.error("Currently only 'Detection' function is implemented")

    model_type = config.selectModel(model_type)
    st.sidebar.success("Select a model above..")

    model_path = ""
    if model_type:
        model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
    else:
        st.error("Please Select Model in Sidebar")

    # load trained model
    try:
        model = load_model(model_path)
    except Exception as e:
        st.error(f"Unable to load model. Please check the specified path: {model_path}")

    # image/video options
    st.sidebar.header("Image/Video Config")
    source_selectbox = st.sidebar.selectbox(
        "Select Source",
        config.SOURCES_LIST
    )

    if source_selectbox == config.SOURCES_LIST[0]: # Image
        infer_uploaded_image(model)
        # detect_example(model)
    elif source_selectbox == config.SOURCES_LIST[1]: # Video
        infer_uploaded_video(model)
    elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
        infer_uploaded_webcam(model)
    else:
        st.error("Currently only 'Image' and 'Video' source are implemented")


if __name__ == "__main__":
    main()