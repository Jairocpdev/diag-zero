import re

BASE = {
    "wifi|internet|dns|rede": ["DNS travado ou roteador", "1. ping 8.8.8.8 | 2. ipconfig /flushdns | 3. reinicie roteador", "netsh winsock reset"],
    "python|pip|ModuleNotFound|ImportError": ["Dependência faltando", "1. confira venv | 2. pip install -r requirements.txt | 3. python -m pip list", "pip install <pacote>"],
    "lento|travando|100% cpu|memoria": ["Processo consumindo recurso", "1. Task Manager / top | 2. feche abas | 3. verifique startup", "ctrl+shift+esc -> finalizar tarefa"],
}

problema = input("Qual o problema? ").lower()
for padrao, (causa, passos, cmd) in BASE.items():
    if re.search(padrao, problema):
        print(f"\nCAUSA: {causa}\nPASSOS:\n{passos}\nCOMANDO: {cmd}")
        break
else:
    print("Não mapeado. Tente descrever com: erro + o que você fez antes.")