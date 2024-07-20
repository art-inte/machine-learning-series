import manim
import numpy

# manim -pql -r 3840,2160 --fps 30 video/sine_curve_unit_circle.py SineCurveUnitCircle

class SineCurveUnitCircle(manim.Scene):
    def construct(self):
        self.camera.background_color = manim.WHITE
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
    
    def show_axis(self):
        x_start = numpy.array([-6, 0 ,0])
        x_end = numpy.array([6, 0, 0])

        y_start = numpy.array([-4,-2,0])
        y_end = numpy.array([-4,2,0])

        x_axis = manim.Line(x_start, x_end, color=manim.BLACK)
        y_axis = manim.Line(y_start, y_end, color=manim.BLACK)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = numpy.array([-4,0,0])
        self.curve_start = numpy.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            manim.MathTex('0'),
            manim.MathTex('1\pi'), manim.MathTex('2\pi'),
            manim.MathTex('3\pi'), manim.MathTex('4\pi'),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(numpy.array([-3 + 2 * i, 0, 0]), manim.DOWN)
            self.add(x_labels[i])

            s_line = manim.Line([-3 + 2 * i, 0.0, 0], [-3 + 2 * i, 0.1, 0], color=manim.BLACK)
            self.add(s_line)

    def show_circle(self):
        circle = manim.Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = manim.Dot(radius=0.08, color=manim.YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return manim.Line(origin_point, dot.get_center(), color=manim.BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return manim.Line(dot.get_center(), numpy.array([x,y,0]), color=manim.YELLOW_A, stroke_width=2)

        self.curve = manim.VGroup()
        self.curve.add(manim.Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = manim.Line(last_line.get_end(), numpy.array([x,y,0]), color=manim.YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = manim.always_redraw(get_line_to_circle)
        dot_to_curve_line = manim.always_redraw(get_line_to_curve)
        sine_curve_line = manim.always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)
