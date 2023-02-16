'''from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))'''
    
import streamlit as st
import os
import pandas as pd
from face_detec import main_face 
from movie_rec import main_movie
from disaster_twet import main_twet
from catvsdog import main_catvsdog
from image_colorization import main_colorization

# -------------------------------------------------------------------------------------------------------------
def main():
    st.set_page_config(layout="wide")
    st.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.subheader("Select an option")
    activities = [
        "Cats vs Dogs", "Disaster Tweet Classification", "Movie Recommender", "Face Detection","Image Colorization"]
    choice = st.sidebar.selectbox("", activities)

# ------------Cats Vs Dogs ----------------------------------------------------------------

    if choice == "Cats vs Dogs":
        main_catvsdog()
# ------------------------------------------------------------------------
    if choice == "Disaster Tweet Classification":
        main_twet()

# ----------------------------------------------------------------------------------------------------------------
    if choice == "Movie Recommender":
        main_movie()
# -------------------------------------------------------------------------------
    if choice == "Face Detection": 
        main_face()
#-----------------------------------------------------------------------
    if choice == "Image Colorization":
        main_colorization()


if __name__ == '__main__':
    main()
