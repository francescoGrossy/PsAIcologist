import os
from agents.psychologist import PsychologistOrchestrator

if __name__ == "__main__":
    task_file_path = "genflow\\tasks\\psychologist_task.yaml"
    orchestrator = PsychologistOrchestrator(task_file_path)
    orchestrator.run_session()
