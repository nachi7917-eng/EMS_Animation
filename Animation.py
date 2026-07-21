from manim import *

class EMS(Scene):
    def construct(self):

        # Creates celestial bodies
        sun = Circle(radius=1)
        earth = Circle(radius=0.5)
        moon = Circle(radius=0.1)

        # Styling
        sun.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        earth.set_fill(DARK_BLUE, opacity=1).set_stroke(width=0)
        moon.set_fill(GREY, opacity=1).set_stroke(width=0)

        # Final positions
        sun_target = ORIGIN
        earth_target = RIGHT * 4
        moon_target = RIGHT * 5
        
        # Add objects
        self.play(FadeIn((sun)))
        self.play(FadeIn((earth)))
        self.play(FadeIn((moon)))

        self.wait(1)

        # Move into position
        self.play(
            sun.animate.move_to(sun_target),
            earth.animate.move_to(earth_target),
            moon.animate.move_to(moon_target),
            run_time=3
        )
        self.play(Rotate(
            earth,
            angle=TAU,
            about_point=sun.get_center(),
            run_time=10))
        self.play(Rotate(
            moon,
            angle=TAU,
            about_point=earth.get_center(),
            run_time=10))

        self.wait(2)

        # Title
        text = Text("Earth Moon Sun Animation")
        text.move_to(DOWN*3)
        self.play(Write(text))
        self.wait(2)