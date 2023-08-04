
# AI Chatbot using OpenAI's GPT-3.5 Turbo

![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Icon.png?raw=true)

The AI Chatbot using OpenAI's GPT-3.5 Turbo is an innovative project that showcases the power of natural language processing and artificial intelligence. Built on OpenAI's GPT-3.5 Turbo engine, this chatbot serves as a virtual AI Tutor, capable of answering questions related to the vast field of artificial intelligence.

The primary goal of this chatbot is to provide users with a seamless and interactive experience while gaining valuable insights into artificial intelligence concepts. It acts as a helpful guide for students, developers, or anyone curious about AI, offering informative and accurate responses to a wide range of AI-related queries.

The chatbot's user interface is designed using Streamlit, making it user-friendly and accessible to a broad audience. Users can simply enter their questions, and the AI Tutor generates real-time responses, harnessing the advanced language understanding and generation capabilities of GPT-3.5 Turbo.

Key Features:

 - Interactive user interface for engaging conversations with the AI Tutor.
 - Real-time response generation powered by GPT-3.5 Turbo.
 - Support for a diverse array of AI topics and queries.
 - Easy deployment with Streamlit for web-based access.
Customizable and extensible for future enhancements and improvements.


## Table Of Contents

 - [Installation](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#installation)
 - [Usage](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#usage)
 - [Acknowledgements](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#acknowledgements)
 - [Technologies Used](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#technologies-used)
 - [Code Description](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#code-description)
 - [Screenshots](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#screenshots)
 - [Future Scope](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#future-scope)
 - [Contributing](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#contributing)
 - [License](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/tree/main#license)
## Installation

To use the AI Chatbot powered by OpenAI's GPT-3.5 Turbo, follow these steps to set up the project environment on your local machine:

1.Clone the Repository:

Start by cloning this GitHub repository to your local machine using the following command:

```bash
git clone https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api.git
```

2.Create a Virtual Environment (Optional):

It is recommended to create a virtual environment to isolate the project dependencies. Use the following commands to create and activate a virtual environment (if desired):

```bash
python -m venv venv
source venv\Scripts\activate

```

3.Install Dependencies:

Install the required Python dependencies using pip:

```bash
pip install -r requirements.txt

```

4.Get OpenAI API Key:

 - Create an account on the OpenAI platform (https://openai.com/).
 - Obtain an API key from your OpenAI account dashboard.
 - Create a new file named .env in the project's root directory.
 - Add your API key to the .env file in the following format:

```bash
OPENAI_API_KEY=your-api-key-here
```
## Usage

1.Prepare the Codebase:

Make sure you have completed the installation steps mentioned in the previous section on your local machine.

2.Run the Streamlit Application:
Open the terminal in the project's root directory.
Run the following command to start the Streamlit application:

```bash
streamlit run chatbot.py # Your file name
```

a.Interact with the Chatbot:

 - The Streamlit application will open in your web browser.
 - Type your question in the "Question" text input field and press Enter.
 - The chatbot will process your question and provide an AI-generated response.
 - You can have a back-and-forth conversation with the chatbot by entering multiple questions.

b.View Conversation History:

 - The chat history will be displayed below the chat input box, showing both user questions and chatbot responses.

c.Quit the Application:

 - To quit the chatbot application, simply close the Streamlit web app or press Ctrl+C in the terminal.
## Acknowledgements

 I would like to express our sincere gratitude to all those who have contributed to the development and success of the AI Chatbot project. Their support, guidance, and expertise have been invaluable throughout the journey of building this interactive AI Tutor.

 - OpenAI Team: My deepest appreciation goes to the team at OpenAI for developing the GPT-3.5 Turbo engine and providing access to their powerful language processing technology. Their cutting-edge advancements in AI have enabled us to create an intelligent and helpful AI Tutor.

 - Streamlit Community: I extend my thanks to the Streamlit community for developing a user-friendly and efficient platform that made it seamless to build and deploy web-based applications. Streamlit has played a crucial role in bringing the AI Chatbot to life.

 - GitHub Contributors: I am grateful to all the contributors to the AI Chatbot's GitHub repository. Your feedback, bug reports, and pull requests have helped improve the chatbot's functionality and user experience.

 - Inspiration from the AI Community: I draw inspiration from the vibrant AI community that continues to push the boundaries of artificial intelligence. The dedication and creativity of fellow AI enthusiasts motivate us to explore new possibilities and innovations.

 - Our Supporters: Last but not least, I would like to thank all the users and supporters of the AI Chatbot. Your engagement, encouragement, and feedback motivate us to continuously enhance the chatbot and make it a valuable resource for AI enthusiasts worldwide.

This project would not have been possible without the collective efforts and contributions from these individuals and organizations. We are deeply grateful for their role in making the AI Chatbot a reality.


## Technologies Used

The AI Chatbot project utilizes several cutting-edge technologies and tools to provide an interactive and intelligent user experience. Below are the key technologies used in the development and deployment of the AI Chatbot:

 - OpenAI GPT-3.5 Turbo: OpenAI's GPT-3.5 Turbo is the core technology powering the AI Chatbot. It is a highly advanced natural language processing (NLP) model that can generate human-like text responses. The chatbot leverages GPT-3.5 Turbo to answer user questions and engage in interactive conversations.

 - Streamlit: Streamlit is an open-source Python library that facilitates the creation of web applications with minimal effort. In this project, Streamlit is used to build the user interface for the AI Chatbot, enabling easy interaction between the user and the chatbot.

 - Python: Python serves as the primary programming language for the entire project. It is widely known for its simplicity, versatility, and extensive libraries, making it an ideal choice for AI and web development tasks.

 - dotenv: The dotenv library is used to manage environment variables in the project. It enables the secure storage of sensitive information, such as the OpenAI API key, in a .env file and ensures that this data remains confidential.

 - GitHub: GitHub provides version control and collaborative tools that are crucial for managing the project's codebase. It allows developers to work together, track changes, and manage contributions effectively.
## Code Description

 1. chatbot.py file-

 This file serves as the main application script for the AI Chatbot. It is built using the Streamlit library to create a user-friendly web-based interface. The key functionalities of this file include:

 - User Interaction: The user can input questions related to AI in the provided text input field. Upon submission, the user's query is sent to the AI Chatbot for processing.

 - AI Response Generation: The user's query is processed using the get_chatgpt_response() function from utils.py. This function interacts with the OpenAI API to generate a response from the AI model (GPT-3.5 Turbo).

 - Displaying User and AI Messages: The chat history, including the user's query and the AI's response, is displayed in a chat-like format using the message() function from the Streamlit Chat extension.

 - Session Management: The application manages the user's past queries and AI-generated responses using Streamlit's st.session_state, ensuring a seamless conversation flow.

 - Selecting Model: The user can choose between different AI models (currently, only GPT-3.5 Turbo is available).

 ```python
 import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# Set page title and favicon
st.set_page_config(page_title="AI Chatbot", page_icon=":robot_face:")

# Sidebar header
with st.sidebar:
    st.title('AI Chatbot')
    st.markdown('''
    **Explore and Learn with AI:**

    - 🤖 Ask questions on various topics.
    - 📚 Receive informative and helpful responses.
    - 💡 Expand your knowledge with AI assistance.
    ''')
    st.info("Note: This chatbot leverages AI to enhance your learning experience.")

st.title("AI Chatbot")
st.subheader("AI Assistance:")
```
 - Importing Libraries: This section imports the necessary libraries and modules required for the chatbot application. It imports streamlit for the web application, streamlit_chat to display the chat messages, utils to access utility functions, os for working with the operating system, dotenv for loading environment variables from a file, and openai to interact with the OpenAI API.

 - Setting Up OpenAI API Key: It loads the OpenAI API key from the .env file using os.getenv() and sets it as the API key for the openai library.

 - import streamlit as st: Imports the Streamlit library, which is used to create interactive web applications with Python.

 - st.set_page_config(page_title="AI Chatbot", page_icon=":robot_face:"): Sets the title and favicon (icon displayed on browser tabs) of the web page.

 - with st.sidebar:: Creates a sidebar section on the web page where you can add content that appears on the side.

 - st.title('AI Chatbot'): Adds a title to the sidebar, displaying "AI Chatbot".

 - st.markdown(''' ... '''): Uses Markdown syntax to add formatted text to the sidebar. In this case, it adds a section with bullet points that describe the capabilities of the AI Chatbot.

 - st.info("Note: This chatbot leverages AI to enhance your learning experience."): Displays an informational box at the bottom of the sidebar, providing a note about the chatbot's usage of AI.

The code sets up a visually appealing and informative sidebar for your AI Chatbot application, presenting users with an introduction and key features of the chatbot. The st.set_page_config function adds branding to the web page, making it more identifiable.
 
 - Setting Up Streamlit Web Application: It creates the basic layout of the web application using Streamlit. The st.sidebar() st.title() and st.subheader() functions set the sidebar,title and subheader of the web page, respectively.

 ```python
 if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Question: ", key="input")
```
 - Initializing Session State: The code checks if certain session state variables, generated and past, are already present. If not, it initializes them to empty lists. These session state variables are used to store the conversation history.

 - User Input: It creates a text input box using st.text_input() where the user can enter their question. The user input is stored in the variable query.

 ```python
 if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages)  # Use GPT-3.5 Turbo (default model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)
```

 - Handling User Input: This section checks if the messages session state variable is already present. If not, it initializes it with the initial messages using the get_initial_message() function from the utils.py file.

 - Generating AI Response: When the user enters a query and submits it, the code updates the messages with the user's input using update_chat(). It then calls get_chatgpt_response() to generate an AI response based on the updated messages. The AI response is stored in the variable response.

 - Updating Session State: The AI response and the user's query are added to the past and generated session state lists, respectively. These lists are used to display the conversation history.

 ```python
 if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

    with st.expander("Show Messages"):
        st.write(messages)
```

 - if st.session_state['generated']:
This line checks if the generated key is present in the session state. If there are generated responses stored in the session state, it means that there is a conversation history to display.

 - for i in range(len(st.session_state['generated'])-1, -1, -1):
This for loop iterates over the conversation history stored in the generated session state list in reverse order. It starts from the last generated response and goes backward through the conversation history.

 - message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
This line calls the message() function from the streamlit_chat module to display the user's queries. The is_user=True argument is passed to indicate that the message belongs to the user, and the key argument is set to a unique identifier with the index i to ensure that each message is uniquely identified.

 - message(st.session_state["generated"][i], key=str(i))
This line calls the message() function again to display the AI's responses. The is_user=True argument is not provided, so by default, it will be treated as an AI response. The key argument is set to a unique identifier with the index i.

 - with st.expander("Show Messages"):
This line creates an expander widget with the label "Show Messages". An expander allows collapsing and expanding a section of content, which is useful when there is a lot of conversation history to display.

 - st.write(messages):
Within the expander, the code uses st.write() to display the entire conversation history, which is stored in the messages list. The messages are already displayed using the message() function within the for loop, so this line serves as a summary display of the conversation history within the collapsible expander.

2. allow.py file-

This file contains a simple command-line interface that allows users to interact with the AI Chatbot. It is primarily intended for testing and development purposes. The key functionalities of this file include:

 - User Interaction: The script prompts the user to enter questions or type 'q' to quit.

 - AI Response Generation: The user's input is sent to the AI Chatbot, and the response is generated using the OpenAI API.

 - Displaying AI Response: The AI-generated answer is displayed to the user on the command line.

```python
api_key = st.text_input("Please enter your OpenAI API key:")
openai.api_key = api_key
```
Setting Up OpenAI API Client: These two lines allow users to input their OpenAI API key using st.text_input. The entered API key is stored in the variable api_key. Then, the openai.api_key is set to the entered API key, so the OpenAI Python client can use it for authentication.

```python
while True:
    user_input = st.text_input("Ask a question (or enter 'q' to quit):")
```
Main Program Loop and User Input: This while loop runs indefinitely until the user decides to quit. Within the loop, the user is prompted to enter a question using st.text_input, and the input is stored in the variable user_input.

```python
response = openai.Completion.create(
    engine=engine,
    prompt=user_input,
    max_tokens=100,
    temperature=0.7,
    n=1,
    stop=None,
    top_p=1.0
)
```
 - engine=engine: The engine parameter specifies the language model to use for generating the response. In this case, the engine variable is set to "gpt-3.5-turbo", which is the GPT-3.5 Turbo model. This model is powerful and efficient for most use cases.

 - prompt=user_input: The prompt parameter is where the user's input question is passed. The GPT-3.5 Turbo model takes this prompt as input and generates a response based on it.

 - max_tokens=100: The max_tokens parameter determines the maximum number of tokens in the generated response. Tokens are chunks of text, and setting this parameter to 100 means the generated response will be limited to 100 tokens. This helps control the length of the output.

 - temperature=0.7: The temperature parameter controls the randomness of the generated response. A higher value (e.g., 1.0) makes the output more random, while a lower value (e.g., 0.7) makes it more focused and deterministic.

 - n=1: The n parameter specifies the number of alternative completions to generate. Here, it is set to 1, which means only one response will be generated.

 - stop=None: The stop parameter can be used to define a stopping sequence for the model. If the model generates a response containing the stop sequence, it will stop generating further text. In this case, it is set to None, so there is no specific stopping sequence defined.

 - top_p=1.0: The top_p parameter, also known as nucleus sampling or "penalty for words outside the nucleus," controls the diversity of the generated response. A value of 1.0 means all words are considered, while lower values restrict the vocabulary to the most likely words.

After making the API call, the response from the OpenAI GPT-3.5 Turbo model is stored in the response variable, which contains information about the generated completion, including the generated text, likelihood, and more. The generated response text is later extracted and displayed to the user.

```python
answer = response.choices[0].text.strip()
```
Extracting the Answer: This line extracts the generated answer from the API response using response.choices[0].text. The answer is stored in the variable answer.

```python
st.text("Answer: " + answer)
```
Displaying the Answer: This line displays the generated answer to the user using st.text. The response from the GPT-3.5 Turbo model is shown as "Answer: " followed by the extracted answer text.

3. utils.py file-

This file contains utility functions used by chatbot.py. It handles interactions with the OpenAI API, manages chat history, and processes AI responses. The key functions in this file include:

 - get_initial_message(): Returns the initial message displayed by the AI Chatbot upon starting the conversation.

 - get_chatgpt_response(messages, model="gpt-3.5-turbo"): Sends a list of chat messages to the OpenAI API and receives the AI-generated response.

 - update_chat(messages, role, content): Appends a new chat message (user or assistant) to the existing list of messages.

```python
def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Tutor. Who answers brief questions about AI."},
    ]
    return messages
```
get_initial_message() Function: This function returns an initial set of messages to initialize a conversation with the AI tutor. It sets up a simple conversation with a system message representing the role and purpose of the AI tutor.

```python
def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    conversation = "\n".join(messages)
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": conversation}]
    )
    return response['choices'][0]['message']['content']
```
 - get_chatgpt_response(messages, model="gpt-3.5-turbo") Function: This function takes a list of messages and a model (defaulting to "gpt-3.5-turbo") and returns the response generated by the OpenAI GPT-3.5 Turbo model.

 - conversation = "\n".join(messages): It joins the individual messages in the messages list into a single string with newline characters as separators. This creates the conversation in the format expected by the OpenAI API.

 - openai.ChatCompletion.create(): This function call sends the conversation to the OpenAI API to generate a response. The model parameter specifies which language model to use.

 - return response['choices'][0]['message']['content']: It extracts the generated content (text) from the API response and returns it as the AI's response to the conversation.

 ```python
 def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
```
 - update_chat(messages, role, content) Function: This function updates the conversation messages list with a new user or AI response.

 - messages.append({"role": role, "content": content}): It appends a new message dictionary with the specified role (either "user" or "assistant") and the corresponding content (text) to the messages list.

 - return messages: It returns the updated list of messages, which now includes the new response.

 The project uses the Streamlit library for creating the web-based interface and Streamlit Chat extension for displaying chat messages. The OpenAI API is employed to interact with the AI model (GPT-3.5 Turbo) for generating responses to user queries.

Overall, the code is designed to provide users with an interactive and user-friendly AI Chatbot experience, making it easy to ask questions and receive informative responses related to AI concepts.






## Screenshots

 - Chatbot-
 
 ![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Results/1.png?raw=true)

 - Asking Question-

 ![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Results/2.png?raw=true)

 - Response-

 ![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Results/3.png?raw=true)

 - Another Question-

 ![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Results/4.png?raw=true)


 - Chat-

 ![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Results/5.png?raw=true)

 - Show Messages-

 ![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Results/6.png?raw=true)

 ![](https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api/blob/main/Results/7.png?raw=true)
## Future Scope

The AI Chatbot project has tremendous potential for further enhancements and expansion. Here are some exciting possibilities for its future development:

 - Multi-Language Support: Currently, the AI Chatbot is primarily focused on answering questions related to AI in English. Expanding its capabilities to support multiple languages would make it accessible to a broader audience, catering to users from diverse linguistic backgrounds.

 - Domain-Specific Knowledge: Enhancing the chatbot's knowledge base to cover a wider range of topics within the field of AI would be valuable. It could be extended to answer questions about specific AI frameworks, algorithms, applications, and emerging trends.

 - Personalization and User Profiles: Implementing user profiles and personalized interactions would enable the chatbot to understand user preferences better. It could tailor responses based on the user's past queries and interactions, creating a more customized learning experience.

 - Interactive Learning Exercises: Integrating interactive learning exercises, quizzes, and challenges would make the AI Chatbot a more engaging and interactive learning platform. Users could test their knowledge and receive feedback from the chatbot.

 - Voice Interaction: Adding voice recognition and text-to-speech capabilities would enable users to interact with the chatbot using voice commands. This would enhance accessibility and user experience, especially for users with visual impairments.

 - Integration with AI Code Execution: Providing the ability to execute small AI code snippets within the chatbot would allow users to experiment with AI concepts and see real-time results. This hands-on approach could boost learning and practical understanding.

 - Continuous Learning and Updating: Implementing a mechanism for the chatbot to continuously learn and update its knowledge base would ensure that it stays up-to-date with the latest developments in the field of AI.

 - Support for Other AI Models: While the current version uses GPT-3.5 Turbo, integrating support for other advanced AI models and transformers would allow users to explore different language models and compare responses.

 - Feedback Collection and Improvement: Gathering user feedback and using it to refine the chatbot's responses and performance would be invaluable in making continuous improvements.

 - Integration with AI Visualizations: Incorporating AI visualization tools into the chatbot would help users understand complex AI concepts through visual representations, making learning more intuitive.

The future of the AI Chatbot project is promising, with opportunities to enhance its functionality, interactivity, and usability. By incorporating these future developments, the chatbot can become an even more powerful and comprehensive AI Tutor, catering to the ever-evolving needs of AI enthusiasts and learners.
## Contributing

We value and appreciate contributions from the community to enhance and improve the Chatbot Using ChatGPT API project. If you wish to contribute, please follow the guidelines below:

1. Fork the Repository:
Start by forking the project's repository on GitHub. This action will create a personal copy of the project under your GitHub account.

2. Clone the Repository:
Clone the forked repository to your local development environment using Git.
```bash
git clone https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api.git
cd Chatbot-Using-ChatGPT-API
```
3. Create a New Branch:
Create a new branch with a meaningful name that reflects the purpose of your contribution.
```bash
git checkout -b feature/your-contribution
```
4. Implement Changes:
Make the necessary changes and improvements to the code, documentation, or any other aspect you wish to enhance.

5. Testing:
Ensure that your changes are well-tested and do not introduce any regressions. If applicable, add appropriate unit tests.

6. Commit and Push:
Commit your changes with a clear and descriptive commit message, then push the changes to your forked repository.
```bash
git add .
git commit -m "Your descriptive commit message"
git push origin feature/your-contribution
```
7. Create a Pull Request:
Navigate to the original repository at https://github.com/abhisheksingh-17/Chatbot-Using-Chatgpt-Api.git and click on the "Pull Request" button. Fill in the details of your contribution and submit the pull request.

8. Review and Merge:
Your pull request will be reviewed by the project maintainers. They will provide feedback if necessary and, upon approval, merge your contribution into the main repository.

Code of Conduct:
Please follow a code of conduct to ensure a respectful and inclusive environment for all contributors. Please review and adhere to our code of conduct during the entire contribution process.
## License

The AI Chatbot project is distributed under the MIT License, a permissive open-source license that allows you to use, modify, and distribute the code without any restrictions. This license promotes collaboration and sharing, making it suitable for both personal and commercial projects.

Feel free to fork the project, use it for learning purposes, or integrate it into your applications. However, please be aware that any modifications or derivative works must retain the original copyright notice and include the same MIT License terms.

By contributing to the project, you agree to license your contributions under the same MIT License. For more details, refer to the LICENSE file in the project repository.