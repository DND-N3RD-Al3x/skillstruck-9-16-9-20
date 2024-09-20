rows = input("Input a list of weather conditions (e.g., sun rain snow): ").split()

cols = ["windy", "breezy", "calm"]

result = [[f"{weather} {wind}" for wind in cols] for weather in rows]

print(result)
