# diag-zero - app.py
import re

BASE = {
    "wifi|internet|dns|rede|sem conexao": ["DNS ou roteador travado", "1. ping 8.8.8.8\n2. ipconfig /flushdns\n3. Reinicie o roteador", "netsh winsock reset"],
    "python|pip|ModuleNotFound|ImportError|ModuleNot": ["Dependência faltando", "1. Ative a venv: source venv/bin/activate\n2. pip install -r requirements.txt\n3. Verifique o nome do pacote", "pip install <nome-do-pacote>"],
    "lento|travando|cpu 100|memoria": ["Processo consumindo recurso", "1. Abra Gerenciador de Tarefas\n2. Ordene por CPU/Memória\n3. Finalize a tarefa pesada", "Ctrl+Shift+Esc"],
    "docker|porta em uso|address already": ["Conflito de porta", "1. docker ps\n2. docker stop <id>\n3. Tente novamente", "lsof -i :3000"],
    "git|merge|conflict": ["Conflito de merge", "1. git status\n2. Resolva os arquivos marcados\n3. git add. && git commit", "git merge --abort para desfazer"],
}

def main():
    p = input("Descreva o erro: ").lower()
    for pattern, (causa, passos, cmd) in BASE.items():
        if re.search(pattern, p):
            print(f"\n[CAUSA] {causa}\n\n[PASSOS]\n{passos}\n\n[COMANDO]\n{cmd}")
            return
    print("\nNão mapeei ainda. Tenta ser mais específico: 'erro X ao fazer Y'")

if __name__ == "__main__":
    main()