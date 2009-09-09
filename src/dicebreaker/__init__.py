from dicebreaker import Config, Die ,Model_SR
from dicechart import DiceChart

print Config.hr
d6 = Die(6)
Config.objective_max = 11
Config.num_min = 1
Config.num_max = 9
Config.iterations = 100

results = {}
models = []
for i in range(Config.num_min, Config.num_max):
    results[i] = []
    for j in range(Config.objective_min, Config.objective_max+1):
        m = Model_SR(d6, i, j, Config.iterations)
        m.start()
        print "objective: " + str(m.objective),
        print "    runs : " + str(m.iterations)
        #print "    result   :",
        #print m.result
        print "passes   : " + str(m.getAverage()) + " / " + str(m.num)
        print ""
        results[i].append(m.getAverage())
        models.append(m)
print Config.hr
print results

dc = DiceChart(results)
dc.download()
