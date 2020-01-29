App.focus("Yousician")
click("settings.png")
wait("guitar.png")
click("guitar.png")
wait("challenges.png")
click("challenges.png")
wait("history.png")
click("history.png")
wait(1)
for x in range(0, 1): # update range as needed
    click(Location(700, 400)) # first challenge on the page
    wait(1)
    print(Region(100,100,1266,100).text()) # challenge title
    click("back.png")
    wait("history.png")
    mouseMove(Location(700, 400)) # first challenge on the page
    wheel(WHEEL_UP, 53) # scroll challenges down
App.focus("Firefox") # focus on Firefox to signal the script is finished
