import math

# pv-> present value
# future -> future value
# r -> rate
# n -> for that year
# t -> continuous upto that year


def present_value_discrete(fv, r, n):
    return fv / (1 + r) ** n


def future_value_discrete(pv, r, n):
    return pv * (1 + r) ** n


def future_value_continuous(pv, r, t):
    return pv * math.exp(r * t)


present_value = 1000
rate = 0.05
years = 10

fv1 = future_value_discrete(present_value, rate, years)
fv2 = future_value_continuous(present_value, rate, years)
print(f"Future value with discrete model is: $ {fv1:.2f}")
print(f"Future value with continuous money is: {fv2:.2f}")
