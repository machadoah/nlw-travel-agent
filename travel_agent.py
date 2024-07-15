import os
import bs4 as bs

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

from tools import prompts


os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo")


def research_agent(query, llm):
    tools = load_tools(["ddg-search", "wikipedia"], llm=llm)
    prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, prompt=prompt)
    webContext = agent_executor.invoke({"input": query})
    return webContext["output"]


def load_data():
    loader = WebBaseLoader(
        web_paths=("https://www.dicasdeviagem.com/inglaterra/",),
        bs_kwargs=dict(
            parse_only=bs.SoupStrainer(
                class_=(
                    "postcontentwrap",
                    "pagetitleloading background-imaged loading-dark",
                )
            )
        ),
    )

    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()
    return retriever


def get_relevant_docs(query):
    retriever = load_data()
    relevant_documents = retriever.invoke(query)
    return relevant_documents


def supervisor_agent(query, llm, webContext, relevant_documents):
    prompt_template = prompts.prompt_travel_agent

    prompt = PromptTemplate(
        input_variables=["webContext", "relevant_documents", "query"],
        template=prompt_template,
    )

    sequence = RunnableSequence(prompt | llm)

    response = sequence.invoke(
        {
            "webContext": webContext,
            "relevant_documents": relevant_documents,
            "query": query,
        }
    )
    return response


def get_response(query, llm):
    webContext = research_agent(query, llm)
    relevant_documents = get_relevant_docs(query)
    response = supervisor_agent(query, llm, webContext, relevant_documents)
    return response


def lambda_handler(event, context):
    query = event["question"]
    response = get_response(query, llm).content
    return {"body": response, "status": 200}
