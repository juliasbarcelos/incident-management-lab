import logging
from pathlib import Path

# Preparar a pasta dos logs
pasta_logs = Path(__file__).resolve().parent / "logs"
pasta_logs.mkdir(exist_ok=True)

logging.basicConfig(
    filename=pasta_logs / "validacao-auth.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Utilizadores fictícios do laboratório
utilizadores = {
    "ana.martins": ["reports.read", "orders.read"],
    "bruno.costa": ["reports.read"],
}

def verificar_acesso(utilizador, permissoes):
    logging.info("Login request received | user=%s", utilizador)

    # Autenticação simulada
    logging.info("Authentication successful | user=%s", utilizador)

    if "orders.read" not in permissoes:
        logging.warning(
            "Access denied | user=%s | missing=orders.read",
            utilizador,
        )
        logging.warning("HTTP 403 Forbidden (simulated)")
        print(f"{utilizador}: Acesso negado — 403 simulado")
        return

    logging.info("Access granted | user=%s", utilizador)
    print(f"{utilizador}: Acesso autorizado")


for utilizador, permissoes in utilizadores.items():
    verificar_acesso(utilizador, permissoes)
