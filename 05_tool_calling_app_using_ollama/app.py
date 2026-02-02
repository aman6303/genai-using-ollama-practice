import re

import ollama
import streamlit as st
from tools import analyze_sentiment, classify_issue, tools

# --- Streamlit Application UI ---

st.set_page_config(layout="wide")
st.title("🤖 Customer Support Message Analyzer")
st.markdown(
    "This app uses a local LLM with function calling to classify a customer issue, analyze its sentiment, and generate a summary."
)


# User input text area
customer_message = st.text_area("Enter the customer's message below:", height=150)

# Analyze button
if st.button("Analyze Message", type="primary"):
    if not customer_message.strip():
        st.warning("Please enter a message to analyze.")
    else:
        try:
            with st.spinner("Analyzing... The AI is thinking and running tools 🤔"):
                # 1. First call to the model to decide which tools to use
                initial_messages = [
                    {
                        "role": "user",
                        "content": f"Analyze this customer message by classifying it and analyzing its sentiment: {customer_message}",
                    }
                ]

                initial_response = ollama.chat(
                    model="qwen3:0.6b",
                    messages=initial_messages,
                    tools=tools,
                )

                messages_for_next_step = initial_messages + [
                    initial_response["message"]
                ]
                tool_outputs = []

                # 2. Execute the tool calls identified by the model
                if "tool_calls" in initial_response["message"]:
                    for tool_call in initial_response["message"]["tool_calls"]:
                        name = tool_call["function"]["name"]
                        args = tool_call["function"]["arguments"]

                        if name == "classify_issue":
                            result = classify_issue(args["message"])
                        elif name == "analyze_sentiment":
                            result = analyze_sentiment(args["message"])
                        else:
                            result = f"Unknown tool call: {name}"

                        tool_outputs.append(
                            {
                                "role": "tool",
                                "name": name,
                                "content": result,
                            }
                        )

                # 3. Send tool outputs back to the model for a final summary
                if tool_outputs:
                    messages_for_next_step.extend(tool_outputs)

                    final_response = ollama.chat(
                        model="qwen3:0.6b",  # Ensure model consistency
                        messages=messages_for_next_step,
                    )

                    response_text = final_response["message"]["content"]
                    # Use a more robust regex to clean up potential model-specific chatter
                    actual_response = re.sub(r"<\|.*?\|>", "", response_text).strip()

                    # --- Display Results ---
                    st.divider()
                    st.subheader("✅ Analysis Complete!")

                    col1, col2 = st.columns(2)

                    # Display the results from the tool calls directly
                    for output in tool_outputs:
                        if output["name"] == "classify_issue":
                            with col1:
                                st.metric("Issue Category", output["content"])
                        elif output["name"] == "analyze_sentiment":
                            with col2:
                                st.metric("Sentiment", output["content"])

                    st.subheader("📝 AI-Generated Summary")
                    st.markdown(actual_response)

                    with st.expander("Show Raw Tool Calls & Model Responses"):
                        st.json(
                            {
                                "initial_response_from_model": initial_response,
                                "executed_tool_outputs": tool_outputs,
                                "final_response_from_model": final_response,
                            }
                        )

                else:
                    # If no tools were called, show the initial response
                    st.info(
                        "The model did not call any specific tools. Here is its direct response:"
                    )
                    st.write(initial_response["message"]["content"])

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.warning(
                "Please ensure the Ollama application is running and the specified model (e.g., 'qwen2') is installed. You can run `ollama pull qwen2` in your terminal."
            )
