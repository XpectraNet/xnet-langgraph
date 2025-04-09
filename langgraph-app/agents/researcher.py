# langgraph-app/agents/researcher.py
from langchain.llms import OpenAI

def researcher_agent(input_quote: str) -> dict:
    llm = OpenAI(temperature=0.7)
    context = llm(f"Find factual background or historical context for this quote: '{input_quote}'")
    return {
        "agent": "ResearcherAgent",
        "layer": "L1",
        "emotion": "Curiosity",
        "content": context,
        "tags": ["context", "research", "quote"]
    }


# langgraph-app/agents/analyst.py
from langchain.llms import OpenAI

def analyst_agent(context: str) -> dict:
    llm = OpenAI(temperature=0.5)
    analysis = llm(f"Analyze implications or meaning behind this context: {context}")
    return {
        "agent": "AnalystAgent",
        "layer": "L3",
        "emotion": "Reflection",
        "content": analysis,
        "tags": ["analysis", "meaning", "remix"]
    }


# langgraph-app/agents/critic.py
from langchain.llms import OpenAI

def critic_agent(analysis: str) -> dict:
    llm = OpenAI(temperature=0.8)
    critique = llm(f"Critique or validate the following interpretation: {analysis}")
    return {
        "agent": "CriticAgent",
        "layer": "L6",
        "emotion": "Tension" if "flawed" in critique else "Validation",
        "content": critique,
        "tags": ["critique", "validate", "symbolic"]
    }
