# Eureka Slack Bot

Eureka is a Slack bot that uses LangChain and OpenAI to have smart conversations. It learns from personal information to talk in a way that feels personal and makes sense. It can also search the internet to give better answers and help more effectively.

## Demo of Current Progress

.
.
.
.

## Key Features Developed So Far

- ✅ The bot only responds when mentioned in the Slack channel
- ✅ Utilizes LangChain and OpenAI to have intelligent conversations
- ✅ Eureka learns from specific personal data to provide personalized and relevant interactions
- ✅ Capable of fetching online information to supplement responses
- ❌ Instead of fetching data from a local folder, Eureka will integrate with a vector database for improved performance and scalability
- ❌ Ability to handle and read schedules from my personal calendar
- ❌ Scheduling feature to send reminders or automated messages at specific times
- ❌ Integration with external APIs to perform specific tasks, such as fetching news, etc
- ❌ Multimedia responses, including sending relevant images, videos, or files

## Technologies Used

- LangChain: Framework for enabling intelligent conversations and natural language processing.
- OpenAI: AI platform used for generating human-like text and understanding language.
- Vector Database Integration: Utilizes a vector database for efficient data storage and retrieval, enhancing performance and scalability.
- Slack SDK: Software development kit for building Slack integrations and bots.
- Python: Programming language used for implementing Eureka's functionality.
- Other Libraries and Tools: Additional dependencies specified in the requirements.txt file to support various features and functionalities of Eureka.

## Running the Bot

To run the bot, execute the `main.py` file:

```bash
python src/main.py
```

## Want to Contribute?

Please read our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) for more details.

## Contributors

- @mkafonso

----------------------------------------------- 
.
.
.
.
.
.
.
# TESTES QUE FIZ RECENTEMENTE
.
.
.
.
.
.
.
----------------------------------------------- 


* É tranquilo gerar esses embeddings com a OpenAI
  
![Screen Shot 2024-04-09 at 23 03 51](https://github.com/mkafonso/eureka/assets/73212666/e03e9105-c868-4675-b13a-bafee5ebfdec)


* Depois de pegar o array dos números, precisamos salvar num banco de dados vetorial. Escolhi o SingleStore: https://www.singlestore.com/

* Cria um workspace, database e depois uma tabela
![Screen Shot 2024-04-09 at 22 58 37](https://github.com/mkafonso/eureka/assets/73212666/6070f530-0ca1-4f30-9444-0af4930f8d0f)

  

* Cadastrar os dados
![Screen Shot 2024-04-09 at 23 21 18](https://github.com/mkafonso/eureka/assets/73212666/fffdf082-b034-4ba6-9e8f-b7e334676736)




* Exagerei e quis subir todo script do filme Shrek 😅 e o modelo reclamou.

![Screen Shot 2024-04-09 at 23 31 18](https://github.com/mkafonso/eureka/assets/73212666/8e3e5f73-4cd6-4b8e-b401-fc8976209f40)



