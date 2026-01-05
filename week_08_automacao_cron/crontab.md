# Documentação de Agendamento (Cron)

Como estou rodando em Windows, utilizei o Task Scheduler apontando para o arquivo `run_etl.bat`.
Porém, se este projeto estivesse em um servidor Linux, esta seria a configuração do Crontab:

## Sintaxe do Cron
# ┌───────────── minuto (0 - 59)
# │ ┌───────────── hora (0 - 23)
# │ │ ┌───────────── dia do mês (1 - 31)
# │ │ │ ┌───────────── mês (1 - 12)
# │ │ │ │ ┌───────────── dia da semana (0 - 6) (Domingo a Sábado)
# │ │ │ │ │
# * * * * * <comando a ser executado>

## Exemplos para meu Projeto

### 1. Rodar todo dia às 08:00 da manhã
0 8 * * * /usr/bin/python3 /app/etl.py --source /data/dados.csv

### 2. Rodar toda segunda-feira às 09:30
30 9 * * 1 /usr/bin/python3 /app/etl.py --source /data/dados.csv

### 3. Rodar de hora em hora (minuto zero)
0 * * * * /usr/bin/python3 /app/etl.py --source /data/dados.csv