from shotgun_api import Shotgun

print("=" * 30)
print("This is shotgun package test")
print("=" * 30)


sg = Shotgun("https://artfx.shotgunstudio.com/", "test_td", "uqtcaegzgsqzDf6ttkz%lkgfw")
proj = sg.find_one("Project", [["name", "is", "Artfx2018_pfern_TD"]])

print("Project Artfx2018_pfern_TD info : " + str(proj))
