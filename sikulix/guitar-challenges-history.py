#App.open("Yousician Launcher.app")
#wait("png/home.png", 60)
App.focus("Yousician")
click("png/settings.png")
wait("png/guitar.png")
click("png/guitar.png")
wait("png/challenges.png")
click("png/challenges.png")
wait("png/history.png")
click("png/history.png")
wait(1)
click(Location(700, 400))
wait(1)
print(Region(100,100,1266,100).text())
print(Region(457,231,647,516).text())
print(Region(1260,250,80,500).text())
App.focus("Firefox")
