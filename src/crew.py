from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import tools

@CrewBase
class AgentstackreceiptmanagerCrew():
    """agentstack_receipt_manager crew"""

    @agent
    def receipt_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['receipt_manager'],
            tools=[tools.upload_file_to_drive_tool, tools.file_read_tool, tools.pdf_search_tool,
    tools.dir_read_tool],
            verbose=True,
        )

    # Task definitions
    @task
    def find_and_upload_receipts(self) -> Task:
        return Task(
            config=self.tasks_config['find_and_upload_receipts'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Test crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
