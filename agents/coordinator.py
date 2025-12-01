from google.adk.agents import LLMAgent
from google.adk import Context
from tools.scheduler_tool import SchedulerTool
from tools.project_mcp import ProjectMCPTool
import logging
from google.adk.tools import BuiltInCodeExecutor, BuiltInGoogleSearch

class TaskCoordinator(LLMAgent):
    def __init__(self, model, reactive_flow, code_executor, google_search, project_mcp, **kwargs):
        super().__init__(model_name=model, tools=[code_executor, google_search, project_mcp], **kwargs)
        self.reactive_flow = reactive_flow

    def get_name(self) -> str: return 'TaskCoordinator'
    def get_description(self) -> str: return 'Router, Code Executor, and Project Manager.'

    async def run_async(self, context: Context) -> Context:
        text = context.events[-1].text.lower()
        if "project" in text or "tomorrow" in text:
            logging.info("Routing to Future Flow (Code Exec)")
            
            # Example of Code Execution for complex decomposition
            code = f"""
from tools.project_mcp import ProjectMCPTool
project_tool = ProjectMCPTool()
print(project_tool.create_project_ticket(name="Project Phoenix", sub_tasks=['Research', 'Outline', 'Draft']))
"""
            await self.tools[0].execute_code(code)
            context.add_event("Future Flow executed via Code Executor.")
            return context
        
        logging.info("Routing to Reactive Flow.")
        return await self.reactive_flow.run_async(context)
