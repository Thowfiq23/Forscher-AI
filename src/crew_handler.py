# src/crew_handler.py

import os
import yaml
from dotenv import load_dotenv

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file.
# This line looks for a .env file and loads the variables from it.
load_dotenv()

# --- 1. Load Configurations ---
# Load agents and tasks configuration from our YAML files.
with open('src/agents.yaml', 'r') as f:
    agents_config = yaml.safe_load(f)

with open('src/tasks.yaml', 'r') as f:
    tasks_config = yaml.safe_load(f)

# --- 2. Initialize the LLM and Tools ---
# Initialize the Gemini Pro LLM.
# verbose=True allows us to see the LLM's thinking process.
llm = ChatGoogleGenerativeAI(model="gemini-pro", verbose=True)

# Initialize the Serper search tool.
search_tool = SerperDevTool()


# --- 3. Create Agent Instances ---
# We create agent objects from the configurations we loaded.
# The researcher is the only one who needs the search_tool.
researcher = Agent(
    **agents_config['researcher'],
    llm=llm,
    tools=[search_tool],
    allow_delegation=False,
    verbose=True
)

analyst = Agent(
    **agents_config['analyst'],
    llm=llm,
    allow_delegation=False,
    verbose=True
)

writer = Agent(
    **agents_config['writer'],
    llm=llm,
    allow_delegation=False,
    verbose=True
)

# --- 4. Create Task Instances ---
# We create task objects from our configurations and assign them to agents.
research_task = Task(
    **tasks_config['research_task'],
    agent=researcher
)

analysis_task = Task(
    **tasks_config['analysis_task'],
    agent=analyst
)

report_task = Task(
    **tasks_config['report_task'],
    agent=writer,
    output_file="research_report.md" # The final report will be saved to this file.
)

# --- 5. Assemble and Run the Crew ---
# We assemble our agents and tasks into a Crew.
# The process is sequential, meaning tasks will be executed one after another.
research_crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, report_task],
    process=Process.sequential,
    verbose=2
)

# This is the main function that will be called by our web interface.
def run_crew(topic):
    """Kicks off the research crew with a given topic."""
    result = research_crew.kickoff(inputs={'topic': topic})
    return result

# --- 6. Main Execution Block (for direct testing) ---
# This block allows us to run the script directly from the terminal for testing.
if __name__ == "__main__":
    print("## Welcome to the Forscher Research Platform ##")
    topic = input("Please enter the research topic: ")

    print("\n--- Starting Research Crew ---")
    final_report = run_crew(topic)

    print("\n--- Research Crew Finished ---")
    print("\nFinal Report:")
    print(final_report)