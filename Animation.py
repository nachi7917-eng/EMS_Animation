from manim import *

class EMS(Scene):
    def construct(self):

        # Creates celestial bodies
        sun = Circle(radius=0.5)
        earth = Circle(radius=0.2)
        moon = Circle(radius=0.05)
        
        #Combines earth and moon into one object
        earth_moon = VGroup(earth, moon)

        # Styling
        sun.set_fill(YELLOW, opacity=1).set_stroke(width=0)
        earth.set_fill(DARK_BLUE, opacity=1).set_stroke(width=0)
        moon.set_fill(GREY, opacity=1).set_stroke(width=0)

        # Final positions
        sun_target = ORIGIN
        earth_target = RIGHT * 3
        moon_target = RIGHT * 3.5
        
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
            run_time=3,
            rate_func= linear
        )
        t = ValueTracker(0)
        earth.add_updater(lambda m: m.move_to(
            sun.get_center() + 3 * np.array([np.cos(t.get_value()), np.sin(t.get_value()), 0])
        ))
        moon.add_updater(lambda m: m.move_to(
            earth.get_center() + 0.5*np.array([np.cos(4 * t.get_value()), np.sin(4 * t.get_value()), 0])
        ))
        self.play(t.animate.set_value(TAU), run_time=10, rate_func=linear)
        earth.clear_updaters()
        moon.clear_updaters()

        self.wait(1)

        # Title
        text = Text("Earth-Moon-Sun Animation")
        text.move_to(DOWN*2)
        self.play(Write(text))
        self.wait(2)
