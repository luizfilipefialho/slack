markdown
Copy code
# Slack Bot Integrado com OpenAI

Este projeto é um bot do Slack que utiliza a API da OpenAI para responder mensagens em DMs (mensagens diretas) com respostas geradas por IA. Ele é construído usando Flask para o backend e a biblioteca `slack_bolt` para a integração com o Slack, além da biblioteca `openai` para a comunicação com a API da OpenAI.

## Funcionalidades

- Responde a mensagens diretas no Slack com conteúdo gerado por um assistente utilizando IA da OpenAI.
- Utiliza threads da OpenAI para manter o contexto das conversas.
- Segurança aprimorada com variáveis de ambiente para tokens e chaves de API.

## Pré-requisitos

Antes de começar, você precisará:

1. **Criar um App no Slack**: Para receber um token de bot e um segredo de assinatura.
2. **Obter as Chaves da API da OpenAI**: Para autenticar suas solicitações à OpenAI.
3. **Python 3.6+**: O código é escrito para ser compatível com Python 3.6 ou superior.

## Configuração

### Configuração do Ambiente Slack

1. Acesse [https://api.slack.com/apps](https://api.slack.com/apps) e crie um novo app.
2. Na seção **OAuth & Permissions**, adicione as permissões necessárias e gere um **Bot User OAuth Token**.
3. Em **Basic Information**, encontre o **Signing Secret**.

### Configuração do Ambiente OpenAI

1. Crie uma conta ou faça login em [https://openai.com/](https://openai.com/) e acesse a seção API para obter sua chave de API.
2. Se necessário, crie um Assistente na OpenAI para obter o ID do assistente.

### Configuração do Projeto

1. Clone este repositório.
2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   
- SLACK_BOT_TOKEN=seu_token_de_bot_slack_aqui
- SLACK_SIGNING_SECRET=seu_secreto_de_assinatura_slack_aqui
- OPENAI_API_KEY=sua_chave_api_openai_aqui
- OPENAI_ASSISTANT_ID=id_do_seu_assistente_openai_aqui
- SLACK_CHANNEL_WEBHOOKURL=(opcional) para utilizar o módulo de envio de mensagens para canais sendmessage.py

4. Instale as dependências executando `pip install -r requirements.txt`.


## Executando o Bot no Heroku

Este projeto está pronto para ser executado no Heroku. Após fazer o deploy no Heroku, certifique-se de configurar as variáveis de ambiente no painel do Heroku.

Para que o Slack envie eventos para o seu bot, aponte o URL de solicitação de eventos do Slack (`Request URL`) para `https://seuapp.herokuapp.com/slack/events`, substituindo `seuapp.herokuapp.com` pelo nome do seu app no Heroku.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou uma issue.

Licença
Open source

Lembre-se de ajustar os detalhes conforme necessário, especialmente nas seções de configuração e execução, para garantir que estejam alinhados com as especificidades do seu projeto.
