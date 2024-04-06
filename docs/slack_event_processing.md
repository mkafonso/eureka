## Configuração do Servidor Flask com SlackEventAdapter

O servidor Flask utiliza o SlackEventAdapter para lidar com eventos recebidos do Slack. Quando ocorre um evento, o payload correspondente é enviado para a rota '/slack/events' do servidor Flask.

## Processamento Assíncrono dos Eventos do Slack

Ao invés de processar os eventos diretamente na rota '/slack/events', os payloads dos eventos são colocados em uma fila chamada `slack_event_queue`. Isso permite que o servidor lide com múltiplos eventos de forma assíncrona e evita atrasos ou bloqueios na resposta ao Slack.

Um novo thread chamado processing_thread é iniciado para processar os eventos assincronamente. Esse thread executa a função process_slack_events, que continua consumindo os eventos da fila e os processa usando o SlackBot.

## Persistência dos Eventos na Fila

Uma observação importante é que mesmo após reiniciar o servidor Flask, os eventos salvos na fila `slack_event_queue` permanecem acessíveis. Isso `garante que nenhum evento seja perdido durante reinicializações` ou atualizações do servidor. Os eventos pendentes na fila são processados pelo processing_thread assim que o servidor é reiniciado, garantindo uma resposta contínua e resiliente aos eventos do Slack.
