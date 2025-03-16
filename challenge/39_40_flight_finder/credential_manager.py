class Credentials():
    def __init__(self):
        self.credentials_file = "credentials/api_credentials.cred"

    def get_credentials(self):
        api_keys = {}
        file = open(self.credentials_file, "r")
        lines = file.readlines()
        for line in lines:
            list = line.split("=")
            key = list[0].strip()
            value = list[1].strip()
            api_keys[key] = value
        return api_keys