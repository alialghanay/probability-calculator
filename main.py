import experiment
from Hat import Hat

hat = Hat(yellow=3, blue=2, green=6)
probability = experiment.experiment(hat=hat, expected_balls={"yellow": 2, "blue": 1}, num_balls_drawn=5, num_experiments=1000)
print("Probability:", probability)
