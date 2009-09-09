import random,logging
LOG_FILENAME = "/tmp/dicebreaker_debug.log"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

class Config:
    "config values"
    num_min = 1
    num_max = 3
    objective_min = 2
    objective_max = 4
    iterations = 10
    hr = "------------------------------"

class Die:
    """ an ordinary die. 
        has a max value, 
        a min value of 1 or more and 
        may expand on a max value roll"""
    def __init__(self, max, min=1, expand = True):
        self.max = max
        self.min = min
        self.expand = expand


class Model_SR:
    " a calculation model for SR"
    dice = None
    num = 0
    objective = 0
    result = {}
    passes = {}
    iterations = 1
  
    def __init__(self, dice, num, obj, iter = 1):
        self.name = "Model_D" + str(dice.max) + "_" + str(num) + "_" + str(obj)
        self.dice = dice
        self.num = num
        self.objective = obj
        self.iterations = iter
    
    def throw(self, num_dice):
        #logging.debug("throwing %s dice" % str(num_dice))
        my_throws = []
        for _ in range(num_dice):
            result = random.randrange(self.dice.min, self.dice.max+1)
            tmp = result
            if self.dice.expand == True:
                while tmp == self.dice.max:
                    tmp = random.randrange(self.dice.min, self.dice.max+1)
                    result = result + tmp
            #logging.debug("result: %s" % result)
            my_throws.append(result)
        return my_throws

    def start(self):
        for i in range(0, self.iterations):
            self.result[i] = self.throw(self.num)
            self.passes[i] = 0
            for j in self.result[i]:
                if j >= self.objective:
                    self.passes[i] = self.passes[i] + 1

    def getAverage(self):
        _len = len(self.passes)
        sum = 0
        dbg = ""
        for i in self.passes.keys():
            sum += self.passes[i]
            dbg = dbg + str(i) + "_"
        return (float(sum) / float(_len))
