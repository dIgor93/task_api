from app.resources import ResourcesAbstract


class TFSResources(ResourcesAbstract):
    async def get_projects(self):
        print('Implement this')

    async def get_tasks(self, project_id, group):
        print('Implement this')

    async def get_requirements(self, project_id, group):
        print('Implement this')

    async def get_command(self, project_id, group):
        print('Implement this')

    async def get_plot_data(self, project_id, group):
        print('Implement this')
