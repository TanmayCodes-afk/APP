import numpy as np
heart_rates = np.random.randint(80, 151, 10)
print(heart_rates[0:4])

print(np.mean(heart_rates))
print(np.max(heart_rates))
print(np.min(heart_rates))


minutes = np.where(heart_rates > 120)[0]

print("Minutes where heart rate exceeded 120 bpm:", minutes)