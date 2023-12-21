from whitenoise import WhiteNoise

from I import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root="/path/to/static/files")
application.add_files("/path/to/more/static/files", prefix="more-files/")

