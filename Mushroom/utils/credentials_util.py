import os


class CredentialsUtil:
    def __init__(self, file_path='data/credentials.txt'):
        self.file_path = os.path.join(os.getcwd(), file_path)

    def read_credentials(self):
        credentials = {}
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    credentials[key] = value
        except FileNotFoundError:
            print("Credentials file not found. Creating a new one.")
            self.save_credentials(credentials)
        return credentials

    def get_credential(self, key):
        credentials = self.read_credentials()
        return credentials.get(key)

    def add_credential(self, key, value):
        credentials = self.read_credentials()
        credentials[key] = value
        self.save_credentials(credentials)

    def remove_credential(self, key):
        credentials = self.read_credentials()
        if key in credentials:
            del credentials[key]
            self.save_credentials(credentials)
        else:
            print(f"Key '{key}' not found in credentials.")

    def save_credentials(self, credentials):
        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            with open(self.file_path, 'w') as file:
                for key, value in credentials.items():
                    file.write(f"{key}={value}\n")
        except Exception as e:
            print(f"Error saving credentials: {str(e)}")
