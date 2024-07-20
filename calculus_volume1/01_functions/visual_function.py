import matplotlib.pyplot as pyplot

if __name__ == '__main__':
    domain = [1, 2, 3]
    values = [3 - x for x in domain]

    pyplot.figure()
    pyplot.scatter(domain, values, color='blue', label='f(x) = 3 - x', zorder=5)
    line_domain = [0, 1, 2, 3, 4]
    line_values = [3 - x for x in line_domain]
    pyplot.plot(line_domain, line_values, color='gray', alpha=0.4, zorder=4)
    for (x, y) in zip(domain, values):
        pyplot.text(x, y, f'({x}, {y})', fontsize=12, ha='right')
    pyplot.legend()
    pyplot.subplots_adjust(left=0.08, right=0.92, top=0.96, bottom=0.06)
    pyplot.savefig('temp/visual_function.png', dpi=300)
    pyplot.show()
