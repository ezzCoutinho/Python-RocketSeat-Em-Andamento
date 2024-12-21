while True:
  print("\n Menu de Gerenciador da Lista de Tarefas:")
  print("1. Adicionar Tarefas")
  print("2. Ver Tarefas")
  print("3. Atualizar Tarefas")
  print("4. Completar Tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = int(input("Escolha uma opção da Lista de Tarefas:"))

  if escolha == 6:
    print("Saindo da Lista de Tarefas...")
    break
  else:
    print("Escolha inválida.")