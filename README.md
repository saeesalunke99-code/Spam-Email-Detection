# Spam Email Detection

A Machine Learning project that classifies emails as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

## Features

- Detects whether an email is Spam or Ham
- Trained using the SMS Spam Collection dataset
- Text preprocessing using NLP
- Machine Learning model for prediction
- Simple Python application for testing

## Project Structure

```
Spam-Email-Detection/
│
├── data/
│   └── SMSSpamCollection
│
├── src/
│   ├── train.py
│   └── app.py
│
├── requirements.txt
├── spam_model.pkl
└── README.md
```

## Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Pickle

## Installation

1. Clone the repository

```bash
git clone https://github.com/saeesalunke99-code/Spam-Email-Detection.git
```

2. Navigate to the project folder

```bash
cd Spam-Email-Detection
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

Train the model:

```bash
python src/train.py
```

Run the application:

```bash
python src/app.py
```

## Dataset

SMS Spam Collection Dataset

## Future Improvements

- Deploy using Streamlit
- Improve model accuracy
- Add a web interface
- Deploy on Render or Hugging Face

## Author

**Saee Salunke**

GitHub: https://github.com/saeesalunke99-code
