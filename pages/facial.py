import numpy as np
import cv2
import streamlit as st
import json
from tensorflow import keras
from keras.models import model_from_json
from keras_preprocessing.image import img_to_array
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase


# load model
emotion_dict = {0:'angry', 1 :'happy', 2: 'neutral', 3:'sad', 4: 'surprise'}
# load json and create model
a = st.json({"class_name": "Sequential", "config": {"name": "sequential", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": [None, 48, 48, 1], "dtype": "float32", "sparse": False, "ragged": False, "name": "conv2d_input"}}, {"class_name": "Conv2D", "config": {"name": "conv2d", "trainable": True, "batch_input_shape": [None, 48, 48, 1], "dtype": "float32", "filters": 32, "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "Conv2D", "config": {"name": "conv2d_1", "trainable": True, "dtype": "float32", "filters": 64, "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "MaxPooling2D", "config": {"name": "max_pooling2d", "trainable": True, "dtype": "float32", "pool_size": [2, 2], "padding": "valid", "strides": [2, 2], "data_format": "channels_last"}}, {"class_name": "Dropout", "config": {"name": "dropout", "trainable": True, "dtype": "float32", "rate": 0.25, "noise_shape": None, "seed": None}}, {"class_name": "Conv2D", "config": {"name": "conv2d_2", "trainable": True, "dtype": "float32", "filters": 128, "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "MaxPooling2D", "config": {"name": "max_pooling2d_1", "trainable": True, "dtype": "float32", "pool_size": [2, 2], "padding": "valid", "strides": [2, 2], "data_format": "channels_last"}}, {"class_name": "Conv2D", "config": {"name": "conv2d_3", "trainable": True, "dtype": "float32", "filters": 128, "kernel_size": [3, 3], "strides": [1, 1], "padding": "valid", "data_format": "channels_last", "dilation_rate": [1, 1], "groups": 1, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "MaxPooling2D", "config": {"name": "max_pooling2d_2", "trainable": True, "dtype": "float32", "pool_size": [2, 2], "padding": "valid", "strides": [2, 2], "data_format": "channels_last"}}, {"class_name": "Dropout", "config": {"name": "dropout_1", "trainable": True, "dtype": "float32", "rate": 0.25, "noise_shape": None, "seed": None}}, {"class_name": "Flatten", "config": {"name": "flatten", "trainable": True, "dtype": "float32", "data_format": "channels_last"}}, {"class_name": "Dense", "config": {"name": "dense", "trainable": True, "dtype": "float32", "units": 1024, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "Dense", "config": {"name": "dense_1", "trainable": True, "dtype": "float32", "units": 720, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "Dropout", "config": {"name": "dropout_2", "trainable": True, "dtype": "float32", "rate": 0.5, "noise_shape": None, "seed": None}}, {"class_name": "Dense", "config": {"name": "dense_2", "trainable": True, "dtype": "float32", "units": 480, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "Dropout", "config": {"name": "dropout_3", "trainable": True, "dtype": "float32", "rate": 0.5, "noise_shape": None, "seed": None}}, {"class_name": "Dense", "config": {"name": "dense_3", "trainable": True, "dtype": "float32", "units": 240, "activation": "relu", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}, {"class_name": "Dense", "config": {"name": "dense_4", "trainable": True, "dtype": "float32", "units": 5, "activation": "softmax", "use_bias": True, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": None}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": None, "bias_regularizer": None, "activity_regularizer": None, "kernel_constraint": None, "bias_constraint": None}}]}, "keras_version": "2.6.0", "backend": "tensorflow"})
b = json.dumps(a)
classifier = model_from_json(b)

# load weights into new model
classifier.load_weights("emotion_model1.h5")

#load face
try:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
except Exception:
    st.write("Error loading cascade classifiers")

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        #image gray
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            image=img_gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img=img, pt1=(x, y), pt2=(
                x + w, y + h), color=(255, 0, 0), thickness=2)
            roi_gray = img_gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = classifier.predict(roi)[0]
                maxindex = int(np.argmax(prediction))
                finalout = emotion_dict[maxindex]
                output = str(finalout)
            label_position = (x, y)
            cv2.putText(img, output, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return img

def main():
    # Face Analysis Application #
    st.title("Real Time Face Emotion Detection Application")
    activiteis = ["Home", "Webcam Face Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activiteis)
    st.sidebar.markdown(
        """ Developed by Mohammad Juned Khan    
            Email : Mohammad.juned.z.khan@gmail.com  
            [LinkedIn] (https://www.linkedin.com/in/md-juned-khan)""")
    if choice == "Home":
        html_temp_home1 = """<div style="background-color:#6D7B8D;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Face Emotion detection application using OpenCV, Custom CNN model and Streamlit.</h4>
                                            </div>
                                            </br>"""
        st.markdown(html_temp_home1, unsafe_allow_html=True)
        st.write("""
                 The application has two functionalities.

                 1. Real time face detection using web cam feed.

                 2. Real time face emotion recognization.

                 """)
    elif choice == "Webcam Face Detection":
        st.header("Webcam Live Feed")
        st.write("Click on start to use webcam and detect your face emotion")
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

    elif choice == "About":
        st.subheader("About this app")
        html_temp_about1= """<div style="background-color:#6D7B8D;padding:10px">
                                    <h4 style="color:white;text-align:center;">
                                    Real time face emotion detection application using OpenCV, Custom Trained CNN model and Streamlit.</h4>
                                    </div>
                                    </br>"""
        st.markdown(html_temp_about1, unsafe_allow_html=True)

        html_temp4 = """
                             		<div style="background-color:#98AFC7;padding:10px">
                             		<h4 style="color:white;text-align:center;">This Application is developed by Mohammad Juned Khan using Streamlit Framework, Opencv, Tensorflow and Keras library for demonstration purpose. If you're on LinkedIn and want to connect, just click on the link in sidebar and shoot me a request. If you have any suggestion or wnat to comment just write a mail at Mohammad.juned.z.khan@gmail.com. </h4>
                             		<h4 style="color:white;text-align:center;">Thanks for Visiting</h4>
                             		</div>
                             		<br></br>
                             		<br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)

    else:
        pass


if __name__ == "__main__":
    main()
