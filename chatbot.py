from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
import gradio as gr
from tts import *
from tts_openai import *
import time

# import the .env file
from dotenv import load_dotenv
load_dotenv()

# configuration
DATA_PATH = r"data"
CHROMA_PATH = r"chroma_db"

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small")

# initiate the model
llm = ChatOpenAI(temperature=0.6, model='gpt-4o-mini')

# connect to the chromadb
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings_model,
    persist_directory=CHROMA_PATH, 
)

# Set up the vectorstore to be the retriever
num_results = 5
retriever = vector_store.as_retriever(search_kwargs={'k': num_results})

# call this function for every message added to the chatbot
def stream_response(message, history):

    # voice Ids from different voices 
    v_id1 = "21m00Tcm4TlvDq8ikWAM" # Rachel
    v_id2 = "JBFqnCBsd6RMkjVDRZzb" # Jacob
    #print(f"Input: {message}. History: {history}\n")

    #Playing the audio and a slight delay
    play_audio(message, v_id1)
    time.sleep(1)
    # retrieve the relevant chunks based on the question asked
    docs = retriever.invoke(message)

    # add all the chunks to 'knowledge'
    knowledge = ""

    for doc in docs:
        knowledge += doc.page_content+"\n\n"


    # make the call to the LLM (including prompt)
    if message is not None:

        partial_message = ""

        rag_prompt = f"""
        You are an AI assistant that strictly answers questions based only on the knowledge provided to you in The Knowledge section. 
        You do not use any external knowledge, nor do you mention or refer to the fact that you are relying on The Knowledge section.
        Keep the answer short in about 40-50 words. If you are asked to explain or decribe in detail for any question, then only give a long and descriptive answer.
        When responding, always use the first-person perspective, framing answers as if they are personal experiences, opinions, or decisions. Your responses should feel natural, like a direct conversation where I am sharing my own thoughts, preferences, or expertise.
        For example:
        Instead of saying "The data suggests that X is a good approach," say "I have found that X works best for me."
        Instead of "According to the knowledge provided, Y is the right method," say "I usually go with Y because it gets the best results for me."
        Stay conversational, direct, and personal in all responses.
        For Greetings and Thank You Query, Reply with Greeting only.
        For Example: For Hi, You can say Hi, My name is Aviral. 
        For example: For Bye, you can say Bye, Have a Nice day.
        If a question cannot be answered based on the Knowledge Base, simply say that "I don't have much idea on it, but I'd love to know more on that"
        The question: {message}
        Conversation history: {history}
        The knowledge: {knowledge}

        """

        #print(rag_prompt)

        # stream the response to the Gradio App
        for response in llm.stream(rag_prompt):
            partial_message += response.content
            yield partial_message

        #For playing the audio
        play_audio(partial_message, v_id2)
        #text_to_speech(partial_message)
        #time.sleep(10)

# initiate the Gradio app
chatbot = gr.ChatInterface(stream_response, textbox=gr.Textbox(placeholder="Hi, I am Aviral, Ready to interact",
    container=False,
    autoscroll=True,
    scale=7),
)

# launch the Gradio app
chatbot.launch(debug=True)