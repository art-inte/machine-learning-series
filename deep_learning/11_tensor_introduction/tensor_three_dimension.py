import manim
import numpy
import tensorflow

class TenorThreeDimension(manim.ThreeDScene):
    def construct(self):
        self.camera.background_color = manim.WHITE
        self.set_camera_orientation(phi= 45 * manim.DEGREES, theta= 45 * manim.DEGREES)

        # There can be an arbitrary number of
        # axes (sometimes called "dimensions")
        rank_3_tensor = tensorflow.constant([
            [[0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9]],
            [[10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19]],
            [[20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29]],
        ])
        for i in range(rank_3_tensor.shape[0]):
            for j in range(rank_3_tensor.shape[1]):
                for k in range(rank_3_tensor.shape[2]):
                    cube = manim.Cube(side_length=1,
                                      fill_opacity=0.8,
                                      stroke_color=manim.BLACK,
                                      stroke_width=2)
                    cube.move_to(numpy.array([3, 0, 0]))
                    self.add(cube)
                    self.play(cube.animate.shift(numpy.array([i - 3, j + 2, k])),
                              run_time=0.4)
        self.wait()
