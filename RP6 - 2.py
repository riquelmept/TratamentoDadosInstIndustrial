import matplotlib.pyplot as plt

# Dados
rotacao = [1804, 1709, 1605, 1501, 1401, 1305, 1203, 1100, 999, 901, 803, 700, 602]
tq1 = [62, 64, 66, 68, 69, 69, 69, 69, 69, 67, 66, 64, 61]
tq2 = [80, 33, 61, 57, 53, 52, 51, 52, 53, 57, 61, 67, 75]
fit = [1.1545, 1.0752, 0.9847, 0.9004, 0.8777, 0.7426, 0.6557, 0.5688, 0.4762, 0.385, 0.2818, 0.1547, 0.0155]

# Gráfico TQ1 x Rotação
plt.figure()
plt.plot(rotacao, tq1, marker='o')
plt.xlabel('Rotação (RPM)')
plt.ylabel('TQ1 (%)')
plt.title('TQ1 x Rotação')

# Gráfico TQ2 x Rotação
plt.figure()
plt.plot(rotacao, tq2, marker='o')
plt.xlabel('Rotação (RPM)')
plt.ylabel('TQ2 (%)')
plt.title('TQ2 x Rotação')

# Gráfico FIT x Rotação
plt.figure()
plt.plot(rotacao, fit, marker='o')
plt.xlabel('Rotação (RPM)')
plt.ylabel('FIT (m³/h)')
plt.title('FIT x Rotação')

# Exibir os gráficos
plt.show()