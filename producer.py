# import os, django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
# django.setup()

# from demoapp.tasks import processar_produto, atualizar_estoque


# def enviar_produto(produto_id):
#     processar_produto.apply_async(
#         args=[produto_id],
#         routing_key="produtos",
#         exchange="produtos_exchange",
#     )
#     atualizar_estoque.apply_async(
#         args=[produto_id],
#         routing_key="estoque",
#         exchange="produtos_exchange",
#     )


# if __name__ == "__main__":
#     enviar_produto(123)
#     print("Produto 123 enviado!")


import os, django
from celery import signature

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()


def enviar_produto(produto_id):
    # cria assinatura da task pelo nome registrado
    sig_produto = signature(
        "demoapp.tasks.processar_produto",
        args=[produto_id],
        options={
            "exchange": "produtos_exchange",
            "routing_key": "produtos",
        },
    )

    sig_estoque = signature(
        "demoapp.tasks.atualizar_estoque",
        args=[produto_id],
        options={
            "exchange": "produtos_exchange",
            "routing_key": "estoque",
        },
    )

    # dispara
    # sig_produto.apply_async()
    # sig_estoque.apply_async()

    sig_produto.delay()
    sig_estoque.delay()


if __name__ == "__main__":
    enviar_produto(123)
    print("Produto 123 enviado para as filas produtos e estoque!")
