#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. (Considerar USD1.00 por R$ 3,27)

wallet = float(input('Quanto dinheiro você tem na sua carteira ? R$ '))
usd = wallet / 3.27
print ('Com R$ {:.2f} é possível comprar $ {:.2f}' .format(wallet, usd ))
