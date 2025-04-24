import asyncio
from langchain.chat_models import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    # Define the MCP server configuration
    mcp_servers = {
        "mean_tool": {
            "url": "http://localhost:8001/mcp",
            "transport": "sse",
        }
    }

    # Initialize the MCP client
    async with MultiServerMCPClient(mcp_servers) as client:
        # Load tools from the MCP server
        tools = await client.load_tools()

        # Initialize the language model
        llm = ChatOpenAI(temperature=0)

        # Create the LangGraph agent with the loaded tools
        agent = create_react_agent(llm, tools)

        # Define the user input
        user_input = {"messages": "Calculate the mean of the numbers 10, 20, 30, 40, and 50."}

        # Invoke the agent with the user input
        result = await agent.ainvoke(user_input)

        # Print the agent's response
        for message in result["messages"]:
            print(message.content)

# Run the main function
asyncio.run(main())
