import random
import time
import matplotlib.pyplot as plt

data = []

print("Simulating Environmental Data Logging...")

for i in range(20):
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(30, 80), 2)
    air_quality = random.randint(200, 500)

    print(f"Temp: {temperature}°C, Humidity: {humidity}%, Air Quality: {air_quality}")
    data.append((temperature, humidity, air_quality))
    time.sleep(1)

# Plot data
temps = [x[0] for x in data]
humid = [x[1] for x in data]
aqi = [x[2] for x in data]

plt.plot(temps, label="Temperature (°C)")
plt.plot(humid, label="Humidity (%)")
plt.plot(aqi, label="Air Quality Index")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Values")
plt.title("Simulated Environmental Monitoring Data")
plt.show()
