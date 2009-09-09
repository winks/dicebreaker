from dicebreaker import Model
from dicebreaker import Model_SR
from dicebreaker import Runner
from dicebreaker import Config

class C_Mock:
    num_min = 1
    num_max = 2
    objective_min = 3
    objective_max = 3
    iterations = 1
    hr = "---"

class D_Mock:
    min = 3
    max = 3
    expand = False
    def roll(self):
        return 3

dmock = D_Mock()
cmock = C_Mock()

m = Model(dmock, 1, 1)

print dmock.roll()
assert dmock.roll() == 3, "dmock.roll()"

print m.name
assert m.name == "Model_D3_N1", "m.name"


fix_1 = {0:3}
fix_2 = {0:3, 1:3}

t = m.throw(1)
print t
assert t == fix_1, "throw(1)"

t = m.throw(2)
print t
assert t == fix_2, "throw(1)"

print cmock.hr

n1 = Model_SR(dmock, 1, 1)
print n1.name
assert n1.name == "Model_D3_N1", "n1.name"

n2 = Model_SR(dmock, 2, 1)
print n2.name
assert n2.name == "Model_D3_N2", "n2.name"

fix_1 = [3]
fix_2 = [3,3]

t1 = n1.throw(1)
print t1
assert t1 == fix_1, "n1.throw(1)"

t2 = n2.throw(2)
print t2
assert t2 == fix_2, "n2.throw(2)"


rr_fix_1 = {1:[1.0]}
rr_fix_2 = {1:[1.0]}

r = Runner(cmock, dmock)
#print r

rr = r.run()
print rr
assert rr == rr_fix_1, "r.run()"
