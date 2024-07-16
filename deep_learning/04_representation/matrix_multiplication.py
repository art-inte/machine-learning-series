import manim
import numpy

class MatrixMultiplication(manim.Scene):
    left_matrix = numpy.array([[1, 2],
                   [3, 4]])
    right_matrix = numpy.array([[5, 6],
                    [7, 8]])
    
    def construct(self):
        self.camera.background_color = manim.WHITE
        if self.left_matrix.shape[1] != self.right_matrix.shape[0]:
            raise Exception('Incompatible shapes for matrix multiplication')

        left_string_matrix = self.left_matrix.astype(str)
        right_string_matrix = self.right_matrix.astype(str)

        left = manim.Matrix(left_string_matrix)
        left.set_color(manim.BLACK)
        right = manim.Matrix(right_string_matrix)
        right.set_color(manim.BLACK)
        result = manim.Matrix(left_string_matrix)
        result.set_color(manim.BLACK)

        self.organize_matrices(left, right, result)
        self.animate_product(left, right, result)

    def organize_matrices(self, left, right, result):
        equals = manim.Tex('=', color=manim.BLACK)
        everything = manim.VGroup(left, right, equals, result)
        everything.arrange()
        self.add(everything)

    def animate_product(self, left, right, result):
        pass
