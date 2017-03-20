import pygal


class Visualiser(object):
    def __init__(self):
        print("visualiser initialized")

    def display_bar(self, data_list):
        # TODO: maybe move this to parser? [(x,), (y,)] -> [x, y]
        # print("vis.data: ", data)
        # data_list = []
        # for element in data:
        #     data_list.append(element[0])
        # print("vis.data_list: ", data_list)

        bar_chart = pygal.Bar()
        # works!
        for index, element in enumerate(data_list):
            bar_chart.add('data {}'.format(index), element)
        # bar_chart.add('datas1', data_list[0])
        # bar_chart.add('datas2', data_list[1])
        bar_chart.render_in_browser()  # opens default web browser

    def display_line(self):
        line_chart = pygal.Line()
        line_chart.title = 'Browser usage evolution (in %)'
        line_chart.x_labels = map(str, range(2002, 2013))
        line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
        line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
        line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
        line_chart.render_in_browser()

    def display(self):
        line_chart = pygal.Bar()
        line_chart.title = 'Browser usage evolution (in %)'
        line_chart.x_labels = map(str, range(2002, 2013))
        line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
        line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
        line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
        line_chart.render_in_browser()
