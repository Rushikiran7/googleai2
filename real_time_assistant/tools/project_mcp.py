from google.adk.tools import CustomTool
class ProjectMCPTool(CustomTool):
    def get_name(self) -> str: return 'ProjectMCPTool'
    def get_description(self) -> str: return 'Manage external projects (Simulated MCP).'
    @CustomTool.method
    def create_project_ticket(self, name: str, sub_tasks: list) -> str:
        return f"Created Project '{name}' with {len(sub_tasks)} sub-tasks."
