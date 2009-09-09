from pygooglechart import SimpleLineChart
from pygooglechart import Axis
import logging

class DiceChart():
    chart = None
    def __init__(self, data, iter = 0, width = 300, height = 300):
        self.chart = SimpleLineChart(width, height, y_range=(0, 10))
        legend = []
        colors = ['cc0000','00cc00','0000cc',
                  '990000','009900','000099',
                  '0099ff','FF9900',
                  '9900ff','ff0099']
        title = 'die rolls per objective'
        if iter > 0:
            title = title + " (%s samples)" % iter
        for i in data.keys():
            self.chart.add_data(data[i])
            legend.append(str(i))
        
        logging.debug(legend)
        logging.debug(colors)
        self.chart.set_colours(colors)
        self.chart.set_legend(legend)

        grid_x_amount = (100/(len(data[i])-1))
        self.chart.set_grid(grid_x_amount, 10, 5, 5)

        left_axis = range(0, 11, 1)
        left_axis[0] = ''
        self.chart.set_axis_labels(Axis.LEFT, left_axis)

        bottom_len = len(data[i])+2
        bottom_axis = range(2, bottom_len, 1)
        self.chart.set_axis_labels(Axis.BOTTOM, bottom_axis)
        
        self.chart.set_title(title)

    def download(self, name = 'dicechart.png'):
        self.chart.download(name)

if __name__ == '__main__':
    dcx = {8: [6.51, 5.33, 3.92, 2.63, 1.33, 1.16, 0.91, 0.89, 0.61, 0.38], 
           6: [4.80, 3.84, 2.82, 2.060, 1.10, 0.84, 0.77, 0.64, 0.45, 0.34], 
           7: [5.88, 4.67, 3.47, 2.17, 1.14, 1.19, 1.04, 0.77, 0.80, 0.46]}
    dc = DiceChart(dcx)
    dc.download()