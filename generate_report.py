import json
import pandas as pd
import matplotlib.pyplot as plt

# Load test results
with open("test_results.json", "r") as f:
    data = json.load(f)

# Convert data into a Pandas DataFrame
df = pd.DataFrame(data)

# Count success and failures
success_count = df["success"].sum()
failure_count = len(df) - success_count

# Generate Graph
plt.figure(figsize=(8, 6))
plt.bar(["Success", "Failure"], [success_count, failure_count], color=["green", "red"])
plt.title("Flaky Test Results")
plt.ylabel("Count")
plt.grid(axis="y")

# Save Report
plt.savefig("flaky_test_report.png")
plt.show()

print(f"Successes: {success_count}, Failures: {failure_count}")
print("Report generated: flaky_test_report.png")