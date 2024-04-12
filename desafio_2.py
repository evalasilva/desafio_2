def calcular_media(valores):
    try:
        soma = sum(valores)
        media = soma / len(valores)
        return media
    except ZeroDivisionError:
        print("Lista vazia.")
        return None
    except TypeError:
        print("Não é um dígito.")
        return None
    except Exception as e:
        print("Ocorreu um erro ao calcular a média:", e)
        return None

valores = []
while True:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        break
    try:
        valor = float(valor)
        valores.append(valor)
    except ValueError:
        print("Digite um número válido.")

media = calcular_media(valores)
if media is not None:
    print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))
