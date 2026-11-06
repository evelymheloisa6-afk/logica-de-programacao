
cadastros = [
    {"nome": "Ana Lyvia", "idade": 18, "curso": "Informática"},
    {"nome": "Eduardo", "idade": 16, "curso": "Informática"}
]


novo_aluno = {
    "nome": input("Digite o nome do aluno: "),
    "idade": int(input("Digite a idade do aluno: ")),
    "curso": input("Digite o curso do aluno: ")
}
cadastros.append(novo_aluno)


cadastros.append({
    "nome": "Evelym",
    "idade": 16,
    "curso": "Informática"
})

cadastros.append({
    "nome": "Anilca",
    "idade": 16,
    "curso": "Informática"
})


print("\nAlunos cadastrados:")

for aluno in cadastros:
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")
    print(f"Curso: {aluno['curso']}")
    print("-" * 30)
