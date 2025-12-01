import os
from google.adk.tools import CustomTool
class Task:
    def __init__(self, title, time, duration, score=0.0):
        self.title = title; self.time = time; self.duration = duration; self.score = score
    def __repr__(self): return f"{self.title} @ {self.time} (Score: {self.score})"
class SchedulerTool(CustomTool):
    def __init__(self): self.task_queue = []
    def get_name(self) -> str: return 'SchedulerTool'
    def get_description(self) -> str: return 'Manage schedule and tasks.'
    @CustomTool.method
    def add_task(self, title: str, time: str, duration: int, priority_score: float) -> str:
        self.task_queue.append(Task(title, time, duration, priority_score))
        return f"Scheduled: {title}."
    @CustomTool.method
    def get_next_imminent_task(self) -> str:
        return str(self.task_queue[0]) if self.task_queue else "No tasks."
TASK_QUEUE = []
