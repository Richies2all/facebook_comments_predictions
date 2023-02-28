# Facebook Comments volume Prediction

Using AutoGluon Framework to Predict AutoML Facebook Comments
 
## Business Objective

The Facebook comments volume prediction is aimed at predicting how many comments a post is expected to receive in next H
hrs. This will assist in determining the common trends in comments with most likes on Facebook in the next H hrs.

## Environment Setup
- conda create --name fbguonenv python=3.9 -y
- conda activate projfbguonenv
- pip install torch==1.13.1+cpu torchvision==0.14.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html
- pip install autogluon streamlit jupyter

- Test successful autogluon installtion on the anaconda cmd with 
 >>> python
 >>> from autogluon.tabular import TabularDataset, TabularPredictor
 >>>

- Test the streamlit installation on the cmd with "streamlit hello"

  - Please note that if the installation was successful, the streamlit application will be opened in a new tab of your default browser.
  - The info below will be shown on the cmd prompt.

  Local URL: http://localhost:8501
  Network URL: http://192.168.100.135:8501

## Project Structure
Facebook Comments Volume
|-- README.md
|-- data
|-- images
|-- models

## Data Ingestion 


## Exploratory Data Analysis (EDA)


## Features Engineering  or Processing


## Model Building


## Model Evaluation


## Model Deployment

The deployment will be done on the Streamlit.