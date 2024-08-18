from manim import *

class HelloManim(Scene):
    def construct(self):
        # Create a text object with the content "Hello, Manim!"
        text = Text("Hello World! \n I'm so excited to use Manim!")

        # Display the text on the screen
        self.play(Write(text))

        # Wait for 2 seconds before ending the scene
        self.wait(2)
