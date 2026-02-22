# Email_Spam_Classifier

A Machine Learning project to classify emails as spam or ham (not spam) using Python. This project demonstrates text preprocessing, feature extraction with CountVectorizer, training Multinomial Naive Bayes, and comparing its performance with other models like Logistic Regression and Support Vector Machines (SVM) after training and testing. The classifier is deployed as an interactive web app using Streamlit.

## Dataset Used

The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged being ham (legitimate) or spam.The files contain one message per line. Each line is composed by two columns: v1 contains the label (ham or spam) and v2 contains the raw text.

## Model Performance Comparison

| Model                 | Accuracy  | Precision | Recall   |
|-----------------------|-----------|-----------|----------|
| Multinomial NB        | 0.975822  | 0.900000  | 0.931034 |
| Logistic Regression   | 0.976789  | 0.991870  | 0.841379 |
| SVM                   | 0.980658  | 0.984496  | 0.875862 |

**Note:** SVM shows the highest accuracy, while Logistic Regression has the best precision.

## Frontend
The frontend of the Email Spam Classification Model is built using Streamlit, providing a clean, interactive, and responsive user interface(UI). Users can input any text from an email/a message and model predicts whether it is spam or not.

Here is the Screenshot of the interface:
<img width="1918" height="852" alt="Screenshot 2026-02-15 200553" src="https://github.com/user-attachments/assets/bf17ea6a-3b72-4597-b6e3-ef1c3ce5c9a6" />


The application is deployed using Streamlit Community Cloud, allowing real-time interaction through a public web URL.

https://saksham-email-spam-classifier.streamlit.app/


##  Tech Stack Used

- **Programming Language:** Python  
- **Libraries & Tools:** Pandas, NumPy, Scikit-learn, Pickle, Matplotlib, Seaborn
- **Frontend:** Streamlit  
- **IDE:** Jupyter Notebook, PyCharm
