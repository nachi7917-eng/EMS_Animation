'''from manim import *
import numpy as np

class EMS(Scene):
    def construct(self):
        # Create celestial bodies
        sun = Circle(radius=0.5).set_fill(YELLOW, opacity=1).set_stroke(width=0)
        earth = Circle(radius=0.2).set_fill(DARK_BLUE, opacity=1).set_stroke(width=0)
        moon = Circle(radius=0.05).set_fill(GREY, opacity=1).set_stroke(width=0)

        # Add objects
        self.play(FadeIn(sun))
        self.play(FadeIn(earth))
        self.play(FadeIn(moon))
        self.wait(1)

        # Move into position
        self.play(
            sun.animate.move_to(ORIGIN),
            earth.animate.move_to(RIGHT * 3),
            moon.animate.move_to(RIGHT * 3.5),
            run_time=3
        )

        # Angle tracker drives both orbits
        t = ValueTracker(0)

        earth_orbit_radius = 3
        moon_orbit_radius = 0.5
        moon_speed = 4  # moon orbits 4x per earth year (real value is ~13)

        earth.add_updater(lambda m: m.move_to(
            sun.get_center() + earth_orbit_radius * np.array([
                np.cos(t.get_value()), np.sin(t.get_value()), 0
            ])
        ))

        # Moon orbits wherever the earth currently is
        moon.add_updater(lambda m: m.move_to(
            earth.get_center() + moon_orbit_radius * np.array([
                np.cos(moon_speed * t.get_value()),
                np.sin(moon_speed * t.get_value()), 0
            ])
        ))

        # Animate one full earth orbit
        self.play(t.animate.set_value(TAU), run_time=10, rate_func=linear)
        #updater cleaner
        earth.clear_updaters()
        moon.clear_updaters()
        
        self.wait(1)

        # Title Animation
        text = Text("Earth-Moon-Sun Animation")
        text.move_to(DOWN * 2)
        self.play(Write(text))
        self.wait(2)'''

from manim import *

class EMS(Scene):
    def construct(self):

        # Creates celestial bodies
        sun = Circle(radius=1)
        earth = Circle(radius=0.5)
        moon = Circle(radius=0.1)
        
        #Combines earth and moon into one object
        earth_moon = VGroup(earth, moon)

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
        moon.add_updater(lambda m: m.move_to(earth.get_center() + RIGHT))
        self.play(Rotate(earth, angle=TAU, about_point=sun.get_center(), run_time=10))
        moon.clear_updaters()

        self.wait(1)

        # Title
        text = Text("Earth Moon Sun Animation")
        text.move_to(DOWN*3)
        self.play(Write(text))
        self.wait(2)