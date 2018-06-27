#coding=utf-8
import pygal
from die import Die

die=Die()

results=[]
for roll_num  in range(1000):
    result=die.roll()
    results.append(result)

f=[]
for value in range(1,die.num_sides):
    fr=results.count(value)
    f.append(fr)

line_chart= pygal.Bar()

line_chart.title = 'Browser usage evolution'
line_chart.x_labels = [1,2,3,4,5,6]
line_chart.x_title="Result"
line_chart.y_title="Frequency of Result"
line_chart.add("D6",f)
line_chart.render_to_file("die.svg")