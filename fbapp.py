## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

st.title('Facebook Most Comments Prediction')

page_likes = st.slider('How many likes per page?', 0, 100, 5)
page_checkins = st.slider('Number of checkins', 0, 100, 5)
page_talkingabt = st.slider('Number of talks', 0, 100, 5)
page_category = st.slider('Page category', 0, 100, 5)
derived_feat_1 = st.slider('How many features makes the posts special_1?', 0, 100, 5)
derived_feat_2 = st.slider('How many features makes the posts special_2?', 0, 100, 5)
derived_feat_3 = st.slider('How many features makes the posts special_3?', 0, 100, 5)
derived_feat_4 = st.slider('How many features makes the posts special_4?', 0, 100, 5)
derived_feat_5 = st.slider('How many features makes the posts special_5?', 0, 100, 5)
derived_feat_6 = st.slider('How many features makes the posts special_6?', 0, 100, 5)
derived_feat_7 = st.slider('How many features makes the posts special_7?', 0, 100, 5)
derived_feat_8 = st.slider('How many features makes the posts special_8?', 0, 100, 5)
derived_feat_9 = st.slider('How many features makes the posts special_9?', 0, 100, 5)
derived_feat_10 = st.slider('How many features makes the posts special_10?', 0, 100, 5)
derived_feat_12 = st.slider('How many features makes the posts special_12?', 0, 100, 5)
derived_feat_13 = st.slider('How many features makes the posts special_13?', 0, 100, 5)
derived_feat_14 = st.slider('How many features makes the posts special_14?', 0, 100, 5)
derived_feat_15 = st.slider('How many features makes the posts special_15?', 0, 100, 5)
derived_feat_16 = st.slider('How many features makes the posts special_16?', 0, 100, 5)
derived_feat_17 = st.slider('How many features makes the posts special_17?', 0, 100, 5)
derived_feat_18 = st.slider('How many features makes the posts special_18?', 0, 100, 5)
derived_feat_19 = st.slider('How many features makes the posts special_19?', 0, 100, 5)
derived_feat_20 = st.slider('How many features makes the posts special_20?', 0, 100, 5)
derived_feat_21 = st.slider('How many features makes the posts special_21?', 0, 100, 5)
derived_feat_22 = st.slider('How many features makes the posts special_22?', 0, 100, 5)
derived_feat_23 = st.slider('How many features makes the posts special_23?', 0, 100, 5)
derived_feat_24 = st.slider('How many features makes the posts special_24?', 0, 100, 5)
derived_feat_25 = st.slider('How many features makes the posts special_25?', 0, 100, 5)
cc1 = st.slider('The total number of comments before selected base date/time?', 1, 100, 5)
cc2 = st.slider('The number of comments in last 24 hours, relative to base date/time?', 1, 100, 5)
cc3 = st.slider('The number of comments in last 48 to last 24 hours relative to base date/time?', 1, 100, 5)
cc4 = st.slider('The number of comments in the first 24 hours after the publication of post but before base date/time?', 1, 100, 5)
cc5 = st.slider('The difference between CC2 and CC3?', 1, 100, 5)
base_time = st.slider('At what time hrs ago comments posted', 1, 50, 5)
post_length = st.slider('Post lengths', 0, 100, 5)
post_share_cnt = st.slider('How many shares on the comments?', 0, 100, 5)
post_promo_status = st.slider('Number of promoted posts?', 0, 100,5)
post_pub_sun = st.slider('Number of posts on Sunday?', 0, 100, 5)
post_pub_mon = st.slider('Number of posts on Monday?', 0, 100, 5)
post_pub_tue = st.slider('Number of posts on Tuesday?', 0, 100, 5)
post_pub_wed = st.slider('Number of posts on Wednesday?', 0, 100, 5)
post_pub_thur = st.slider('Number of posts on Thursday?', 0, 100, 5)
post_pub_fri = st.slider('Number of posts on Friday?', 0, 100, 5)
post_pub_sat = st.slider('Number of posts on Saturday?', 0, 100, 5)
hr_local = st.slider('At what local time in hr', 1, 50, 5)
base_datetim_sun = st.slider('Selected base time on Sunday', 1, 50, 5)
base_datetim_mon = st.slider('Selected base time on Monday', 1, 50, 5)
base_datetim_tue = st.slider('Selected base time on Tuesday', 1, 50, 5)
base_datetim_wed = st.slider('Selected base time on Wednesday', 1, 50, 5)
base_datetim_thur = st.slider('Selected base time on Thursday', 1, 50, 5)
base_datetim_fri = st.slider('Selected base time on Friday', 1, 50, 5)
base_datetim_sat = st.slider('Selected base time on Saturday', 1, 50, 5)
target_var = st.slider('How many target variables', 0, 100, 5)

input_data_dict = {
    "page_likes": page_likes,
    "page_checkins": page_checkins,
    "page_talkingabt": page_talkingabt,
    "page_category": page_category,
    "derived_feat_1": derived_feat_1,
    "derived_feat_2": derived_feat_2,
    "derived_feat_3": derived_feat_3,
    "derived_feat_4": derived_feat_4,
    "derived_feat_5": derived_feat_5,
    "derived_feat_7": derived_feat_7,
    "derived_feat_8": derived_feat_8,
    "derived_feat_9": derived_feat_9,
    "derived_feat_10": derived_feat_10,
    "derived_feat_12": derived_feat_12,
    "derived_feat_13": derived_feat_13,
    "derived_feat_14": derived_feat_14,
    "derived_feat_15": derived_feat_15,
    "derived_feat_17": derived_feat_17,
    "derived_feat_18": derived_feat_18,
    "derived_feat_19": derived_feat_19,
    "derived_feat_20": derived_feat_20,
    "derived_feat_21": derived_feat_21,
    "derived_feat_22": derived_feat_22,
    "derived_feat_23": derived_feat_23,
    "derived_feat_24": derived_feat_24,
    "derived_feat_25": derived_feat_25,
    "cc1": cc1,
    "cc2": cc2,
    "cc3": cc3,
    "cc4": cc4,
    "cc5": cc5,
    "base_time": base_time,
    "post_length": post_length,
    "post_share_cnt": post_share_cnt,
    "post_promo_status": post_promo_status,
    "post_pub_sun": post_pub_sun,
    "post_pub_mon": post_pub_mon,
    "post_pub_tue": post_pub_tue,
    "post_pub_wed": post_pub_wed,
    "post_pub_thur": post_pub_thur,
    "post_pub_fri": post_pub_fri,
    "post_pub_sat": post_pub_sat,
    "hr_local": hr_local,
    "base_datetim_sun": base_datetim_sun,
    "base_datetim_mon": base_datetim_mon,
    "base_datetim_tue": base_datetim_tue,
    "base_datetim_wed": base_datetim_wed,
    "base_datetim_thur": base_datetim_thur,
    "base_datetim_fri": base_datetim_fri,
    "base_datetim_sat": base_datetim_sat,
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