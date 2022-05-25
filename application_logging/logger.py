from datetime import datetime

class App_Logger:
    def __init__(self):
        pass
    def log(self, file_object, log_message):
        self.file_object = file_object
        self.log_message = log_message
        file_object.write(
            str(datetime.now().date()) + "/" + str(datetime.now().strftime("%H:%M:%S")) + "\t\t" + self.log_message +"\n")
