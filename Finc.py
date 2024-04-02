import math
# Given values
S0 = 50  # initial stock price
X = 48  # exercise price
r = 0.12  # risk-free rate
t = 0.5  # time in years
u = 60 / S0  # up factor
d = 42 / S0  # down factor

# Calculate risk-neutral probability
p = (math.exp(r * t) - d) / (u - d)

# Calculate payoffs
C_up = max(0, u * S0 - X)
C_down = max(0, d * S0 - X)

# Calculate call option value
C0 = math.exp(-r * t) * (p * C_up + (1 - p) * C_down)

print(C0)
