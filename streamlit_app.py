import streamlit as st
from manim import *
import os

"""
# Manim on Streamlit

I'm trying to run a Streamlit app that uses Manim to render a simple animation.

"""

class ExampleOfAnimation(Scene):
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
    custom_scene = ExampleOfAnimation()

    # Create a button to run the Manim animation
    if st.button("Run Animation"):

        # Render the animation using Manim
        custom_scene.render(preview=False)


        # image_path = "/app/streamlit-example/media/images/Example_ManimCE_v0.16.0.post0.png"
        # st.image(image_path, caption="Example Image")
        # Display the rendered video using Streamlit
        # video_path = os.path.join(os.getcwd(), "media/videos/1080p60/Example.mp4")
        # st.video(video_path)
        # video_path = "/app/streamlit-example/media/images/Example_ManimCE_mp4"


if __name__ == "__main__":
    main()

