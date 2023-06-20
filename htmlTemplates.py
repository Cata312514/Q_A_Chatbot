css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="streamlit
streamlit-chat
openai
python-dotenv
langchain
pypdf2
beautifulsoup4
pinecone-client
unstructured

https://github.com/Cata312514/Q_A_Chatbot/blob/9be6b6472d5e350542fb0f000800b6daf169085f/chatbot.JPG" alt="Smart PDF Chatbot" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="streamlit
streamlit-chat
openai
python-dotenv
langchain
pypdf2
beautifulsoup4
pinecone-client
unstructured

https://github.com/Cata312514/Q_A_Chatbot/blob/9be6b6472d5e350542fb0f000800b6daf169085f/chatbot.JPG" alt="user">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''