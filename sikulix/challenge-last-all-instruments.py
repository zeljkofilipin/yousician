App.focus("Yousician")
for instrument in ["guitar", "piano", "ukulele", "bass"]:
    instrument_png = instrument + ".png"
    wait("settings.png")
    click("settings.png")
    wait(instrument_png)
    click(instrument_png)
    wait("challenges.png")
    click("challenges.png")
    print(Region(100,100,1266,100).text()) # challenge title
    print(Region(457,231,647,516).text()) # songs
    # levels
    print(Region(1285,270,25,30).text())
    print(Region(1285,405,25,30).text())
    print(Region(1285,545,25,30).text())
    print(Region(1285,685,25,30).text())
App.focus("Firefox") # focus on Firefox to signal the script is finished
