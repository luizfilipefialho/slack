# Slack Bot Integrado com OpenAI Assistants

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

### Adicionando Scopes de Bot

Na seção **OAuth & Permissions** do seu app no Slack, você precisará adicionar os seguintes **Scopes de Bot** para garantir que seu bot tenha as permissões necessárias para operar:

- `chat:write`: Permite que o bot envie mensagens.
- `im:history`: Permite que o bot leia mensagens em DMs.
- `users:read`: Permite que o bot acesse informações sobre os usuários do Slack.

Esses scopes são essenciais para que o bot possa enviar mensagens, ler mensagens diretas e acessar informações dos usuários para personalizar as respostas.

### Configurando Event Subscriptions

Para que o bot possa receber eventos do Slack, como mensagens enviadas por usuários, você precisará habilitar e configurar **Event Subscriptions**:

1. Navegue até a seção **Event Subscriptions** no painel do seu app Slack.
2. Ative os eventos, inserindo o URL de solicitação de eventos (Request URL) que aponta para seu servidor, por exemplo, `https://seuapp.herokuapp.com/slack/events`.
3. Adicione os seguintes **Event Types** na seção **Subscribe to bot events**:
   - `message.im`: Permite que o bot receba eventos de mensagens enviadas em mensagens diretas.

Certifique-se de que o URL de solicitação de eventos responda ao desafio de verificação do Slack com o valor `challenge` que o Slack envia quando você insere ou atualiza o URL.

### Instalando o App no Workspace do Slack

Após configurar as permissões e os eventos, não se esqueça de instalar o app no seu workspace do Slack. Isso pode ser feito na seção **Install App** no painel do seu app. Após a instalação, você receberá o **Bot User OAuth Token**, que será usado para autenticar as solicitações do seu bot ao Slack.

### Mantendo a Segurança

Lembre-se de nunca compartilhar publicamente seus tokens ou segredos de API. Utilize variáveis de ambiente para gerenciar essas informações sensíveis, tanto no desenvolvimento local quanto no deploy em plataformas como o Heroku.

Com essas configurações, seu bot do Slack estará pronto para interagir com os usuários do seu workspace, utilizando o poder da IA da OpenAI para responder às mensagens.


### Configuração do Ambiente OpenAI

1. Crie uma conta ou faça login em [https://openai.com/](https://openai.com/) e acesse a seção API para obter sua chave de API.
2. Se necessário, crie um Assistente na OpenAI para obter o ID do assistente.

### Configuração do Projeto para execução local ou servidor

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

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou uma issue.

### Licença
Open source

Originalmente feito por Luiz Fialho
