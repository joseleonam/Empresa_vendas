# Servidor/main.py
from fastapi import FastAPI
from app.service.produtos_service import ProdutosService
from app.service.compras_service import ComprasService
from app.service.financeiro_service import FinanceiroService
app = FastAPI(
    title="Sistema de Vendas API",
    version="1.0"
)

produtos_service = ProdutosService()
compras_service = ComprasService()
financeiro_service = FinanceiroService()


@app.get("/produtos")
def listar_produtos():
    return produtos_service.listar_produtos()


@app.get("/produtos/buscar")
def buscar_produtos(ids: str | None = None):
    if not ids:
        return []

    lista_ids = [int(i) for i in ids.split(",")]
    return produtos_service.buscar_produtos(lista_ids)

@app.post("/compras")
def comprar_produtos(dados: dict):
    return compras_service.comprar_produtos(
        dados["cliente"],
        dados["ids"]
    )


@app.post("/total")
def calcular_total(dados: dict):
    return financeiro_service.calcular_total(dados["ids"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)