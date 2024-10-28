import numpy as np
import matplotlib.pyplot as plt

input_file = 'qpp_corr.csv'
corr_matrix = np.genfromtxt(input_file, delimiter=',')
print(corr_matrix)

qppmethods = ['NQC', 'WIG', 'Clarity', 'UEF_NQC', 'UEF_WIG', 'UEF_Clarity',
              'NeuralQPP', 'qppBERT-PL', 'DeepQPP', 'BERTQPP']

fig, ax = plt.subplots()
im = ax.imshow(corr_matrix)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(qppmethods)), labels=qppmethods)
ax.set_yticks(np.arange(len(qppmethods)), labels=qppmethods)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(qppmethods)):
    for j in range(len(qppmethods)):
        text = ax.text(j, i, corr_matrix[i, j], ha="center", va="center", color="w")

ax.set_title("Correlation b/w QPP Scores")
fig.tight_layout()
plt.show()