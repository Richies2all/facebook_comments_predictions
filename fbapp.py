## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

st.title('Facebook Most Comments Prediction')

page_likes = st.number_input('How many likes per page?')
page_checkins = st.number_input('Number of checkins')
page_talkingabt = st.number_input('Number of talks')
page_category = st.number_input('Page category')
derived_feature_1 = st.slider('How many features makes the posts special_1?', 0, 100, 25)
derived_feature_2 = st.slider('How many features makes the posts special_2?', 0, 100, 25)
derived_feature_3 = st.slider('How many features makes the posts special_3?', 0, 100, 25)
derived_feature_4 = st.slider('How many features makes the posts special_4?', 0, 100, 25)
derived_feature_5 = st.slider('How many features makes the posts special_5?', 0, 100, 25)
derived_feature_7 = st.slider('How many features makes the posts special_7?', 0, 100, 25)
derived_feature_8 = st.slider('How many features makes the posts special_8?', 0, 100, 25)
derived_feature_9 = st.slider('How many features makes the posts special_9?', 0, 100, 25)
derived_feature_10 = st.slider('How many features makes the posts special_10?', 0, 100, 25)
derived_feature_12 = st.slider('How many features makes the posts special_12?', 0, 100, 25)
derived_feature_13 = st.slider('How many features makes the posts special_13?', 0, 100, 25)
derived_feature_14 = st.slider('How many features makes the posts special_14?', 0, 100, 25)
derived_feature_15 = st.slider('How many features makes the posts special_15?', 0, 100, 25)
derived_feature_17 = st.slider('How many features makes the posts special_17?', 0, 100, 25)
derived_feature_18 = st.slider('How many features makes the posts special_18?', 0, 100, 25)
derived_feature_19 = st.slider('How many features makes the posts special_19?', 0, 100, 25)
derived_feature_20 = st.slider('How many features makes the posts special_20?', 0, 100, 25)
derived_feature_21 = st.slider('How many features makes the posts special_21?', 0, 100, 25)
derived_feature_22 = st.slider('How many features makes the posts special_22?', 0, 100, 25)
derived_feature_23 = st.slider('How many features makes the posts special_23?', 0, 100, 25)
derived_feature_24 = st.slider('How many features makes the posts special_24?', 0, 100, 25)
derived_feature_25 = st.slider('How many features makes the posts special_25?', 0, 100, 25)
cc1 = st.slider('How many posts on Sunday?', 1, 50, 5)
cc2 = st.slider('How many posts on Monday?', 1, 50, 5)
cc3 = st.slider('How many posts on Tuesday?', 1, 50, 5)
cc4 = st.slider('How many posts on Wednesday?', 1, 50, 5)
cc5 = st.slider('How many posts on Thursday?', 1, 50, 5)
base_time = st.slider('At what time hrs ago comments posted', 1, 50, 5)
post_length = st.slider('Post lengths', 0, 100, 25)
post_share_cnt = st.slider('How many shares on the comments?', 0, 100, 25)
hr_local = st.slider('At what local time in hr', 1, 50, 5)
target_var = st.slider('How many target variables', 0, 100, 25)

input_data_dict = {
    "page_likes": page_likes,
    "page_checkins": page_checkins,
    "page_talkingabt": page_talkingabt,
    "page_category": page_category,
    "derived_feature_1": derived_feature_1,
    "derived_feature_2": derived_feature_2,
    "derived_feature_3": derived_feature_3,
    "derived_feature_4": derived_feature_4,
    "derived_feature_5": derived_feature_5,
    "derived_feature_7": derived_feature_7,
    "derived_feature_8": derived_feature_8,
    "derived_feature_9": derived_feature_9,
    "derived_feature_10": derived_feature_10,
    "derived_feature_12": derived_feature_12,
    "derived_feature_13": derived_feature_13,
    "derived_feature_14": derived_feature_14,
    "derived_feature_15": derived_feature_15,
    "derived_feature_17": derived_feature_17,
    "derived_feature_18": derived_feature_18,
    "derived_feature_19": derived_feature_19,
    "derived_feature_20": derived_feature_20,
    "derived_feature_21": derived_feature_21,
    "derived_feature_22": derived_feature_22,
    "derived_feature_23": derived_feature_23,
    "derived_feature_24": derived_feature_24,
    "derived_feature_25": derived_feature_25,
    "cc1": cc1,
    "cc2": cc2,
    "cc3": cc3,
    "cc4": cc4,
    "cc5": cc5,
    "base_time": base_time,
    "post_length": post_length,
    "post_share_cnt": post_share_cnt,
    "hr_local": hr_local,
    "target_var": target_var,

}

st.write(input_data_dict)

input_data = pd.DataFrame([input_data_dict])

st.write(input_data)

save_path = "model"

save_model_predictor = TabularPredictor.load(save_path)

submit = st.button("CLICK TO PREDICT NUMBER OF COMMENTS")

if submit:
    number_of_comments = save_model_predictor.predict(input_data)[0]
    st.write(f"The facebook comments prediction is : {number_of_comments}")