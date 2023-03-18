from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
from manim import *
import os
import subprocess
import time

"""
# Welcome to Manim+AI!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

"""

config['format'] = "mp4"

class Example(Scene):
    def construct(self):
        circle = Circle(color=WHITE)
        square = Square(color=BLUE)

        self.play(Create(circle))
        self.wait()

        self.play(Transform(circle, square))
        self.wait()

        self.play(FadeOut(square))
        self.wait()


# Define the Streamlit app
def main():
    st.title("Basic Manim Animation")

    # Create a button to run the Manim animation
    if st.button("Run Animation"):
        # Render the animation using Manim
        scene = Example()
        scene.render()

        # Wait 1000 seconds an list the files in the media directory

        # image_path = "/app/streamlit-example/media/images/Example_ManimCE_v0.16.0.post0.png"
        # st.image(image_path, caption="Example Image")

        # Display the rendered video using Streamlit
        # video_path = os.path.join(os.getcwd(), "media/videos/Example.mp4")
        # st.video(video_path)


if __name__ == "__main__":
    main()

# with st.echo(code_location='below'):
    # total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    # num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    # Point = namedtuple('Point', 'x y')
    # data = []

    # points_per_turn = total_points / num_turns

    # for curr_point_num in range(total_points):
    # curr_turn, i = divmod(curr_point_num, points_per_turn)
    # angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
    # radius = curr_point_num / total_points
    # x = radius * math.cos(angle)
    # y = radius * math.sin(angle)
    # data.append(Point(x, y))

    # st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
    # .mark_circle(color='#0068c9', opacity=0.5)
    # .encode(x='x:Q', y='y:Q'))
