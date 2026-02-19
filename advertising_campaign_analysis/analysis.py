import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8')


#----------------------------------------------------------------------
np.random.seed(42)

n = 300

data = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=n),
    "channel": np.random.choice(["Google", "Facebook", "Display", "Direct"], n),
    "impressions": np.random.randint(10000, 100000, n),
})

data["clicks"] = (data["impressions"] * np.random.uniform(0.01, 0.08, n)).astype(int)
data["cost"] = data["clicks"] * np.random.uniform(0.5, 2.5, n)
data["conversions"] = (data["clicks"] * np.random.uniform(0.02, 0.15, n)).astype(int)
data["revenue"] = data["conversions"] * np.random.uniform(50, 300, n)


#----------------------------------------------------------------------
data["CTR"] = data["clicks"] / data["impressions"]
data["CPC"] = data["cost"] / data["clicks"]
data["Conversion_Rate"] = data["conversions"] / data["clicks"]
data["ROAS"] = data["revenue"] / data["cost"]


#----------------------------------------------------------------------
channel_summary = data.groupby("channel")[["CTR", "CPC", "Conversion_Rate", "ROAS", "revenue"]].mean()

print("\n=== Średnie KPI per kanał ===")
print(channel_summary)


#----------------------------------------------------------------------
revenue_by_channel = data.groupby("channel")["revenue"].sum()

plt.figure()
revenue_by_channel.plot(kind="bar")
plt.title("Total Revenue by Channel")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_by_channel.png")
plt.close()


#----------------------------------------------------------------------
plt.figure()
data.groupby("channel")["ROAS"].mean().plot(kind="bar")
plt.title("Average ROAS by Channel")
plt.ylabel("ROAS")
plt.tight_layout()
plt.savefig("roas_by_channel.png")
plt.close()


#----------------------------------------------------------------------
plt.figure()
correlation = data[["impressions", "clicks", "cost", "conversions", "revenue"]].corr()
sns.heatmap(correlation, annot=True)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
plt.close()
