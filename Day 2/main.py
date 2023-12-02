with open("data.txt") as file:
    lines = [line.rstrip() for line in file]

totalLimits = {"red": 12, "green": 13, "blue": 14}

possibleGames = []
powerSum = []

for line in lines:
    gameId, results = line.split(": ")
    gameNumber = int(gameId.split()[1])
    games = results.split("; ")

    maxCounts = {color: 0 for color in totalLimits}
    for game in games:
        counts = {color: int(count) for count, color in (pair.split(" ") for pair in game.split(", "))}
        maxCounts["red"] = max(counts.get("red", 0), maxCounts["red"])
        maxCounts["green"] = max(counts.get("green", 0), maxCounts["green"])
        maxCounts["blue"] = max(counts.get("blue", 0), maxCounts["blue"])

    if all(maxCounts[color] <= totalLimits[color] for color in totalLimits):
        possibleGames.append(gameNumber)

    powerSum.append(maxCounts["blue"] * maxCounts["green"] * maxCounts["red"])

print("Possible games:", sum(possibleGames))
print("Power sum:", sum(powerSum))
