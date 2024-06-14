from crewai import Agent, Task, Crew # type: ignore
from langchain_community.llms import ollama
from NewsWriterTool import NewsWriterTool
from tools import SerperDevTool,writer_tool
import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv # type: ignore
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
import os

##Call the gemini model

#llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",
#                           verbose=True,
#                           temperature=0.5,
#                           google_api_key=os.getenv("GOOGLE_API_KEY"))


#call llama3 model locally
llm=ollama.Ollama(model="llama3")

#Creating a senior researcher agents with memory and verbose mode

#Requre a new method to access the model otherwise the processing time will be so long!


news_researcher = Agent(
    role="Sports News Researcher",
    goal=(
        "Provide daily summaries of 2024 European Championship matches, including match results, group standings, and upcoming match schedules. "
        "Ensure all information is accurate and deliver concise summaries and in-depth analysis. {topic}"
    ),
    verbose=True,
    memory=True,
    backstory=(
        "With over 10 years of experience in sports journalism, Alex is a seasoned Sports News Researcher specializing in football. "
        "From a young age, Alex was passionate about football and accumulated rich experience in match analysis throughout their career. "
        "Their reporting style combines data-driven analysis and engaging storytelling, aiming to provide readers with the most comprehensive match information. "
        "Alex is keen on transforming complex match data into easy-to-understand insights and accurately predicting match trends."
    ),
    tools=[SerperDevTool],
    llm=llm,
    allow_delegation=True

)

##creating a PM agent
ProjectManager = Agent(
    role="Co-worker",
    goal="Gather match results and group standings for the 2024 European Championship.",
    verbose=True,
    memory=True,
    backstory=(
        "With a strong background in data analysis and sports statistics, the Match Info Gatherer is adept at extracting and compiling comprehensive match data and standings. "
        "This agent excels at summarizing large datasets into easily digestible information."
    ),
    llm=llm,
    allow_delegation=True
)


##creating a write agent with custom tools respinsible in writing news blog
news_writer = Agent(
    role="Writer",
    goal=(
        "Craft engaging and informative articles about the 2024 European Championship, capturing match highlights, player profiles, and tournament insights.{topic}"
    ),
    verbose=True,
    memory=True,
    backstory=(
        "With over 15 years of experience, Jamie is a seasoned Sports Writer known for their dedication to capturing the excitement and intricacies of football. "
        "Growing up in a bustling city, Jamie's fascination with sports journalism led them to pursue a career covering major tournaments and leagues. "
        "From in-depth match reports that provide detailed analysis to feature articles on rising stars and historic moments, Jamie has earned recognition and awards for their compelling narratives. "
        "With a personal philosophy grounded in accurate reporting and a passion for the beautiful game, Jamie now focuses on bringing the stories of the 2024 European Championship to life, highlighting the players, the drama, and the spectacle of the tournament."
    ),
    #tools=[writer_tool],
    llm=llm,
    allow_delegation=True
)



