from celery import shared_task


@shared_task
def processar_produto(produto_id):
    print(f"[Fila PRODUTOS] Processando produto {produto_id}")


@shared_task
def atualizar_estoque(produto_id):
    print(f"[Fila ESTOQUE] Atualizando estoque do produto {produto_id}")
