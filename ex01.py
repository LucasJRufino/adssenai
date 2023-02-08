n1 = float(input("Entre com n1"))
n2 = float(input("Entre com n2"))
n3 = float(input("Entre com n3"))

me = float(input("Qual a média de atividades"))
ma = (n1 + n2 * 2 + n3 * 3 +me) / 7

if ma < 4:
    print("Aluno Reprovado!")
else:
    print("Aluno Aprovado!")

print(ma) 
