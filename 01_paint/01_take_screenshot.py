from robocorp import windows
from time import sleep
from PIL import ImageGrab, ImageDraw

paint = windows.find_window('executable:mspaint.exe')
print("sleeping 5 secs")
sleep(5)
elements = paint.find_many("control:ButtonControl", search_strategy="all")
len(elements)

visible_elements = [b for b in elements if b.ui_automation_control.GetClickablePoint()[2]]

screenshot = ImageGrab.grab()
screenshot_1 = ImageDraw.Draw(screenshot)

for b in elements:
    cp = b.ui_automation_control.GetClickablePoint()
    if cp[2]:
        if cp[0]==b.xcenter and cp[1]==b.ycenter:
            screenshot_1.rectangle(b.rectangle, outline ="blue")
        else:
            screenshot_1.rectangle(b.rectangle, outline ="yellow")
    else:
        pass
        #screenshot_1.rectangle(b.rectangle, outline ="red")

screenshot.save("01_image.png") 
screenshot.close()