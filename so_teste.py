import platform
import getpass
from datetime import datetime

print("Nome maquina:................", platform.node())
print("Arquitetura:.................", platform.architecture())
print("Sistema Operacional:.........", platform.system())
print("Versão do SO:................", platform.release())
print("Processador:.................", platform.processor())
print("Versão do Python:............", platform.python_version())

print(datetime.now().year)

print(getpass.getuser())
print(getpass.getpass("Digite sua senha:....."))



