from manim import *

class EMS(Scene):
    def construct(self):

        sun = Circle(radius=3)
        earth = Circle(radius=0.5)
        moon = Circle(radius=0.1)

        text = Text("Earth Moon Sun Animation")

        self.wait(2)

        self.play(Create(sun))
        self.play(Create(earth))
        self.play(Create(moon))

        self.wait(2)

        self.play(Write(text))

        self.wait(2)