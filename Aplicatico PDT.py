def calcular_vcexato(vcc, resistencia_coletor, corrente_coletor, resistencia_emissor, corrente_emissor):
    tensao_coletor_emissor = vcc - (resistencia_coletor * corrente_coletor) - (resistencia_emissor * corrente_emissor)
    return tensao_coletor_emissor


def calcular_ic(corrente_base, beta_transistor):
    corrente_coletor = corrente_base * beta_transistor
    return corrente_coletor


def calcular_iesimples(tensao_emissor, resistencia_emissor):
    Ie = tensao_emissor / resistencia_emissor
    return Ie


def calcular_vcesimples(tensao_coletor, tensao_emissor):
    Vce = tensao_coletor - tensao_emissor
    return Vce


def calcular_vc(vcc, resistencia_coletor, corrente_coletor):
    tensaao_coletor = vcc - resistencia_coletor * corrente_coletor
    return tensaao_coletor


def calcular_vth(resistencia2, resistencia1, vcc):
    Vth = resistencia2 / (resistencia1 + resistencia2)
    Vth = Vth * vcc
    return Vth


def calcular_ve(resistencia_emissor, corrente_emissor):
    tensao_emissor = resistencia_emissor * corrente_emissor
    return tensao_emissor


def calcular_ib(vcc, rth, resistencia_emissor, beta_transistor):
    corrente_base = (vcc - 0.7) / (rth + (beta_transistor + 1) * resistencia_emissor)
    return corrente_base


while True:
    print('#' * 50)
    # Desicão de escolha
    escolha = input('Quer calcular? [s] ou [n]: ')
    if escolha == 's':
        r1 = float(input('Digite o valor de R1: '))
        r2 = float(input('Digite o valor de R2: '))
        rc = float(input('Digite o valor de Rc: '))
        re = float(input('Digite o valor de Re: '))
        beta = float(input('Digite o valor de beta: '))
        tensao_de_alimentacao = float(input('Digite o valor da tensão de alimentação: '))
        # Calculo do paralelo da Resistência 1 com a Resistênci 2
        teste = (r1 * r2) / (r1 + r2)
        dez_do_beta = 0.1 * beta * re
        # metódo simplificado
        if teste < dez_do_beta:
            vth = calcular_vth(r2, r1, tensao_de_alimentacao)
            ve = vth - 0.7
            ie = calcular_iesimples(ve, re)
            ic = ie
            ib = ic / beta
            vc = calcular_vc(tensao_de_alimentacao, rc, ic)
            vce = calcular_vcesimples(vc, ve)
            print('#' * 50)
            print(f"    Vth = {vth:.2f} V")
            print(f"    Ve = {ve:.2f} V")
            print(f"    Ic = {ic:.6f} A")
            print(f"    Ie = {ic:.6f} A")
            print(f"    Vc = {vc:.2f} V")
            print(f"    Vce = {vce:.2f} V")
            print(f"    Ib = {ib} A")
            print('Show, deu certo!'.format())
        else:
            # Metodo exato
            vth = calcular_vth(r2, r1, tensao_de_alimentacao)
            ib = calcular_ib(vth, teste, re, beta)
            ic = calcular_ic(ib, beta)
            ie = (beta + 1) * ib
            vce = calcular_vcexato(tensao_de_alimentacao, rc, ic, re, ie)
            vc = calcular_vc(tensao_de_alimentacao, rc, ic)
            ve = calcular_ve(re, ie)
            print('#' * 50)
            print(f"    Valor de Vb = {vth:.2f} V")
            print(f"    Valor de Ib = {ib} A")
            print(f"    Valor de Ic = {ic} A")
            print(f"    Valor de Ie = {ie} A")
            print(f"    Valor de Vce = {vce:.2f} ")
            print(f"    Valor de Vc = {vc:.2f} V")
            print(f"    Valor de Ve = {ve:.2f} V")
            print('             Show, deu certo!')
    elif escolha != 's' or escolha != 'n':
        # Bloco de codigos para evitar o progama de fechar
        print(f'Você digitou uma opção inválida, por favor digie apenas "s" para sim, ou, "n" para não')
        print()
        continue
    else:
        print('PROGAMA ENCERRADO COM SUCESSO, SHOW!')
        break
