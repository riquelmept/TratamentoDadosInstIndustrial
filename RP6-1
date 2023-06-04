import matplotlib.pyplot as plt

# Dados
dt = ["00:00", "00:30,5", "00:29,8", "00:31,0", "00:31,1", "00:31,9", "00:32,3", "00:32,0"]
tq1 = [60, 63, 67, 70, 74, 77, 81, 84]
tq2 = [80, 70, 60, 50, 40, 30, 20, 10]
fit = [1.3368, 1.324, 1.3224, 1.3182, 1.3187, 1.3205, 1.3188, 1.3145]

# Gráfico TQ1 x DT
plt.figure()
plt.plot(dt, tq1, marker='o')
plt.xlabel('DT (mm:ss)')
plt.ylabel('TQ1 (%)')
plt.title('TQ1 x DT')
plt.grid(True)
plt.show()

# Gráfico TQ2 x DT
plt.figure()
plt.plot(dt, tq2, marker='o')
plt.xlabel('DT (mm:ss)')
plt.ylabel('TQ2 (%)')
plt.title('TQ2 x DT')
plt.grid(True)
plt.show()

# Gráfico FIT x DT
plt.figure()
plt.plot(dt, fit, marker='o')
plt.xlabel('DT (mm:ss)')
plt.ylabel('FIT (m³/h)')
plt.title('FIT x DT')
plt.grid(True)
plt.show()
