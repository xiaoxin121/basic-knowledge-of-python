import uiautomator2 as ui
d=ui.connect_usb("AJ5KUT2B10007244")
d.app_start('com.taobao.idlefish' , '.ui.LauncherUI') # app 和 活动