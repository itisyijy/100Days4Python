# Day04 for 100Days4Python
# Lists -> "ORDER" exists!
# https://docs.python.org/3/tutorial/datastructures.html
# list_name = [item1, item2, item3, ... , itemN]
# list_name[X] = itemX+1, list_name[2] = item3

pl_teams = [
  "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton & Hove Albion", "Burnley",
  "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton Town", "Manchester City",
  "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United", "Tottenham Hotspur",
  "West Ham United", "Wolverhampton Wanderers"
]
print(f"\nMy team is {pl_teams[-3]}")
pl_teams.append("Ipswich Town")  # item is appended in the end
pl_teams.extend(["Leicester City", "Southampton"])  # lists are appended in the end
pl_teams.remove("Luton Town")
pl_teams.remove("Bournemouth")
pl_teams.pop(-4)
pl_teams.sort()
print(pl_teams, len(pl_teams))

# Nested List
fruits  = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]