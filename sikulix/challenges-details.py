App.focus("Yousician")
click("settings.png")
wait("guitar.png")
click("guitar.png")
wait("challenges.png")
click("challenges.png")
wait("history.png")
click("history.png")
wait(1)
for x in range(0, 5): # update range as needed
    click(Location(700, 400)) # first challenge on the page
    wait(1)
    print(Region(100,100,1266,100).text()) # challenge title
    print(Region(457,231,647,516).text()) # songs
    # levels
    print(Region(1285,270,25,30).text())
    print(Region(1285,405,25,30).text())
    print(Region(1285,545,25,30).text())
    print(Region(1285,685,25,30).text())
    click("back.png")
    wait("history.png")
    mouseMove(Location(700, 400)) # first challenge on the page
    wheel(WHEEL_UP, 53) # scroll challenges down
App.focus("Firefox") # focus on Firefox to signal the script is finished
