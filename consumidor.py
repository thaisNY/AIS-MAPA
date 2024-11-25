import boto3

# Criar cliente do S3
s3 = boto3.client('s3')

# Nome do arquivo baixado localmente
LOCAL_FILE = 'zomato.csv'

# Baixar o arquivo do S3
try:
    s3.download_file(BUCKET_NAME, FILE_KEY, LOCAL_FILE)
    print(f"Arquivo baixado com sucesso: {LOCAL_FILE}")
except Exception as e:
    print("Erro ao baixar arquivo:", e)
