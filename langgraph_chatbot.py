import json
from langgraph.graph import StateGraph

# Load responses from a JSON file
with open("responses.json", "r") as file:
    responses = json.load(file)

# Simple function to process user input
def chat_node(state: dict) -> dict:
    user_input = state["user_input"].lower()
    bot_response = responses.get(user_input, "I'm not sure how to respond to that. Can you ask something else?")
    return {"user_input": user_input, "bot_response": bot_response}

# Create LangGraph state graph
graph = StateGraph(dict)
graph.add_node("chat", chat_node)
graph.set_entry_point("chat")

# Compile graph
graph = graph.compile()

# Example run
if __name__ == "__main__":
    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
            break
        state = {"user_input": user_message}
        output = graph.invoke(state)
        print("Bot:", output["bot_response"])
