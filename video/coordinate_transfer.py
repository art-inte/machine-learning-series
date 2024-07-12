import manim
import numpy

class CoordinateTransfer(manim.Scene):
    def __init__(self, **kwargs):
        self.new_coordinate_group = manim.VGroup()
        super().__init__(**kwargs)

    def show_axis(self):
        x_start = numpy.array([-1, 0, 0])
        x_end = numpy.array([3, 0, 0])

        y_start = numpy.array([0, -2, 0])
        y_end = numpy.array([0, 3, 0])

        x_axis = manim.Line(x_start, x_end, color=manim.GRAY)
        y_axis = manim.Line(y_start, y_end, color=manim.GRAY)

        self.add(x_axis, y_axis)
        pass
    
    def draw_blue_points(self):
        blue_points = [
            (0.5, 0.9),
            (0.5, 0.5),
            (1, 1),
            (1, 2),
            (1, 3),
            (1.5, 1.5),
            (1.6, 1.8),
            (2, 1),
            (2.2, 0.8)
        ]
        groups = manim.VGroup()
        for x, y in blue_points:
            circle = manim.Circle(radius=0.1, color=manim.BLUE)
            circle.set_fill(color=manim.BLUE, opacity=1)
            circle.move_to(numpy.array([x, y, 0]))
            groups.add(circle)
            self.new_coordinate_group.add(circle.copy())
        self.add(groups)

    def draw_red_points(self):
        red_points = [
            (1.7, 2.9),
            (2, 2.4),
            (2, 4),
            (2.2, 3),
            (2.3, 2.6),
            (2.5, 2.2),
            (2.8, 2.1),
            (3, 1.6),
            (3, 3),
            
        ]
        groups = manim.VGroup()
        for x, y in red_points:
            circle = manim.Circle(radius=0.1, color=manim.RED)
            circle.set_fill(color=manim.RED, opacity=1)
            circle.move_to(numpy.array([x, y, 0]))
            groups.add(circle)
            self.new_coordinate_group.add(circle.copy())
        self.add(groups)

    def rotate_shift_axis(self):
        x_start = numpy.array([-1, 0, 0])
        x_end = numpy.array([3, 0, 0])

        y_start = numpy.array([0, -2, 0])
        y_end = numpy.array([0, 3, 0])

        new_x_axis = manim.Line(x_start, x_end, color=manim.BLACK)
        new_y_axis = manim.Line(y_start, y_end, color=manim.BLACK)

        self.add(new_x_axis, new_y_axis)

        self.wait(1)

        self.play(
            new_x_axis.animate.rotate(manim.PI / 6, about_point=numpy.array([0, 0, 0])),
            new_y_axis.animate.rotate(manim.PI / 6, about_point=numpy.array([0, 0, 0])),
            run_time = 3)

        self.wait(2)

        self.play(
            new_x_axis.animate.shift(numpy.array([2, 2, 0])),
            new_y_axis.animate.shift(numpy.array([2, 2, 0])),
            run_time=3)
        
        self.new_coordinate_group.add(new_x_axis)
        self.new_coordinate_group.add(new_y_axis)

        self.wait(2)

    def shift_rotate_new_coordinate(self):
        self.play(
            self.new_coordinate_group.animate.rotate(-manim.PI / 6, about_point=numpy.array([2, 2, 0])),
            run_time = 3)

        self.wait(2)

        self.play(
            self.new_coordinate_group.animate.shift(numpy.array([4, -2, 0])),
            run_time=3)

        self.wait(2)

    def construct(self):
        self.camera.background_color = manim.WHITE
        self.camera.frame_center = numpy.array([4, 1.5, 0])

        self.show_axis()
        self.draw_blue_points()
        self.draw_red_points()
        self.rotate_shift_axis()
        self.shift_rotate_new_coordinate()
