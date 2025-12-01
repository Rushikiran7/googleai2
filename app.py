from google.adk.app import App
from google.adk.services import InMemoryCredentialService, InMemorySessionService
from google.adk.session import EventsCompactionConfig
from google.adk.tools import BuiltInCodeExecutor, BuiltInGoogleSearch
import logging
import sys

# Add project root to path for imports
sys.path.append('.')

# Import components from subdirectories
from tools.scheduler_tool import SchedulerTool, TASK_QUEUE
from tools.project_mcp import ProjectMCPTool
from memory.memory_bank_service import MEMORY_BANK
from agents.priority_a2a.agent import PriorityAgent
from agents.reactive_flow import create_reactive_flow
from agents.proactive_loop import MonitorAgent, InstructionAgent
from agents.coordinator import TaskCoordinator

def create_adk_app(model='gemini-2.5-flash'):
    # Tool Instances (must be initialized once)
    scheduler = SchedulerTool(); scheduler.task_queue.extend(TASK_QUEUE)
    code_executor = BuiltInCodeExecutor()
    google_search = BuiltInGoogleSearch()
    project_mcp = ProjectMCPTool()

    # Agent Instances
    priority_agent = PriorityAgent(model, MEMORY_BANK)
    instruction_agent = InstructionAgent(model)
    monitor_agent = MonitorAgent(model, instruction_agent, scheduler)
    
    # Flows
    reactive_flow = create_reactive_flow(priority_agent, scheduler, model)
    coordinator = TaskCoordinator(model, reactive_flow, code_executor, google_search, project_mcp)

    return App(
        name='OmniscientAssistant',
        entry_agent=coordinator,
        credential_service=InMemoryCredentialService(),
        session_service=InMemorySessionService(),
        agents=[coordinator, reactive_flow, monitor_agent, priority_agent, instruction_agent],
        tools=[scheduler, code_executor, google_search, project_mcp]
    )
