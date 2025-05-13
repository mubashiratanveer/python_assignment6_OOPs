
class logged:

    def __init__(self):
        print("Logger created: Starting logging session.")

    def __del__(self):
        print("Logger destroyed: Ending logging session.")

log = logged()

del log