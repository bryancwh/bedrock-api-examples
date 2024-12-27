import streamlit as st
import boto3

def main():
    st.title("Bedrock Chatbot")
    
    # Initialize chat history in session state if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display chat history
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

    # Assign default value to response
    output = "Sorry, I couldn't process your request at the moment."

    # Chat input
    prompt = st.chat_input("What's on your mind?", key="input")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Bedrock Knowledge Base RetrieveAndGenerate API
        bedrock = boto3.client('bedrock-agent-runtime', region_name="us-west-2")
        try:
            response = bedrock.retrieve_and_generate(
                input = {
                    'text': prompt
                },
                retrieveAndGenerateConfiguration={
                    'type': 'KNOWLEDGE_BASE',
                    'knowledgeBaseConfiguration': {
                        'knowledgeBaseId': "YOUR_BEDROCK_KB_ID",
                        'modelArn': "YOUR_BEDROCK_MODEL_ARN",
                        'retrievalConfiguration': {
                            'vectorSearchConfiguration': {
                                'numberOfResults': 3
                            }
                        },
                        'generationConfiguration': {
                            'inferenceConfig': {
                                'textInferenceConfig': {
                                    'maxTokens': 500,
                                    'temperature': 0.7,
                                    'topP': 0.9
                                }
                            } 
                        }
                    }
                }
            )
            output = response["output"]["text"]

        except Exception as e:
            print(f"An error occurred: {e}")

        st.session_state.messages.append({"role": "assistant", "content": output})

        st.chat_message("assistant").write(output)

if __name__ == "__main__":
    main()
