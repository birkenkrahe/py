import matplotlib.pyplot as plt
import seaborn as sns

test_1 = [18.17, 21, 21.5, 21.67, 23.17, 24]
test_2 = [14.17, 17.67, 17.83, 19.17, 19.5, 23]

fig, axs = plt.subplots(ncols=2, figsize=(10, 5))

sns.kdeplot(test_1, ax=axs[0])
axs[0].set_aspect('equal')

sns.kdeplot(test_2, ax=axs[1])
axs[1].set_aspect('equal')

plt.tight_layout()
plt.show()
