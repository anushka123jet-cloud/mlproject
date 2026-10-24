# 🎓 EduPredict AI

### An End-to-End Machine Learning Application for Predicting Student Mathematics Performance

## 📌 Overview

**Student Exam Performance Indicator** is a machine learning project that predicts a student's mathematics score based on demographic, educational, and academic performance features.

The application takes user inputs such as gender, ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score. It processes the inputs using a trained machine learning pipeline and displays the predicted mathematics score through a Flask web application.

The project demonstrates an end-to-end machine learning workflow, from data preprocessing and model training to prediction and web application integration.

## 🎯 Objectives

* Analyze student performance data to identify relevant predictive features.
* Perform data preprocessing and feature transformation.
* Train and evaluate multiple regression algorithms.
* Develop a reusable prediction pipeline.
* Integrate the trained model into a Flask web application.
* Generate predictions from user-provided input.

## ✨ Key Features

* **Data Preprocessing:** Prepare numerical and categorical features for machine learning.
* **Model Training:** Train and evaluate multiple regression algorithms.
* **Model Evaluation:** Compare candidate models using appropriate regression metrics.
* **Reusable Pipeline:** Separate data processing and prediction logic into modular components.
* **Flask Web Application:** Provide a user-friendly interface for entering student information.
* **Real-Time Prediction:** Generate a predicted mathematics score from the submitted inputs.
* **Exception Handling:** Organize error handling to support debugging and maintainability.

## 🛠️ Technologies Used

| Technology   | Purpose                                            |
| ------------ | -------------------------------------------------- |
| Python       | Core programming language                          |
| Pandas       | Data manipulation and analysis                     |
| NumPy        | Numerical operations                               |
| Scikit-learn | Data preprocessing, model training, and evaluation |
| Flask        | Web application and prediction interface           |
| HTML/CSS     | User interface                                     |
| Dill         | Serialization and loading of saved Python objects  |
| Git & GitHub | Version control and source code management         |

Additional libraries may be used depending on the models and components enabled in the project.

## ⚙️ Machine Learning Workflow

The project follows these steps:

1. **Data Ingestion:** Load the student performance dataset.
2. **Data Preprocessing:** Prepare numerical and categorical features.
3. **Feature Transformation:** Apply suitable transformations using a preprocessing pipeline.
4. **Model Training:** Train multiple regression models on the prepared dataset.
5. **Model Evaluation:** Compare model performance and select a suitable candidate.
6. **Model Serialization:** Save the trained model and preprocessing object for reuse.
7. **Application Integration:** Load the saved objects through the prediction pipeline.
8. **User Input:** Collect student information through the Flask web interface.
9. **Prediction:** Transform the submitted data and generate the predicted mathematics score.
10. **Result Display:** Display the prediction to the user.

### Workflow Diagram

```text
Student Performance Dataset
           |
           v
     Data Ingestion
           |
           v
    Data Preprocessing
           |
           v
     Model Training
           |
           v
     Model Evaluation
           |
           v
  Save Model and Preprocessor
           |
           v
       Flask App
           |
           v
     User Input Form
           |
           v
  Prediction Data Processing
           |
           v
   Predicted Math Score
           |
           v
     Display Result
```

## 🤖 Algorithms

The project includes candidate regression algorithms such as:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* K-Nearest Neighbors Regressor
* AdaBoost Regressor
* Gradient Boosting Regressor
* XGBoost Regressor
* CatBoost Regressor

The final model should be identified based on the actual evaluation results produced by the training pipeline.

## 📂 Project Structure

The project uses a modular structure to separate application logic, data processing, and prediction.

```text
mlproject/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   └── utils.py
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

*Note: This is an illustrative structure. Adjust the filenames and folders to match the actual files in your repository.*

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anushka123jet-cloud/mlproject.git
```

### 2. Navigate to the Project Directory

```bash
cd mlproject
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

If the Flask entry-point file is named `app.py`, run:

```bash
python app.py
```

If your entry-point file has a different name, use that filename instead.

Open the local address displayed in the terminal to access the application in your browser.

**Note:** The saved model and preprocessor files must exist at the paths expected by the application. If the repository does not contain these artifacts, follow your project's actual training procedure to generate them before running predictions.

## 🖥️ How to Use

1. Start the Flask application.
2. Open the application in your browser.
3. Enter the student's demographic and academic information.
4. Provide reading and writing scores.
5. Submit the form.
6. View the predicted mathematics score.

## 📊 Input Features

| Feature                     | Description                                          |
| --------------------------- | ---------------------------------------------------- |
| Gender                      | Student's gender                                     |
| Race/Ethnicity              | Student's ethnicity category                         |
| Parental Level of Education | Parent's highest education category                  |
| Lunch                       | Type of lunch received                               |
| Test Preparation Course     | Whether the student completed the preparation course |
| Reading Score               | Student's reading score                              |
| Writing Score               | Student's writing score                              |

**Output:** Predicted mathematics score.

## 🧠 Key Learnings

Through this project, I gained practical experience in:

* Building an end-to-end machine learning application.
* Preparing numerical and categorical data for model training.
* Implementing reusable preprocessing and prediction pipelines.
* Comparing regression algorithms.
* Saving and loading trained machine learning objects.
* Integrating machine learning models with Flask.
* Organizing Python projects into reusable modules.
* Handling exceptions and debugging application issues.

## 🔮 Future Improvements

Potential enhancements include:

* Deploying the application to a cloud platform.
* Adding model performance visualizations.
* Improving input validation and user feedback.
* Adding automated tests for preprocessing and prediction.
* Monitoring prediction performance as new data becomes available.

## 👩‍💻 Author

**Anushka Verma**

* GitHub: [anushka123jet-cloud](https://github.com/anushka123jet-cloud)
* Project Repository: [EduPredict AI](https://github.com/anushka123jet-cloud/mlproject)

---

*This project was developed for educational purposes to explore machine learning, regression, and web application integration. Predictions are estimates and should not be treated as definitive assessments of a student's abilities.*
