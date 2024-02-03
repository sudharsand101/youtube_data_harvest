import pandas as pd
import streamlit as st
df_title = pd.DataFrame()
df_title['title'] = ['project title','learner name','course','batch','institute']
df_title["name"]  = ["youtube data harvesting and warehousing","sudharsan J","datascience","d101","GUVI"]
df_title.index = range(1, len(df_title)+1)
df_title



# to read the video csv file with pandas
df = pd.read_csv(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\youtube_harvest\video_details.csv")


# to rename the column appropiately
df.rename(columns={"repeating channel name": "repeating_channel_name",
                   'video id':'video_id',
                   'video title':'video_title',
                   'published time':'published_time',
                   'video tag':'video_tag',
                   'view count':'view_count',
                   'video duration':'video_duration',
                   'video duration in sec':'video_duration_in_sec',
                   'video published year':'video_published_year',
                   'comment count':'comment_count'
                  }, inplace=True)

st.write(":orange[Q1)What are the names of all the videos and their corresponding channels?]")
#)video titles of channel - My Research Support
st.write(":blue[Q1(i)video titles of channel - My Research Support:]")
channel1_videos = df[df['repeating_channel_name'] == 'My Research Support']
channel1_videos.index = range(1, len(channel1_videos)+1) #)to change the index from 0 to 1 in the dataframe index
channel1_videos_series = channel1_videos["video_title"]
st.write(channel1_videos_series)


#)video titles of channel - All About Python
st.write(":blue[Q1(ii)video titles of channel - All About Python:]")
channel2_videos = df[df['repeating_channel_name'] == 'All About Python']
channel2_videos.index = range(1, len(channel2_videos)+1)
channel2_videos_series = channel2_videos["video_title"]
st.write(channel2_videos_series)

#)video titles of channel - techTFQ
st.write(":blue[Q1(iii)video titles of channel - techTFQ:]")
channel3_videos = df[df['repeating_channel_name'] == 'techTFQ']
channel3_videos.index = range(1, len(channel3_videos)+1)
channel3_videos_series = channel3_videos["video_title"]
st.write(channel3_videos_series)


#)video titles of channel - LearnTech
st.write(":blue[Q1(iv)video titles of channel - LearnTech:]")
channel4_videos = df[df['repeating_channel_name'] == 'LearnTech']
channel4_videos.index = range(1, len(channel4_videos)+1)
channel4_videos_series = channel4_videos["video_title"]
st.write(channel4_videos_series)


#)video titles of channel - Sounds of Isha
st.write(":blue[Q1(v)video titles of channel - Sounds of Isha:]")
channel5_videos = df[df['repeating_channel_name'] == 'Sounds of Isha']
channel5_videos.index = range(1, len(channel5_videos)+1)
channel5_videos_series = channel5_videos["video_title"]
st.write(channel5_videos_series)


#)video titles of channel - CareerFoundry
st.write(":blue[Q1(vi)video titles of channel - CareerFoundry:]")
channel6_videos = df[df['repeating_channel_name'] == 'CareerFoundry']
channel6_videos.index = range(1, len(channel6_videos)+1)
channel6_videos_series = channel6_videos["video_title"]
st.write(channel6_videos_series)


#)video titles of channel - Learn Data with Mark
st.write(":blue[Q1(vii)video titles of channel - Learn Data with Mark:]")
channel7_videos = df[df['repeating_channel_name'] == 'Learn Data with Mark']
channel7_videos.index = range(1, len(channel7_videos)+1)
channel7_videos_series = channel7_videos["video_title"]
st.write(channel7_videos_series)

#) video titles of channel - Our Future Health
st.write(":blue[Q1(viii)video titles of channel - Our Future Health:]")
channel8_videos = df[df['repeating_channel_name'] == 'Our Future Health']
channel8_videos.index = range(1, len(channel8_videos)+1)
channel8_videos_series = channel8_videos["video_title"]
st.write(channel8_videos_series)

#) titles of channel - LingaBhairavi
channel9_videos = df[df['repeating_channel_name'] == 'LingaBhairavi']
st.write(":blue[Q1(xi)video titles of channel - LingaBhairavi:]")
channel9_videos.index = range(1, len(channel9_videos)+1)
channel9_videos_series = channel9_videos["video_title"]
st.write(channel9_videos_series)

#)video titles of channel - nature videos
st.write(":blue[Q1(x)video titles of channel - nature videos:]")
channel10_videos = df[df['repeating_channel_name'] == 'Nature Videos']
channel10_videos.index = range(1, len(channel10_videos)+1)
channel10_videos_series = channel10_videos["video_title"]
st.write(channel9_videos_series)

# to show channel data in pandas
import pandas as pd
df = pd.read_csv(r"D:\Sudharsan\Guvi_Data science\DS101_Sudharsan\Mainboot camp\capstone project\youtube_harvest\channel_details.csv")
# to get list of channels
channel_name_list = df["channel_name"].tolist()

# to get list of channel videos
channel_videos_list = df["channel_videos"].tolist()





# to get maximum videos of a channel and corrosponding its channel name(Question:1)
st.write(":orange[Q2)Which channels have the most number of videos, and how many videos do they have?]")
channel_names_videos = df[['channel_name','channel_videos']]
channel_names_videos.index += 0 #)to change the index of dataframe from 0 to 1
col = 'channel_videos'
max_channel_videos = channel_names_videos.loc[channel_names_videos[col].idxmax()] #)to get the maximum number of videos in the channel list
st.write(":blue[Ans:]")
st.write(max_channel_videos)

st.write("Q.3) What are the top 10 most viewed videos and their respective channels?")
st.write("top 10 most viewed videos of channel1(My Research Support):")
channel1_videos_views = channel1_videos[["video_title","view_count"]]
channel1_videos_max_views = channel1_videos_views.nlargest(10,["view_count"])
channel1_videos_max_views.index = range(1, len(channel1_videos_max_views)+1)
channel1_videos_max_views

st.write("top 10 most viewed videos videos of channel2 (All About Python):")
channel2_videos_views = channel2_videos[["video_title","view_count"]]
channel2_videos_max_views = channel2_videos_views.nlargest(10,["view_count"])
channel2_videos_max_views.index = range(1, len(channel2_videos_max_views)+1)
channel2_videos_max_views

st.write("top 10 most viewed videos of channel3(techTFQ):")
channel3_videos_views = channel3_videos[["video_title","view_count"]]
channel3_videos_max_views = channel3_videos_views.nlargest(10,["view_count"])
channel3_videos_max_views.index = range(1, len(channel3_videos_max_views)+1)
channel3_videos_max_views

st.write("top 10 most viewed videos of channel4(LearnTech):")
channel4_videos_views = channel4_videos[["video_title","view_count"]]
channel4_videos_max_views = channel4_videos_views.nlargest(10,["view_count"])
channel4_videos_max_views.index = range(1, len(channel4_videos_max_views)+1)
channel4_videos_max_views

st.write("top 10 most viewed videos of channel5(Sounds of Isha):")
channel5_videos_views = channel5_videos[["video_title","view_count"]]
channel5_videos_max_views = channel5_videos_views.nlargest(10,["view_count"])
channel5_videos_max_views.index = range(1, len(channel5_videos_max_views)+1)
channel5_videos_max_views

st.write("top 10 most viewed videos of channel6(CareerFoundry):")
channel6_videos_views = channel6_videos[["video_title","view_count"]]
channel6_videos_max_views = channel6_videos_views.nlargest(10,["view_count"])
channel6_videos_max_views.index = range(1, len(channel6_videos_max_views)+1)
channel6_videos_max_views

st.write("top 10 most viewed videos of channel7(Learn Data with Mark):")
channel7_videos_views = channel7_videos[["video_title","view_count"]]
channel7_videos_max_views = channel7_videos_views.nlargest(10,["view_count"])
channel7_videos_max_views.index = range(1, len(channel7_videos_max_views)+1)
channel7_videos_max_views

st.write("top 10 most viewed videos of channel8(Our Future Health):")
channel8_videos_views = channel1_videos[["video_title","view_count"]]
channel8_videos_max_views = channel1_videos_views.nlargest(10,["view_count"])
channel8_videos_max_views.index = range(1, len(channel1_videos_max_views)+1)
channel8_videos_max_views

st.write("top 10 most viewed videos of channel9(LingaBhairavi):")
channel9_videos_views = channel9_videos[["video_title","view_count"]]
channel9_videos_max_views = channel9_videos_views.nlargest(10,["view_count"])
channel9_videos_max_views.index = range(1, len(channel1_videos_max_views)+1)
channel9_videos_max_views

st.write("top 10 most viewed videos of channel10(Nature Videos):")
channel10_videos_views = channel10_videos[["video_title","view_count"]]
channel10_videos_max_views = channel10_videos_views.nlargest(10,["view_count"])
channel10_videos_max_views.index = range(1, len(channel10_videos_max_views)+1)
channel10_videos_max_views

st.write(":orange[Q.4)How many comments were made on each video, and what are theircorresponding video names?]")
#comment count of channel1 videos-My Research Support videos
st.write(":blue[comment count of channel1 (My Research Support)videos]:")
channel1_videos_comments = channel1_videos[["video_title",'comment_count']]
st.write(channel1_videos_comments)

#comment count of channel2 videos-All About Python videos
st.write(":blue[comment count of channel2 (All About Python)videos:]")
channel2_videos_comments = channel2_videos[["video_title",'comment_count']]
st.write(channel2_videos_comments)

#comment count of channel3 videos-techTFQ videos
st.write(":blue[comment count of channel3 (techTFQ)videos:]")
channel3_videos_comments = channel3_videos[["video_title",'comment_count']]
st.write(channel3_videos_comments)

#comment count of channel4 videos-LearnTech
st.write(":blue[comment count of channel4 (LearnTech)videos:]")
channel4_videos_comments = channel4_videos[["video_title",'comment_count']]
st.write(channel4_videos_comments)

#comment count of channel5 videos-Sounds of Isha
st.write(":blue[comment count of channel5 (Sounds of Isha)videos:]")
channel5_videos_comments = channel5_videos[["video_title",'comment_count']]
st.write(channel5_videos_comments)

#comment count of channel6 videos-CareerFoundry
st.write(":blue[comment count of channel6 (CareerFoundry) videos:]")
channel6_videos_comments = channel6_videos[["video_title",'comment_count']]
st.write(channel6_videos_comments)

#comment count of channel7 videos-Learn Data with Mark
st.write(":blue[comment count of channel7 (Learn Data with Mark) videos:]")
channel7_videos_comments = channel7_videos[["video_title",'comment_count']]
st.write(channel7_videos_comments)

#comment count of channel8 videos-Our Future Health
st.write(":blue[comment count of channel8 (Our Future Health) videos:]")
channel8_videos_comments = channel8_videos[["video_title",'comment_count']]
st.write(channel8_videos_comments)

#comment count of channel9 videos-LingaBhairavi
st.write(":blue[comment count of channel9 (LingaBhairavi) videos:]")
channel9_videos_comments = channel9_videos[["video_title",'comment_count']]
st.write(channel9_videos_comments)

#comment count of channel10 videos-Nature Videos
st.write(":blue[comment count of channel10 (Nature Videos) videos:]")
channel10_videos_comments = channel10_videos[["video_title",'comment_count']]
st.write(channel10_videos_comments)



#likes of channel1 videos-My Research Support
st.write(":orange[Q.6)What is the total number of likes and dislikes for each video, and what aretheir corresponding video names?]")
st.write(":blue[likes of channel1 (My Research Support)videos:]")
channel1_videos_likes = channel1_videos[["video_title",'likes']]
st.write(channel1_videos_likes)

#likes of channel2 videos-All About Python
st.write(":blue[likes of channel 2 (All About Python)videos:]")
channel2_videos_likes = channel2_videos[["video_title",'likes']]
st.write(channel2_videos_likes)

#likes of channel3 videos-techTFQ
st.write(":blue[likes of channel 3 (techTFQ)videos:]")
channel3_videos_likes = channel3_videos[["video_title",'likes']]
st.write(channel3_videos_likes)

#likes of channel4 videos-LearnTech
st.write(":blue[likes of channel 4 (LearnTech) videos:]")
channel4_videos_likes = channel4_videos[["video_title",'likes']]
st.write(channel4_videos_likes)

#likes of channel5 videos-Sounds of Isha
st.write(":blue[likes of channel 5 (Sounds of Isha) videos:]")
channel5_videos_likes = channel5_videos[["video_title",'likes']]
st.write(channel5_videos_likes)

#likes of channel6 videos-CareerFoundry
st.write(":blue[likes of channel6 (CareerFoundry) videos:]")
channel6_videos_likes = channel6_videos[["video_title",'likes']]
st.write(channel6_videos_likes)

#likes of channel7 videos-Learn Data with Mark
st.write(":blue[likes of channel 7 (Learn Data with Mark) videos:]")
channel7_videos_likes = channel7_videos[["video_title",'likes']]
st.write(channel7_videos_likes)

#likes of channel8 videos-Our Future Health
st.write(":blue[likes of channel 8 (Our Future Health) videos:]")
channel8_videos_likes = channel8_videos[["video_title",'likes']]
st.write(channel8_videos_likes)

#likes of channel9 videos-LingaBhairavi
st.write(":blue[likes of channel 9 (LingaBhairavi) videos:]")
channel9_videos_likes = channel9_videos[["video_title",'likes']]
st.write(channel9_videos_likes)

#likes of channel10 videos-Nature Videos
st.write(":blue[likes of channel 10 (Nature Videos) videos:]")
channel10_videos_likes = channel10_videos[["video_title",'likes']]
st.write(channel10_videos_likes)


# to get the maximum liked video in all the channels
st.write(":orange[Q.5)Which videos have the highest number of likes, and what are theircorresponding channel names?]")

# to get the maximum liked video in channel 1-My Research Support
col = 'likes'
max_channel1_likes = channel1_videos_likes.loc[channel1_videos_likes[col].idxmax()]
max_channel1_likes_dict = max_channel1_likes.to_dict()

# to get the maximum liked video in channel 2-All About Python
col = 'likes'
max_channel2_likes = channel2_videos_likes.loc[channel2_videos_likes[col].idxmax()]
max_channel2_likes_dict = max_channel2_likes.to_dict()

# to get the maximum liked video in channel 3-techTFQ
col = 'likes'
max_channel3_likes = channel3_videos_likes.loc[channel3_videos_likes[col].idxmax()]
max_channel3_likes_dict = max_channel3_likes.to_dict()

# to get the maximum liked video in channel 4-LearnTech
col = 'likes'
max_channel4_likes = channel4_videos_likes.loc[channel4_videos_likes[col].idxmax()]
max_channel4_likes_dict = max_channel4_likes.to_dict()

# to get the maximum liked video in channel 5-Sounds of Isha
col = 'likes'
max_channel5_likes = channel5_videos_likes.loc[channel5_videos_likes[col].idxmax()]
max_channel5_likes_dict = max_channel5_likes.to_dict()

# to get the maximum liked video in channel 6-CareerFoundry
col = 'likes'
max_channel6_likes = channel6_videos_likes.loc[channel6_videos_likes[col].idxmax()]
max_channel6_likes_dict = max_channel6_likes.to_dict()

# to get the maximum liked video in channel 7-Our Future Health
col = 'likes'
max_channel7_likes = channel7_videos_likes.loc[channel7_videos_likes[col].idxmax()]
max_channel7_likes_dict = max_channel7_likes.to_dict()

# to get the maximum liked video in channel 8-LingaBhairavi
col = 'likes'
max_channel8_likes = channel8_videos_likes.loc[channel8_videos_likes[col].idxmax()]
max_channel8_likes_dict = max_channel8_likes.to_dict()


# to get the maximum liked video in channel 9-Our Future Health
col = 'likes'
max_channel9_likes = channel9_videos_likes.loc[channel9_videos_likes[col].idxmax()]
max_channel9_likes_dict = max_channel9_likes.to_dict()


# to get the maximum liked video in channel 10-Nature Videos
max_channel10_likes = channel10_videos_likes.max()
max_channel10_likes_dict = max_channel10_likes.to_dict()

# to get the maximum liked video in all the channels
st.write(":blue[Ans:]")
data_max_likes = [max_channel1_likes_dict,
       max_channel2_likes_dict,
       max_channel3_likes_dict,
       max_channel4_likes_dict,
       max_channel5_likes_dict,
       max_channel6_likes_dict,
       max_channel7_likes_dict,
       max_channel8_likes_dict,
       max_channel9_likes_dict,
       max_channel10_likes_dict
       ]
max_video_likes = pd.DataFrame(data_max_likes)
max_video_likes['corrosponding_channel_name'] = [
    'My Research Support',
    'All About Python',
    'techTFQ',
    'LearnTech',
    'Sounds of Isha',
    'CareerFoundry',
    'Learn Data with Mark',
    'Our Future Health',
    'LingaBhairavi',
    'Nature Videos'    
]
max_video_likes.index = range(1, len(max_video_likes)+1)
max_video_likes

# to get the total number of views of each channel(Question:7)
st.write(":orange[Q7)What is the total number of views for each channel, and what are their corresponding channel names?]")
channel_names_views = df[['channel_name','channel_views']]
channel_names_views.index += 1 #)to change the index of dataframe from 0 to 1
st.write(":blue[Ans:]")
st.write(channel_names_views)


# to get the channel published in 2022(Question-8)
st.write(":orange[Q8)What are the names of all the channels that have published videos in the year 2022?]")
st.write(":blue[Ans:]")

st.write(":blue[channel 1 (My Research Support) videos in 2022:]")
channel1_videos_year = channel1_videos[["video_title",'video_published_year']]
channel1_videos_2022 =channel1_videos_year[channel1_videos_year['video_published_year'] == 2022]
channel1_videos_2022.index = range(1, len(channel1_videos_2022)+1)
st.write(channel1_videos_2022)

st.write(":blue[channel 2 (All About Python) videos in 2022:]")
channel2_videos_year = channel2_videos[["video_title",'video_published_year']]
channel2_videos_2022 =channel2_videos_year[channel2_videos_year['video_published_year'] == 2022]
channel2_videos_2022.index = range(1, len(channel2_videos_2022)+1)
st.write(channel2_videos_2022)

st.write(":blue[channel 3 (techTFQ) videos in 2022:]")
channel3_videos_year = channel3_videos[["video_title",'video_published_year']]
channel3_videos_2022 =channel3_videos_year[channel3_videos_year['video_published_year'] == 2022]
channel3_videos_2022.index = range(1, len(channel3_videos_2022)+1)
st.write(channel3_videos_2022)

st.write(":blue[channel 4 (LearnTech) videos in 2022:]")
channel4_videos_year = channel4_videos[["video_title",'video_published_year']]
channel4_videos_2022 =channel4_videos_year[channel4_videos_year['video_published_year'] == 2022]
channel4_videos_2022.index = range(1, len(channel4_videos_2022)+1)
st.write(channel4_videos_2022)

st.write(":blue[channel 5 (Sounds of Isha) videos in 2022:]")
channel5_videos_year = channel5_videos[["video_title",'video_published_year']]
channel5_videos_2022 =channel5_videos_year[channel5_videos_year['video_published_year'] == 2022]
channel5_videos_2022.index = range(1, len(channel5_videos_2022)+1)
st.write(channel5_videos_2022)

st.write(":blue[channel 6 (CareerFoundry) videos in 2022:]")
channel6_videos_year = channel6_videos[["video_title",'video_published_year']]
channel6_videos_2022 =channel6_videos_year[channel6_videos_year['video_published_year'] == 2022]
channel6_videos_2022.index = range(1, len(channel6_videos_2022)+1)
st.write(channel6_videos_2022)

st.write(":blue[likes of channel 7 (Learn Data with Mark) videos in 2022:]")
channel7_videos_year = channel7_videos[["video_title",'video_published_year']]
channel7_videos_2022 =channel7_videos_year[channel7_videos_year['video_published_year'] == 2022]
channel7_videos_2022.index = range(1, len(channel7_videos_2022)+1)
st.write(channel7_videos_2022)

st.write(":blue[likes of channel 8 (Our Future Health) videos in 2022:]")
channel8_videos_year = channel8_videos[["video_title",'video_published_year']]
channel8_videos_2022 =channel8_videos_year[channel8_videos_year['video_published_year'] == 2022]
channel8_videos_2022.index = range(1, len(channel8_videos_2022)+1)
st.write(channel8_videos_2022)

st.write(":blue[likes of channel 9 (LingaBhairavi) videos in 2022:]")
channel9_videos_year = channel9_videos[["video_title",'video_published_year']]
channel9_videos_2022 =channel9_videos_year[channel9_videos_year['video_published_year'] == 2022]
channel9_videos_2022.index = range(1, len(channel9_videos_2022)+1)
st.write(channel9_videos_2022)

st.write(":blue[channel 10 (Nature Videos) videos in 2022:]")
channel10_videos_year = channel10_videos[["video_title",'video_published_year']]
channel10_videos_2022 =channel10_videos_year[channel10_videos_year['video_published_year'] == 2022]
channel10_videos_2022.index = range(1, len(channel10_videos_2022)+1)
st.write(channel10_videos_2022)

#)video avg video duration -  My Research Support
channel1_video_duration = channel1_videos['video_duration_in_sec'].mean()
channel1_video_duration = round(channel1_video_duration, 2)

#)video avg video duration -  All About Python
channel2_video_duration = channel2_videos['video_duration_in_sec'].mean()
channel2_video_duration = round(channel2_video_duration, 2)

#)video avg video duration -  techTFQ
channel3_video_duration = channel3_videos['video_duration_in_sec'].mean()
channel3_video_duration = round(channel1_video_duration, 3)

#)video avg video duration -   LearnTech
channel4_video_duration = channel4_videos['video_duration_in_sec'].mean()
channel4_video_duration = round(channel4_video_duration, 2)

#)video avg video duration-Sounds of Isha
channel5_video_duration = channel5_videos['video_duration_in_sec'].mean()
channel5_video_duration = round(channel5_video_duration, 2)

#)video avg video duration-CareerFoundry
channel6_video_duration = channel6_videos['video_duration_in_sec'].mean()
channel6_video_duration = round(channel6_video_duration, 2)

#)video avg video duration-Learn Data with Mark
channel7_video_duration = channel7_videos['video_duration_in_sec'].mean()
channel7_video_duration = round(channel7_video_duration, 2)

#)video avg video duration-Our Future Health
channel8_video_duration = channel8_videos['video_duration_in_sec'].mean()
channel8_video_duration = round(channel8_video_duration, 2)

#)video avg video duration-LingaBhairavi
channel9_video_duration = channel9_videos['video_duration_in_sec'].mean()
channel9_video_duration = round(channel9_video_duration, 2)

#)video avg video duration-Nature Videos  
channel10_video_duration = channel10_videos['video_duration_in_sec'].mean()
channel10_video_duration = round(channel10_video_duration, 2)

#)video avg video duration-all channels
avg_duration_sec = [channel1_video_duration,channel2_video_duration,channel3_video_duration,
         channel4_video_duration,channel5_video_duration,channel6_video_duration,
        channel7_video_duration,channel8_video_duration,channel9_video_duration,
        channel10_video_duration]


#)video avg video duration-all channels in dataframe
st.write(":orange[Q9) What is the average duration of all videos in each channel, and what are their corresponding channel names?]")
st.write(":blue[Ans:]")
df_avg_duration = pd.DataFrame()
df_avg_duration['channel_name_list'] = channel_name_list
df_avg_duration['avg_duration_sec'] = avg_duration_sec
df_avg_duration.index = range(1, len(df_avg_duration)+1)
df_avg_duration



st.write("Q.10)Which videos have the highest number of comments, and what are their corresponding channel names?")
col = 'comment_count'
max_channel1_comments = channel1_videos_comments.loc[channel1_videos_comments[col].idxmax()]
max_channel1_comments_dict = max_channel1_comments.to_dict()

col = 'comment_count'
max_channel2_comments = channel2_videos_comments.loc[channel2_videos_comments[col].idxmax()]
max_channel2_comments_dict = max_channel2_comments.to_dict()

col = 'comment_count'
max_channel3_comments = channel3_videos_comments.loc[channel2_videos_comments[col].idxmax()]
max_channel3_comments_dict = max_channel3_comments.to_dict()

col = 'comment_count'
max_channel4_comments = channel4_videos_comments.loc[channel4_videos_comments[col].idxmax()]
max_channel4_comments_dict = max_channel4_comments.to_dict()

col = 'comment_count'
max_channel5_comments = channel5_videos_comments.loc[channel5_videos_comments[col].idxmax()]
max_channel5_comments_dict = max_channel5_comments.to_dict()

col = 'comment_count'
max_channel6_comments = channel6_videos_comments.loc[channel6_videos_comments[col].idxmax()]
max_channel6_comments_dict = max_channel6_comments.to_dict()

col = 'comment_count'
max_channel7_comments = channel7_videos_comments.loc[channel7_videos_comments[col].idxmax()]
max_channel7_comments_dict = max_channel7_comments.to_dict()

col = 'comment_count'
max_channel8_comments = channel8_videos_comments.loc[channel8_videos_comments[col].idxmax()]
max_channel8_comments_dict = max_channel8_comments.to_dict()

col = 'comment_count'
max_channel9_comments = channel9_videos_comments.loc[channel9_videos_comments[col].idxmax()]
max_channel9_comments_dict = max_channel9_comments.to_dict()

col = 'comment_count'
max_channel10_comments = channel10_videos_comments.loc[channel10_videos_comments[col].idxmax()]
max_channel10_comments_dict = max_channel10_comments.to_dict()

data_max_comments = [max_channel1_comments_dict,
       max_channel2_comments_dict,
       max_channel3_comments_dict,
       max_channel4_comments_dict,
       max_channel5_comments_dict,
       max_channel6_comments_dict,
       max_channel7_comments_dict,
       max_channel8_comments_dict,
       max_channel9_comments_dict,
       max_channel10_comments_dict
       ]

max_video_comments = pd.DataFrame(data_max_comments)
max_video_comments['corrosponding_channel_name'] = [
    'My Research Support',
    'All About Python',
    'techTFQ',
    'LearnTech',
    'Sounds of Isha',
    'CareerFoundry',
    'Learn Data with Mark',
    'Our Future Health',
    'LingaBhairavi',
    'Nature Videos'    
]
max_video_comments.index = range(1, len(max_video_comments)+1)
max_video_comments

