import random
def estimate_pi(n):
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            inside_circle += 1
    pi_approx = 4 * inside_circle / n
    return pi_approx

n = int(input("Enter the number of random points to generate: "))
pi_value = estimate_pi(n)
print(f"Approximated value of pi: {pi_value}")