#!/bin/bash

# --- CONFIGURACAO ---
PG_USER="postgres"
PG_HOST="localhost"
PG_PORT="5432"
DB_ORIGEM="postgres"
DB_DESTINO="postgres_teste_restore"
ARQUIVO_BACKUP="backup_loja.dump"

# --- CAMINHO ---
PG_BIN="C:/Users/matheus.r/pgsql/bin"

# Define a senha
export PGPASSWORD="admin"

echo "----------------------------------------"
echo "1. Iniciando Backup (Dump) do banco..."
echo "----------------------------------------"

# Executa o dump
"$PG_BIN/pg_dump.exe" -U $PG_USER -h $PG_HOST -p $PG_PORT -F c -d $DB_ORIGEM -f $ARQUIVO_BACKUP

if [ -f "$ARQUIVO_BACKUP" ]; then
    echo "[SUCESSO] Arquivo de backup criado: $ARQUIVO_BACKUP"
else
    echo "[ERRO] O arquivo de backup nao foi criado."
    echo "Caminho testado: $PG_BIN"
    exit 1
fi

echo ""
echo "----------------------------------------"
echo "2. Criando banco de teste para restore..."
echo "----------------------------------------"

# Cria o banco novo
"$PG_BIN/createdb.exe" -U $PG_USER -h $PG_HOST -p $PG_PORT $DB_DESTINO || true

echo ""
echo "----------------------------------------"
echo "3. Restaurando dados no banco novo..."
echo "----------------------------------------"

# Restaura o backup
"$PG_BIN/pg_restore.exe" -U $PG_USER -h $PG_HOST -p $PG_PORT -d $DB_DESTINO -c $ARQUIVO_BACKUP

# Remove a senha
unset PGPASSWORD

echo ""
echo "----------------------------------------"
echo "PROCESSO FINALIZADO COM SUCESSO."
echo "----------------------------------------"