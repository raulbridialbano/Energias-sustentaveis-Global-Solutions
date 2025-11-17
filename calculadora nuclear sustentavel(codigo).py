#inserir dados de população e área de uma respectiva cidade
from urllib.response import addbase

pop = int(input('Digite a populacao: '))



if pop <= 1000000:
    Status = 'Energias sustentaveis'
    ConMen = (pop * 162)
    custo= (0.079335 * ConMen)

else:
    Status = 'Energias nuclear'
    usinas = 0
    for i in range(1, pop, 1750000):
        usinas += 1
    custo= (usinas * 1750000)
    ConMen = (pop * 162)
    print('Quantidde usinas é de', usinas)

print(f'Pra essa cidade recomendamos uso de {Status}')
print(f'O consumo mensal de energia é de  {ConMen} kWh' )

print(f'O custo de instalar essa usina/gerador vai ser de {custo}'.2f)
