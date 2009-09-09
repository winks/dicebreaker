from dicebreaker import Config, Die, Model_SR, Runner
from dicechart import DiceChart

d6 = Die(6)
######################################
cfg = Config();
cfg.objective_max = 11
cfg.num_max = 11
cfg.iterations = 10

runner = Runner(cfg, d6)
results = runner.run()

dc = DiceChart(results, cfg.iterations)
dc.download("dice-10.png")
######################################
cfg = Config();
cfg.objective_max = 11
cfg.num_max = 11
cfg.iterations = 100

runner = Runner(cfg, d6)
results = runner.run()

dc = DiceChart(results, cfg.iterations)
dc.download("dice-100.png")
#######################################
cfg = Config();
cfg.objective_max = 11
cfg.num_max = 11
cfg.iterations = 1000

runner = Runner(cfg, d6)
results = runner.run()

dc = DiceChart(results, cfg.iterations)
dc.download("dice-1000.png")
