from google.adk.agents import LLMAgent, ToolAgent, SequentialFlow, ParallelFlow

class ContextAgent(LLMAgent):
    def get_name(self) -> str: return 'ContextAgent'
    def get_description(self) -> str: return 'Extracts task details.'

class ConflictAgent(LLMAgent):
    def get_name(self) -> str: return 'ConflictAgent'
    def get_description(self) -> str: return 'Checks conflicts.'

class ExecutionAgent(ToolAgent):
    def get_name(self) -> str: return 'ExecutionAgent'
    def get_description(self) -> str: return 'Finalizes scheduling.'

class ResponseAgent(LLMAgent):
    def get_name(self) -> str: return 'ResponseAgent'
    def get_description(self) -> str: return 'Generates confirmation.'

def create_reactive_flow(priority_agent, scheduler_tool, model='gemini-2.5-flash'):
    return SequentialFlow(
        name='ReactiveFlow',
        agents=[
            ContextAgent(model_name=model, tools=[scheduler_tool]),
            ParallelFlow(
                name='PrioritizationParallelFlow',
                agents=[
                    priority_agent,
                    ConflictAgent(model_name=model, tools=[scheduler_tool])
                ]
            ),
            ExecutionAgent(model_name=model, tools=[scheduler_tool]),
            ResponseAgent(model_name=model)
        ]
    )
