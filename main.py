from plyer import notification
from time import sleep

while True:
    notification.notify(
        title = 'EYE ALERT',
        message = 'Please blink\nRest Your Eyes\nLook at a Object at 20 yards for 20 secs',
        app_name = 'Eye Protection',
        app_icon = r'C:\Users\DELL\Documents\sea\project\notification\eye.ico',
        timeout = 5,
        )
    sleep(1200)