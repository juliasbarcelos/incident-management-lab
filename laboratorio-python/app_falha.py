import logging
from pathlib import Path

# Criar a pasta para guardar os logs
pasta_logs = Path("logs")
pasta_logs.mkdir(exist_ok=True)

# Configurar o sistema de registos
logging.basicConfig(
    filename=pasta_logs / "application-auth.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Dados fictícios da utilizadora
utilizadora = "ana.martins"
perfil = "Financeiro_Restrito"
permissoes = ["reports.read"]

def iniciar_sessao():
    logging.info("Login request received | user=%s", utilizadora)

    # Simulação de autenticação bem-sucedida
    logging.info("Authentication successful | user=%s", utilizadora)

    # Verificação de autorização
    if "orders.read" not in permissoes:
        logging.error("Permission validation failed")
        logging.error("Role: %s", perfil)
        logging.error("Missing permission: orders.read")
        logging.error("HTTP 500 returned (simulated)")

        print("Erro 500 — Internal Server Error (simulado)")
        return

    logging.info("Access granted")
    print("Acesso autorizado")


iniciar_sessao()
