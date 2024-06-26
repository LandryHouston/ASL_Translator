<h1 align='center'>American Sign Language (ASL) Translator</h1>

<div align='center'>

![](/media/images/amer_sign2.png)

</div>

---

<h2 align='center'>Overview</h2>

<p>
Welcome to my Capstone project repository. The focus of this project is to provide a simple way for deaf people to be able to communicate with hearing people. This project can also serve as an educational tool to help with learning basic ASL signs. I'm implementing an Image Classification model using Convolutional Neural Networks (CNNs) and integrating real-time hand detection with OpenCV and MediaPipe. This approach aims to break down communication barriers and contribute to bridging the gap between the deaf and hearing communities. The model aims to optimize for maximum accuracy to achieve an accuracy of over 95%. Additionally, I'll be creating a Streamlit and Flask app to ensure a user-friendly experience for everyone.
</p>

---

<h2 align='center'>Data Analysis</h2>

<p>
With ASL consisting of thousands of diverse static and dynamic signs, I decided to begin with a focused approach, starting small by considering the Alphabet. Our dataset consists of 174,474 images distributed across 24 classes. These classes represent all the letters of the alphabet, excluding J and Z due to being dynamic signs. The distribution of instances among the various classes is fairly even.

It should be noted that no data cleaning or image augmentation was considered necessary before model development. The dataset includes a wide array of signs that feature different positions, orientations, lighting conditions, and distances. Attempting further augmentation was found to have a negative impact on model accuracy.

The dataset can be accessed [here](https://www.kaggle.com/datasets/debashishsau/aslamerican-sign-language-aplhabet-dataset).

</p>

---

<h2 align='center'>Modeling</h2>

<p>
I created a Keras Sequential model incorporating Convolutional Neural Networks. Before constructing the model, I divided the dataset into training, validation, and test sets. The training phase was time-consuming due to the dataset's size. Despite the duration, the model exhibited remarkable performance with a Test Accuracy of 0.9919 and a Train Accuracy of 0.9996. These results signify the model's exceptional capability in accurately predicting image classes.
</p>

<div align='center'>

|            Accuracy             |            Loss             |
| :-----------------------------: | :-------------------------: |
| ![](/media/images/accuracy.png) | ![](/media/images/loss.png) |

</div>

---

<h2 align='center'>Hand Landmarks</h2>

<p>
I wanted to create a real-time translation system that utilizes someone's webcam. I was able to achieve this using MediaPipe and OpenCV. First I decided to create my dataset by collecting my own images. I created a function to help streamline this process that takes in a list of class names and captures a total of 1000 images for each class, 500 for each hand. I made the image collection process easy by displaying on-screen text with instructions. I knew that data augmentation was not needed if pictures are taken at different positions and distances so I rotated and moved my hand throughout the capture process.

</p>

<div align='center'>

![](/media/videos/data_collection.gif)

</div>

<p>

After the images were collected they were processed using MediaPipe and hand landmarks were added to the images. The landmark coordinates were saved as a pickle file.

A new classification model needed to be created for precise and quick predictions. I decided to go with my favorite, Random Forest Classifier. The model trains quickly and we get an impressive accuracy score resulting in 99.9% of samples being classified correctly. The model is also saved as a pickle for easy accessibility.

</p>

<div align='center'>

![](/media/images/landmark_image.png)

## </div>

<h2 align='center'>Web Applications</h2>

<p>

I've developed two ASL Translator web applications for a user-friendly experience. The Streamlit app allows users to upload ASL sign images, providing automatic class predictions. On the other hand, the Flask app enables real-time translations using a webcam. It recognizes hand gestures, assigns landmarks, and displays predictions near the hand, ensuring easy readability. For a prediction to be visible, the model requires a confidence level of at least 50%. If it's less confident, no prediction will be displayed.

I created videos showcasing both of the web applications, check them out [here](/media/videos/).

You can check out the code in the [Web App folder](/web_applications/).

</p>

<div align='center'>

![](/media/videos/flask_showcase.gif)

</div>

---

<h2 align='center'>Conclusions</h2>

<p>
In summary, I successfully created two advanced predictive models to enhance communication for deaf and hearing individuals, utilizing a Sequential model and a Random Forest Classifier. The Sequential model exhibited outstanding performance with a Test Accuracy of 99.19% and a Train Accuracy of 99.96%, showcasing its exceptional ability to accurately predict image classes. The Random Forest Classifier also delivered excellent results, classifying 99.9% of samples correctly. Together, these models provide highly accurate outcomes for image classification and real-time sign translation, surpassing our expectations and affirming their effectiveness in facilitating improved communication. Future improvements can be made by collecting more diverse data and expanding the range of classes. This can contribute to further improving the model's robustness and performance across a broader spectrum of scenarios.
</p>

---

<h2 align='center'>Citations</h2>

<p align='left'>
"Web Cam in a Webpage Using Flask and Python." <a href='https://stackoverflow.com/questions/54786145/web-cam-in-a-webpage-using-flask-and-python'>www.stackoverflow.com</a>, 20 Feb. 2019.<br><br>
"Sign Language Detection with Python and Scikit Learn." <a href='https://youtu.be/MJCSjXepaAM?si=KkBwTAqwPveyiTBy'>www.youtube.com</a>, uploaded by Computer Vision Engineer, 26 Jan. 2023.
</p>


Notes: 
Principle Component Analysis might help with the image pattern recognition.
