import matplotlib.pyplot as plt

stages = [
    "Initial Deployment",
    "Successful Update",
    "Faulty Update",
    "After Rollback"
]

available_pods = [3, 3, 3, 3]

plt.figure(figsize=(10, 5))

plt.plot(
    stages,
    available_pods,
    marker="o",
    linewidth=2,
    markersize=9
)

plt.title("Application Availability During Rolling Update and Rollback")
plt.xlabel("Deployment Stages")
plt.ylabel("Healthy Available Pods")

plt.yticks([0, 1, 2, 3])
plt.ylim(0, 3.5)
plt.grid(True)

for i, value in enumerate(available_pods):
    plt.text(i, value + 0.12, str(value), ha="center")

plt.tight_layout()
plt.savefig("screenshots/09-application-availability.png", dpi=300)

print("Graph created successfully!")