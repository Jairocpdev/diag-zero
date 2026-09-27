# diag-zero

> Diagnostica e resolve bugs em segundos. Sem API. Sem chave. Só Python puro.

Um troubleshooter CLI de 28 linhas que roda offline. Ideal pra quem tá começando em IA mas quer algo útil de verdade.

### Por que?

Todo troubleshooter hoje depende de OpenAI/Groq. Esse não. Ele usa um dicionário de padrões + regex pra entender o problema e cuspir a solução. Rápido, leve e 100% seu.

### Como funciona
1. Você descreve o erro: `wifi não conecta` ou `ModuleNotFoundError: pandas`
2. O script casa com um padrão regex em `BASE`
3. Retorna: CAUSA PROVÁVEL + 3 PASSOS + COMANDO FINAL