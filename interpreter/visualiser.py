import pygal


class Visualiser(object):
    def __init__(self):
        print("visualiser initialized")

    def display(self):
        bar_chart = pygal.Bar()
        bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        bar_chart.render_in_browser()  # opens default web browser