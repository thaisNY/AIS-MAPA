import boto3

# Configurações do AWS S3
BUCKET_NAME = 'ais-proj-final'
FILE_PATH = 'C:\Users\thais\Documents\zomato.csv'  # Caminho do arquivo que você enviou
S3_KEY = 'AisDados.csv'  # Nome do arquivo no S3

# Criar cliente do S3
s3 = boto3.client('s3')

# Fazer upload do arquivo
try:
    s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
    print(f"Arquivo {S3_KEY} enviado com sucesso para o bucket {BUCKET_NAME}.")
except Exception as e:
    print("Erro ao fazer upload:", e)
