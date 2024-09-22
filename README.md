# Apple Product & FAQ Chatbot

## Overview

This project is an interactive chatbot built using Streamlit and LangChain that provides Apple product recommendations and answers FAQs by retrieving real-time data from the official Apple website. It leverages advanced language models and embedding techniques to deliver accurate and helpful responses to user queries.

## Key Features

- **Product Recommendation**: Based on user input, the bot suggests Apple products, providing descriptions, features, and direct links to the Apple store.
- **FAQ Handling**: It can answer common customer questions by fetching relevant data from the Apple website.
- **Advanced Document Retrieval**: Uses Mistral AI for document embedding and FAISS for efficient retrieval from split chunks of web data.
- **Conversational Memory**: Keeps track of the conversation flow using `ConversationBufferWindowMemory`, enhancing user interaction.

## Tech Stack

- **LangChain**: For managing language models and chains.
  - **Groq Llama 3.1**: The language model used for generating responses.
  - **Mistral AI**: Used for generating embeddings for document retrieval.
- **FAISS**: A library for efficient document retrieval using embeddings.
- **Streamlit**: Framework for building the chatbot interface.
- **Web Scraping**: Fetches live data from Apple’s official website for product information and FAQs.
- **Streamlit-Chat**: To display the conversation in a chat-like format.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/apple-product-faq-chatbot.git
   cd apple-product-faq-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your API keys for Groq and Mistral:
   ```
   export GROQ_API_KEY='your-groq-api-key'
   export MISTRALAI_API_KEY='your-mistralai-api-key'
   ```
4. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

## Usage
- Once the app is running, enter your query into the text input box (e.g., "I am looking for a new iPhone").
- The chatbot will recommend a product along with a detailed description and provide a link to view it on the Apple website.
- The bot can also answer any FAQs related to Apple products or services.

## Future Improvements
- Add multi-language support for international users.
- Include a wider range of product categories and specific user preferences.
- Enhance the chatbot's capability to handle more complex customer support queries.

## Contact

If you have any questions or feedback, feel free to reach out to me via:

- LinkedIn: [Pratirath Gupta](https://www.linkedin.com/in/pratirathgupta/)
- Email: pratirathgupta51@gmail.com

Happy Coding!

Brought by, Pratirath Gupta!
