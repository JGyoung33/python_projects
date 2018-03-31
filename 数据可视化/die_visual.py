from die import Die
import pygal

die_1 =Die()
die_2 = Die(10)
results =[]
for num in range(50000):
    result=die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for num in range(2,max_result+1):
    frequency = results.count(num)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.title=("Results of rolling one D6 1000 times.")
hist.x_labels = []
for i in range(2,max_result+1):
    hist.x_labels.append(str(i))
hist.x_title ="Results"
hist.y_title ="Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')

