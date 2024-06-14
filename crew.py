from crewai import Crew,Process # type: ignore
from tasks import daily_summary_task, group_standings_task, upcoming_matches_task,daily_highlight_task, player_profile_task, tournament_insight_task,gather_match_info_task
from agents import news_researcher,news_writer,ProjectManager
import sys
from langchain_community.llms import ollama
sys.path.append('/path/to/ollama')

crew=Crew(
    agents=[news_researcher,news_writer,ProjectManager],
    tasks=[daily_summary_task, group_standings_task, upcoming_matches_task,gather_match_info_task,daily_highlight_task, player_profile_task, tournament_insight_task],
    process=Process.sequential,
    manager_llm=ollama.Ollama(model="llama3")
)

##Start the task and execution process with enhenced results

result=crew.kickoff(inputs={'topic':'2024 European Championship'})
print(result)