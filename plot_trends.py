import matplotlib.pyplot as plt

days = ["Day1", "Day2", "Day3", "Day4"]

avg_t1 = [146.10, 146.10, 135.46, 142.32]
avg_t2 = [104.41, 104.41, 96.79, 104.25]

plt.figure(figsize=(8,5))
plt.plot(days, avg_t1, marker="o", label="Average T1")
plt.plot(days, avg_t2, marker="o", label="Average T2")

plt.title("IBM Fez Qubit Stability Trend")
plt.xlabel("Collection Day")
plt.ylabel("Microseconds")
plt.legend()
plt.grid(True)

plt.savefig("stability_trend.png")

plt.show()