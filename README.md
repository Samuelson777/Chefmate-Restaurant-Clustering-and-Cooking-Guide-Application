# 🍽️ ChefMate: Restaurant Clustering & Cooking Guide Application

**ChefMate** is an intelligent application designed to cluster and recommend restaurants based on user preferences, such as cuisine or specific dishes. Additionally, it features a chef-like chatbot that assists users in preparing recipes, enhancing their cooking experience. This project leverages machine learning and cloud computing technologies to deliver personalized recommendations and cooking guidance

---

## 🌟 Features of app
- **Personalized Recommendations**: Get tailored restaurant suggestions based on your favorite cuisines and dishes.
- **Interactive Maps**: Explore restaurant locations with dynamic maps and ratings for an enhanced user experience.
- **Cooking Assistance**: Engage with our chatbot for step-by-step cooking instructions and tips.
- **Future Integrations**: Potential to connect with food delivery platforms for seamless ordering.

---

## 🚀 Technologies Used
- **Streamlit**: For building a user-friendly web application.
- **AWS Services**: Utilizing S3 for data storage, RDS for database management, and EC2 for deployment.
- **Machine Learning**: Implementing clustering algorithms for effective restaurant recommendations.
- **Python**: The primary programming language for development.
- **Chatbot Integration**: Enhancing user interaction with conversational AI.

---

## 🗝 Key Features of the project
- **Data Storage**: Utilized AWS S3 for storing project files and raw data.
- **Data Preprocessing**: Implemented data cleaning and preprocessing techniques to prepare the data for model training.
- **Database Management**: Connected to AWS RDS to store cleaned data for structured querying.
- **Model Training**: Trained multiple clustering models, including:
                        * KMeans
                        * DBSCAN
                        * Agglomerative Clustering
                        * Gaussian Mixture,
    The models were evaluated using the silhouette score to determine the best-performing model
- **Application Development**: Developed the ChefMate application using Streamlit to meet project requirements.
- **Chatbot integration in the app**: Used gemini generative AI role based chatbot using the API key.
- **Deployment**: Deployed the application on AWS for real-time interaction.

---

## 📦 Installation

Follow these steps to set up ChefMate on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ChefMate.git

2. **Navigate to the project directory**:
    ```bash
   cd ChefMate

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt

4. **Set up your AWS credentials and configure the necessary services (S3, RDS, EC2)**

---

## 🛠️ Usage

1. **Run the Streamlit application**:
   ```bash
   streamlit run app.py

2. **Access the application in your web browser at http://localhost:8501**

---

## 📁 Project Structure

The project is organized into the following directory structure:


### Description of Each Component:

- **ChefMate.py**: This is the main entry point of the application. It initializes the Streamlit web app, handles user inputs, and displays restaurant recommendations and chatbot interactions.

- **requirements.txt**: This file lists all the Python packages and dependencies required to run the application. It can be installed using pip.

- **ChefMate/**: This directory contains datasets used in the application. The `Zomato_cluster_data.csv` file includes detailed information about various restaurants, such as their names, locations, cuisines, ratings, and more.

- **models/**: This directory is dedicated to storing machine learning models. The `kmeans_model.pkl` file contains the trained clustering model that groups restaurants based on similarities in user preferences.

- **ChefMate/**: This directory includes scripts for data preprocessing and other utility functions. 
  - **data_preprocessing.ipynb**: This script is responsible for cleaning the raw restaurant data, handling missing values, and converting JSON data into a structured format suitable for analysis.
  - **data_cleaning.ipynb**: This file contains various utility functions that can be used throughout the application for tasks such as data manipulation and visualization.

- **README.md**: This file provides comprehensive documentation for the project, including an overview, features, installation instructions, usage guidelines, and contribution details.

---

## 📧 Contact

For any inquiries, feedback, or suggestions regarding the ChefMate project, feel free to reach out to me:

- **SAMUELSON G**: [gsamuelsonguna@gmail.com]
- **GitHub**: [https://github.com/Samuelson777]

---

## 🌐 Live Demo

Check out the live demo of ChefMate here: [Live Demo](http://65.0.177.245:8501/).

Experience the features of ChefMate in real time with this eg app and see how it can help you find the best restaurants and assist you in cooking delicious meals!

Thank you for checking out ChefMate! I hope you enjoy using it as much as i enjoyed building it. Happy cooking! 🍳

For any clarification about using the app refer the user manual pdf

---

## 📸 IMAGES OF APP

![Image_1](https://github.com/user-attachments/assets/86802b1b-9299-492a-955a-959e46ecaa5e)

![Image_2](https://github.com/user-attachments/assets/5bf0ac1d-61a2-4ecd-8deb-495472e0f9c2)

![Image_3](https://github.com/user-attachments/assets/1d1ad9f5-1ba3-447e-a0f2-aba2d340abe8)

![Image_4](https://github.com/user-attachments/assets/e6f392f2-8072-41c4-a996-c7a5c1c85904)

![Image_5](https://github.com/user-attachments/assets/6aed3697-9ed6-4ff9-8688-b9aad3963035)

---

## 💹 Challenges Faced
One of the main challenges encountered was the limited data available for unsupervised learning, which restricted the depth of analysis and model training. Despite this, the project successfully demonstrates the core functionalities.

---

## 🔮 Future Plans
The goal is to utilize this application in real-time scenarios, allowing users to receive personalized restaurant recommendations and cooking assistance.

---

## 🎯 Target Audience
The primary users of this application are individuals seeking personalized dining experiences and cooking guidance.

---

## 📝 Acknowledgments
This project was developed as part of a learning initiative to explore the integration of machine learning and cloud computing in real-world applications.
