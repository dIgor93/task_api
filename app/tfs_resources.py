import requests
from requests import HTTPError

from app.resources import ResourcesAbstract

TFS_DSN = 'https://tfs.project/root/link'


class TFSResources(ResourcesAbstract):
    async def get_projects(self):
        try:
            response = requests.get(TFS_DSN + "/projects")
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    async def get_tasks(self, project_id, group):
        try:
            response = requests.get(TFS_DSN + "/tasks")
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    async def get_requirements(self, project_id, group):
        try:
            response = requests.get(TFS_DSN + "/req")
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    async def get_command(self, project_id, group):
        try:
            response = requests.get(TFS_DSN + "/commands")
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    async def get_plot_data(self, project_id, group):
        try:
            response = requests.get(TFS_DSN + "/query?params")
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()
