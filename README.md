<h1 align='center'>American Sign Language (ASL) Translator</h1>

<h3 align='center'>Capstone Project for General Assembly DSI-1113</h3>

<div align='center'>

![](/images/amer_sign2.png)

</div>

---

<h2 align='center'>Overview</h2>

<p>
Welcome to my Capstone project repository. The focus of this project is to provide a simple way for deaf people to be able to communicate with hearing people. This project can also serve as an educational tool to help with learning basic ASL signs. I'm implementing an Image Classification model using Convolutional Neural Networks (CNNs) and integrating real-time hand detection with OpenCV and MediaPipe. This approach aims to break down communication barriers and contribute to bridging the gap between the deaf and hearing communities. The model aims to optimize for maximum accuracy with the goal of achieving an accuracy of over 95%. Additionally, I'll be creating a Streamlit and Flask app to ensure a user-friendly experience for everyone."
</p>

---

<h2 align='center'>Data Analysis</h2>

<p>
With ASL consisting of thousands of diverse static and dynamic signs, I decided to begin with a focused approach, starting small by considering the Alphabet. Our dataset consists of 174,474 images distributed across 24 classes. These classes represent all the letters of the alphabet, excluding J and Z due to being dynamic signs. The distribution of instances among the various classes is fairly even.

It should be noted that no data cleaning or image augmentation was deemed necessary before model development. The dataset includes a wide array of signs, featuring different positions, orientations, lighting conditions, and distances. Attempting further augmentation was found to have a negative impact on model accuracy.

</p>

---

<h2 align='center'>Modeling</h2>

<p>
I created a Keras Sequential model incorporating Convolutional Neural Networks. Before constructing the model, I divided the dataset into training, validation, and test sets. The training phase was time-consuming due to the dataset's size. Despite the duration, the model exhibited remarkable performance with a Test Accuracy of 0.9919 and a Train Accuracy of 0.9996. These results signify the model's exceptional capability in accurately predicting image classes.
</p>

|         Accuracy          |         Loss          |
| :-----------------------: | :-------------------: |
| ![](/images/accuracy.png) | ![](/images/loss.png) |

---

<h2 align='center'>Hand Landmarks</h2>

<p>
I wanted to create a real-time translation system that utilizes someones webcam. I was able to achieve this using MediaPipe and OpenCV. First I decided to create my own dataset by collecting my own images. I created a function to help streamline this process that takes in a list of class names and captures a total of 1000 images for each class, 500 for each hand. I made the image collection process easy by displaying on-screen text with instructions. I knew that data augmentation was not needed if pictures are taken at different positions and distances so I rotated and moved my hand throughout the capture process.

<div align='center'>

![](/images/landmark_image.png)

</div>

After the images were collected they were processing using MediaPipe and hand landmarks were added to the images. The landmark coordinates were saved as a pickle file.

A new classification model needed to be created for precise and quick predictions. I decided to go with my favorite, Random Forest Classifier. The model trains quickly and we get an impressive accuracy score resulting in 99.9% of samples being classified correctly. The model is also saved as a pickle for easy accessibility.

</p>

<video align='center' width="320" height="240" controls>
  <source src="/images/data_collection.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

<h2 align='center'>Web Applications</h2>

<p>
To make the ASL Translator accessible and user-friendly, I've developed a web application using Streamlit and Flask.

You can check out the live app [here](#) or explore the code in the [Web App folder](/web_applications/).

</p>
