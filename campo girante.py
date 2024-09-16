import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definir parâmetros
H = 1  # Amplitude do campo magnético
omega = 2 * np.pi  # Frequência angular (ajustável)
t = np.linspace(0, 2*np.pi, 500)  # Intervalo de tempo

# Definir as componentes do campo magnético
H_a = lambda t: H * np.sin(omega * t)
H_b = lambda t: H * np.sin(omega * t - 2*np.pi/3)  # Defasagem de -120°
H_c = lambda t: H * np.sin(omega * t + 2*np.pi/3)  # Defasagem de +120°

# Preparar a figura para a animação
fig, ax = plt.subplots()
ax.set_xlim(-1.5*H, 1.5*H)
ax.set_ylim(-1.5*H, 1.5*H)
ax.set_aspect('equal')

# Configurar as setas vetoriais para H_a, H_b, H_c e o vetor resultante
arrow_a = ax.quiver(0, 0, 0, 0, color='r', angles='xy', scale_units='xy', scale=1, label='$H_a$')
arrow_b = ax.quiver(0, 0, 0, 0, color='g', angles='xy', scale_units='xy', scale=1, label='$H_b$')
arrow_c = ax.quiver(0, 0, 0, 0, color='b', angles='xy', scale_units='xy', scale=1, label='$H_c$')
arrow_result = ax.quiver(0, 0, 0, 0, color='k', angles='xy', scale_units='xy', scale=1, label='Campo resultante')

# Função de inicialização
def init():
    arrow_a.set_UVC(0, 0)
    arrow_b.set_UVC(0, 0)
    arrow_c.set_UVC(0, 0)
    arrow_result.set_UVC(0, 0)
    return arrow_a, arrow_b, arrow_c, arrow_result

# Função de animação
def animate(i):
    t_val = t[i]
    
    # Componentes dos vetores H_a, H_b, H_c
    H_a_x, H_a_y = H_a(t_val), 0
    H_b_x, H_b_y = H_b(t_val) * np.cos(2*np.pi/3), H_b(t_val) * np.sin(2*np.pi/3)
    H_c_x, H_c_y = H_c(t_val) * np.cos(-2*np.pi/3), H_c(t_val) * np.sin(-2*np.pi/3)
    
    # Resultante
    H_res_x = H_a_x + H_b_x + H_c_x
    H_res_y = H_a_y + H_b_y + H_c_y
    
    # Atualizar as setas (U, V são os componentes x e y das setas)
    arrow_a.set_UVC(H_a_x, H_a_y)
    arrow_b.set_UVC(H_b_x, H_b_y)
    arrow_c.set_UVC(H_c_x, H_c_y)
    arrow_result.set_UVC(H_res_x, H_res_y)
    
    return arrow_a, arrow_b, arrow_c, arrow_result

ax.grid()
ax.legend()

# Configurar a animação
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, interval=20, blit=True)

ani.save('campo girante lento.mp4')

plt.show()
