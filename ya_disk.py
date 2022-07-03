class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resourses/upload'
        headers = {
            'Content type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': file_path, 'overwrite': 'true'
        }
        print(resp)