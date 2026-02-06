class LoginButton:
    def __init__(self):
        self.label = "Login"
        self.enabled = True

    def get_label(self):
        return self.label

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def is_enabled(self):
        return self.enabled
