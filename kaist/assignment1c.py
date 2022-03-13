import random
import matplotlib.pyplot as plt

experiments = []

ntimes = 10000

for num_tries in range(1, ntimes + 1):
    experiment = {
        'tries': num_tries,
        'heads': 0,
        'tails': 0,
        'heads_ratio': 0
    }

    for t in range(0, num_tries):
        coin = random.randint(0, 1)

        if coin == 1:
            experiment['heads'] += 1
        elif coin == 0:
            experiment['tails'] += 1
    
    # compute the ratio
    experiment['heads_ratio'] = experiment['heads'] / num_tries

    experiments.append(experiment)

experiment_that_has_half_probability = None

# x axis
n = [i for i in range(1, ntimes + 1)]

# y axis
heads_ratio = []
for experiment in experiments:
  ratio = experiment['heads_ratio']

  if ratio == 0.50 and experiment_that_has_half_probability is None:
    experiment_that_has_half_probability = experiment

  heads_ratio.append(ratio)

plt.figure(figsize=(5, 5))

plt.plot(n, heads_ratio)
plt.title('Head Ratio')
plt.xlabel('Times')
plt.ylabel('Ratio')
plt.show()

print(experiment_that_has_half_probability)
