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
        has a max value 
        has a min value of 1 or more
        may expand on a max value roll"""
    def __init__(self, max, min=1, expand = True):
        self.max = max
        self.min = min
        self.expand = expand
    def roll(self):
        my_roll = random.randrange(self.min, self.max+1)
        return my_roll
        

class Runner:
    config = None
    die = None
    def __init__(self, config, die):
        self.config = config
        self.die = die
    def run(self):
        results = {}
        for i in range(self.config.num_min, self.config.num_max):
            results[i] = []
            for j in range(self.config.objective_min, self.config.objective_max+1):
                m = Model_SR(self.die, i, j, self.config.iterations)
                m.start()
                print "objective: " + str(m.objective),
                print "    runs : " + str(m.iterations)
                print "passes   : " + str(m.getAverage()) + " / " + str(m.num)
                print ""
                logging.debug(m.result)
                results[i].append(m.getAverage())
        return results

    def drun(self):
        results = {}
        for i in range(0, self.config.num_max):
            print i
            m = Model_DSA(self.die, self.config.num_max, self.config.iterations)
            m.start()

class Model:
    " a default calculation model "
    dice = None
    number = 0
    objective = {}
    result = {}
    passes = {}
    iterations = 1

    def __init__(self, dice, num, obj, iter = 1):
        self.name = "Model_D" + str(dice.max) + "_N" + str(num)
        self.dice = dice
        self.number = num
        self.objective = obj
        self.iterations = iter

    def throw(self, num_dice):
        result = {}
        for num in range(num_dice):
            result[num] = self.dice.roll()
            tmp = result[num]
            if self.dice.expand == True:
                while tmp == self.dice.max:
                    tmp = self.dice.roll()
                    result[num] = result[num] + tmp
        return result

    def start(self):
        pass

    def getAverage(self):
        pass

class Model_SR:
    " a calculation model for SR"
    dice = None
    num = 0
    objective = 0
    result = {}
    passes = {}
    iterations = 1
  
    def __init__(self, dice, num, obj, iter = 1):
        self.name = "Model_D" + str(dice.max) + "_N" + str(num)
        self.dice = dice
        self.num = num
        self.objective = obj
        self.iterations = iter
    
    def throw(self, num_dice):
        #logging.debug("throwing %s dice" % str(num_dice))
        my_throws = []
        for _ in range(num_dice):
            result = self.dice.roll()
            tmp = result
            if self.dice.expand == True:
                while tmp == self.dice.max:
                    tmp = self.dice.roll()
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

class Model_DSA(Model):
    " a calculation model for DSA "

    def start(self):
        for i in range(0, self.iterations):
            logging.debug("iter: " + str(i))
            self.result[i] = self.throw(self.num)
            print "self.throw():",
            print self.result[i]
            self.passes[i] = {}
            for j in self.result[i].keys():
#                if j >= self.objective[j]:
                 self.passes[i][j] = abs(self.result[i][j]-self.objective[j])


    def getAverage(seld):
        _len = len(self.passes)
        sum = 0
        for i in self.passes.keys():
            sum += self.passes[i]
        return (float(sum) / float(_len))

