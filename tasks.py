from crewai import Task # type: ignore
#from NewsWriterTool import NewsWriterTool
from tools import SerperDevTool,writer_tool
from agents import news_researcher,news_writer,ProjectManager


daily_summary_task = Task(
    description=(
        "Summarize the daily match information of the 2024 European Championship, including match results, key data, and highlights. "
        "Generate a concise summary covering match results, key statistics, and notable moments."
    ),
    expected_output=(
        "A report including all daily match results, key statistics (e.g., goals, yellow/red cards), and highlights. "
        "The report should include tabular results and narrative descriptions of match highlights."
    ),
    tools=[SerperDevTool],  # Ensure it includes relevant data collection tools
    agent=news_researcher
)

group_standings_task = Task(
    description=(
        "Update and provide the latest group standings for the 2024 European Championship. "
        "Include key information such as points, goal differences, and rankings for each group."
    ),
    expected_output=(
        "A detailed group standings table showing the current points, goal differences, rankings, and qualification status for each team."
    ),
    tools=[SerperDevTool],  # Ensure it includes relevant data collection tools
    agent=news_researcher
)

upcoming_matches_task = Task(
    description=(
        "Summarize and display the schedule of upcoming matches for the 2024 European Championship. "
        "Include match times, competing teams, locations, and broadcast information."
    ),
    expected_output=(
        "A list of upcoming matches including the match times, competing teams, locations, and broadcast information."
    ),
    tools=[SerperDevTool],  # Ensure it includes relevant data collection tools
    agent=news_researcher
)

gather_match_info_task = Task(
    description="Gather match results and group standings for the 2024 European Championship from various sources.",
    expected_output="Detailed match results and group standings.",
    agent=ProjectManager,
)

daily_highlight_task = Task(
    description=(
        "Write a compelling article summarizing the highlights of the 2024 European Championship matches held today. "
        "Focus on key moments, standout performances, and any unexpected events. "
        "Include quotes from players and coaches if available."
    ),
    expected_output=(
        "An engaging article summarizing the highlights of today's matches, including key moments, standout performances, and any unexpected events. "
        "Include quotes from players and coaches if available."
    ),
    tools=[writer_tool],  # Ensure it includes relevant data collection tools
    agent=news_writer,
    async_execution=False
)

player_profile_task = Task(
    description=(
        "Write an in-depth feature article on a standout player from the 2024 European Championship. "
        "Include their background, current performance in the tournament, and impact on their team."
    ),
    expected_output=(
        "A detailed feature article on a standout player, including their background, current performance in the tournament, and impact on their team."
    ),
    tools=[writer_tool],  # Ensure it includes relevant research tools
    agent=news_writer,
    async_execution=False
)

tournament_insight_task = Task(
    description=(
        "Write an insightful article analyzing a key trend or development in the 2024 European Championship. "
        "Focus on tactical changes, emerging trends, or notable team strategies."
    ),
    expected_output=(
        "An insightful article analyzing a key trend or development in the tournament, focusing on tactical changes, emerging trends, or notable team strategies."
    ),
    tools=[writer_tool],  # Ensure it includes relevant analysis tools
    agent=news_writer,
    async_execution=False
)


news_writing_task = Task(
    description=(
        "Write an insightful and compelling article about the {topic} that "
        "addresses the needs of underrepresented communities. Focus on identifying at least two recent innovations "
        "or applications, gather stories or case studies, and include interviews or quotes from experts or affected "
        "individuals if possible. Highlight both the potential benefits and any ethical considerations or challenges."
    ),
    expected_output=(
        "A well-researched and engaging article around 1,200-1,500 words long, suitable for a tech news platform. "
        "The article should include a compelling introduction, detailed body sections with examples and case studies, "
        "and a conclusion summarizing the impact of the technology on the community."
    ),
    tools=[writer_tool],  # Ensure this includes tools for research and interviews
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.txt'
)


