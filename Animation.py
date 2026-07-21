from manim import *

class EMS(Scene):
    def construct(self):
        text = Text("Earth Moon Sun Animation")
        self.play(Write(text))
        self.wait(2)