from manim import *

class EMS(Scene):
    def construct(self):

        #Creates the Celestial bodies
        
        sun = Circle(radius=1)
        earth = Circle(radius=0.5)
        moon = Circle(radius=0.1)
        
        #Gives them colour,opacity and set their border width to zero
        
        sun.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        earth.set_fill(DARK_BLUE, opacity=1).set_stroke(width=0)
        moon.set_fill(GREY, opacity=1).set_stroke(width=0)
        
        #Adds the text
        
        text = Text("Earth Moon Sun Animation")

        #Plays the animation

        self.wait(2)

        self.play(Create(sun))

        self.play(Create(earth))
        self.play(Create(moon))

        self.wait(2)

        self.play(Write(text))

        self.wait(2)