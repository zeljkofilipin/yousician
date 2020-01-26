# settings - guitar
click("settings.png")
click("guitar.png")

# challenges - history
click("challenges.png")
click("history.png")

# scroll down
click(Location(700, 400))
wheel(WHEEL_UP, 100)

Region(0,0,1366,768).text()
