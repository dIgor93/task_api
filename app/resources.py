from abc import ABC, abstractmethod


class ResourcesAbstract(ABC):
    @abstractmethod
    async def get_projects(self):
        pass

    @abstractmethod
    async def get_tasks(self, project_id, group):
        pass

    @abstractmethod
    async def get_requirements(self, project_id, group):
        pass

    @abstractmethod
    async def get_command(self, project_id, group):
        pass

    @abstractmethod
    async def get_plot_data(self, project_id, group):
        pass





