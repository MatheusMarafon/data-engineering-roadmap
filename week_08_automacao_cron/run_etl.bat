@echo off
:: Define os caminhos
SET PYTHON_EXE=C:\Users\matheus.r\Desktop\data-engineering-roadmap\.venv\Scripts\python.exe
SET SCRIPT_PATH=C:\Users\matheus.r\Desktop\data-engineering-roadmap\week_08_automacao_cron\python\etl.py
SET DATA_PATH=C:\Users\matheus.r\Desktop\data-engineering-roadmap\week_08_automacao_cron\csv\dados.csv

:: Executa o script
echo Iniciando ETL...
"%PYTHON_EXE%" "%SCRIPT_PATH%" --source "%DATA_PATH%"

:: Mantem a tela aberta por 5 segundos para voce ver o resultado
timeout /t 5