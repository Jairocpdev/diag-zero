# diag-zero

> Diagnostica e resolve bugs em segundos. Sem API. Sem chave. Só Python puro.

Um troubleshooter CLI de 28 linhas que roda offline. Ideal pra quem tá começando em IA mas quer algo útil de verdade.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![No Deps](https://img.shields.io/badge/deps-zero-black)

### Por que?

Todo troubleshooter hoje depende de OpenAI/Groq. Esse não. Ele usa um dicionário de padrões + regex pra entender o problema e cuspir a solução. Rápido, leve e 100% seu.

### Como funciona

1.  Você descreve o erro: `wifi não conecta` ou `ModuleNotFoundError: pandas`
2.  O script casa com um padrão regex em `BASE`
3.  Retorna: **CAUSA PROVÁVEL + 3 PASSOS + COMANDO FINAL**

### Como usar

```bash
git clone https://github.com/Jairocpdev/diag-zero.git
cd diag-zero
python app.py
