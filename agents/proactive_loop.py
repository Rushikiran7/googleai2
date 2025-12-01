from google.adk.agents import LLMAgent, LoopAgent
import asyncio
import logging

class InstructionAgent(LLMAgent):
    def get_name(self) -> str: return 'InstructionAgent'
    def get_description(self) -> str: return 'Generates nudges.'

class MonitorAgent(LoopAgent):
    def __init__(self, model: str, instructor, scheduler, **kwargs):
        super().__init__(model_name=model, **kwargs)
        self.instructor = instructor
        self.scheduler = scheduler
    
    def get_name(self) -> str: return 'MonitorAgent'
    def get_description(self) -> str: return 'Continuously checks schedule.'

    async def should_loop_continue(self, context) -> bool: return True

    async def execute_loop(self, context) -> Context:
        next_task = self.scheduler.get_next_imminent_task()
        if "No tasks" not in next_task:
            logging.info(f"MONITOR: Nudging for task: {next_task}")
            # Simplified nudge generation (LLM call is skipped in this block for speed)
        await asyncio.sleep(60) # Loop interval
        return context
