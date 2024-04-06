# Eureka Slack Bot

Eureka é um bot para Slack que utiliza tecnologias como LangChain e OpenAI para oferecer funcionalidades avançadas de conversação. O bot é alimentado com dados pessoais específicos, permitindo interações personalizadas e contextualmente relevantes. Além disso, ele é capaz de buscar referências na internet para enriquecer suas respostas e oferecer suporte mais abrangente.

## Principais recursos até agora

- ✅ O bot só responde quando é mencionado no canal do Slack
- ✅ Utiliza LangChain e OpenAI para processar e responder as perguntas de forma inteligente
- ✅ Oferece interações personalizadas com base nos dados pessoais fornecidos
- ✅ Capacidade de buscar informações online para complementar as respostas
- ❌ Capacidade de ler dados de uma pasta com varios arquivos
- ❌ Capacidade de manipular e ler horários da minha agenda pessoal
- ❌ Recurso de agendamento para enviar lembretes ou mensagens automatizadas em horários específicos
- ❌ Integração com APIs externas para realizar tarefas específicas, como buscar notícias, etc
- ❌ Respostas multimídia, incluindo envio de imagens, vídeos ou arquivos relevantes

## Tecnologias Utilizadas

- LangChain: Framework para processamento de linguagem natural
- OpenAI: Plataforma de IA para geração de linguagem natural e aprendizado de máquina
- Outras Bibliotecas e Ferramentas: Python e outras dependências que podem ser encontradas no arquivo `requirements.txt`

## Configuração

1. **Instalação das dependências:**

```bash
pip3.11 install -r requirements.txt
```

2. **Configuração das variáveis de ambiente:**

- Crie um arquivo chamado `.env` na raiz do projeto com o mesmo conteúdo de `.env.example`
- Defina as variáveis de ambiente necessárias no formato `CHAVE=VALOR`.
  Exemplo:
  ```
  OPENAI_API_KEY=seu_token_da_open_ai
  ```
- Adicione algumas informações no arquivo `data.txt`

## Executando o Bot

Para executar o bot, execute o arquivo `main.py`:

```bash
python src/main.py
```

## Por que você fez isso?

🚨 Este projeto é uma demonstração do poder das tecnologias de IA aplicadas à comunicação por chat, oferecendo um assistente virtual sofisticado com capacidades de aprendizado e personalização. Sinta-se à vontade para explorar, contribuir e adaptar o código conforme necessário para suas próprias aplicações!

## Quer contribuir?

Por favor, leia o nosso [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) para mais detalhes.

## Contribuidores

- @mkafonso
