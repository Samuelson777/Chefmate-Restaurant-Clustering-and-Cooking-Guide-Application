# 🍽️ ChefMate: Restaurant Clustering & Cooking Guide Application

Welcome to **ChefMate**, your intelligent culinary companion! This application clusters and recommends restaurants based on your preferences and features a chef-like chatbot to assist you in preparing delicious recipes. Whether you're looking for a new dining experience or need help in the kitchen, ChefMate has got you covered!

---

## 🌟 Features
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

- **app.py**: This is the main entry point of the application. It initializes the Streamlit web app, handles user inputs, and displays restaurant recommendations and chatbot interactions.

- **requirements.txt**: This file lists all the Python packages and dependencies required to run the application. It can be installed using pip.

- **data/**: This directory contains all datasets used in the application. The `restaurant_data.json` file includes detailed information about various restaurants, such as their names, locations, cuisines, ratings, and more.

- **models/**: This directory is dedicated to storing machine learning models. The `clustering_model.pkl` file contains the trained clustering model that groups restaurants based on similarities in user preferences.

- **scripts/**: This directory includes scripts for data preprocessing and other utility functions. 
  - **data_preprocessing.py**: This script is responsible for cleaning the raw restaurant data, handling missing values, and converting JSON data into a structured format suitable for analysis.
  - **utils.py**: This file contains various utility functions that can be used throughout the application for tasks such as data manipulation and visualization.

- **README.md**: This file provides comprehensive documentation for the project, including an overview, features, installation instructions, usage guidelines, and contribution details.

---

## 🤝 Contributing

I welcome contributions to the ChefMate project! Whether you want to report a bug, suggest a new feature, or improve the documentation, your input is valuable. Please follow the guidelines below to contribute effectively:

### How to Contribute

1. **Fork the Repository**: 
   - Click on the "Fork" button at the top right corner of the repository page to create your own copy of the project.

2. **Clone Your Fork**: 
   - Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/ChefMate.git

3. **Create a New Branch**:
   - Navigate to the project directory and create a new branch for your feature or bug fix:
   ```bash
   cd ChefMate
   git checkout -b feature/YourFeature

4. **Make Your Changes**:
   - Implement your changes in the codebase. Ensure that your code adheres to the project's coding standards and is well-documented.

5. **Test Your Changes**:
   - Run the application locally to ensure that your changes work as expected. If applicable, add unit tests to cover your new features or bug fixes.

6. **Commit Your Changes**:
   -Commit your changes with a descriptive message
   ```bash
   git commit -m 'Add some feature or fix a bug'

7. **Push to Your Branch**:
   -Push your changes to your forked repository
   ```bash
   git push origin feature/YourFeature

8. **Open a Pull Request**:
   -Go to the original repository where you want to propose your changes. Click on the "Pull Requests" tab and then click on "New Pull Request". Select your branch and submit the pull request

---

## 📧 Contact

For any inquiries, feedback, or suggestions regarding the ChefMate project, feel free to reach out to us:

- **Your Name**: [gsamuelsonguna@gmail.com]
- **GitHub**: [https://github.com/Samuelson777]

---

## 🌐 Live Demo

Check out the live demo of ChefMate here: [Live Demo](#) (link to be added once deployed).

Experience the features of ChefMate in real-time and see how it can help you find the best restaurants and assist you in cooking delicious meals!

Thank you for checking out ChefMate! We hope you enjoy using it as much as i enjoyed building it. Happy cooking! 🍳

---

## 📧 IMAGES OF APP

![Image_1](https://github.com/user-attachments/assets/86802b1b-9299-492a-955a-959e46ecaa5e)

![Image_2](https://github.com/user-attachments/assets/5bf0ac1d-61a2-4ecd-8deb-495472e0f9c2)

![Image_3](https://github.com/user-attachments/assets/1d1ad9f5-1ba3-447e-a0f2-aba2d340abe8)

![Image_4](https://github.com/user-attachments/assets/e6f392f2-8072-41c4-a996-c7a5c1c85904)

![Image_5](https://github.com/user-attachments/assets/6aed3697-9ed6-4ff9-8688-b9aad3963035)


