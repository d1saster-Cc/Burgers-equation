import numpy as np
import matplotlib.pyplot as plt

def expl_2(f, init, bound1, bound2, a, b, h, tau, t_end, eps):
    size_h = int(abs(b - a) / h) + 1
    
    u_0 = np.zeros(size_h)
    for i in range(0, size_h):
      u_0[i] = init(a + i * h)

    plt.figure(figsize=(10, 7))
    plt.plot(u_0)
    # plt.show()

    u_1 = np.zeros(size_h)
    u_1[0] = bound1(tau)
    u_1[-1] = bound2(tau)

    for i in range(1, size_h-1):
      u_1[i] = u_0[i] + tau * (eps * (u_0[i-1] - 2 * u_0[i] + u_0[i+1]) / (h * h) - f(u_0[i]) * (u_0[i] - u_0[i-1]) / h)

    n_plot = (t_end / tau) / 10
    for j in range(2, int(t_end/tau) + 1):
        u_0 = u_1.copy()

        for i in range(1, size_h-1):
          if f(u_0[i]) > 0:
            u_1[i] = u_0[i] + tau * (eps * (u_0[i-1] - 2 * u_0[i] + u_0[i+1]) / (h * h) - f(u_0[i]) * (u_0[i] - u_0[i-1]) / h)
          if f(u_0[i]) < 0:
            u_1[i] = u_0[i] + tau * (eps * (u_0[i-1] - 2 * u_0[i] + u_0[i+1]) / (h * h) - f(u_0[i]) * (u_0[i+1] - u_0[i]) / h)
          
        u_1[0] = bound1(j*tau)
        u_1[-1] = bound2(j*tau)

        # n_plot = 40
        if j % n_plot == 0:
          plt.plot(u_1, alpha=0.5, label=f"t = {j}")
          plt.ylim(-2, 4.5)
          # plt.show()
    plt.legend()
    return u_1
  
def impl_2(f, init, bound_1, bound_2, a, b, h, tau, t_end, eps):
  size_h = int(abs(b - a) / h) + 1
    
  u_0 = np.zeros(size_h)
  for i in range(0, size_h):
    u_0[i] = init(a + i * h)
  
  plt.figure(figsize=(10, 7))
  plt.plot(u_0)
  # plt.show()
  
  alpha = np.zeros(size_h)
  beta = np.zeros(size_h)
  
  A = np.eye(size_h)
  b = np.zeros(size_h)

  n_plot = (t_end / tau) / 10
  for j in range(1, int(t_end / tau) + 1):
    # считаем на границах
    beta[1] = bound_1(i * tau)
    b[0] = bound_1(i * tau)

    for i in range(2, size_h):
        A_n = -eps / (h * h) - f(u_0[i - 1]) / h 
        B_n = 1 / tau + f(u_0[i - 1]) / h + 2 * eps / (h * h)
        C_n = -eps / (h * h)
        alpha[i] = -C_n / (A_n * alpha[i - 1] + B_n)
        beta[i] = ((u_0[i - 1] / tau) - A_n * beta[i - 1]) / (A_n * alpha[i - 1] + B_n)
    
    for i in range(1, size_h-2):
        A[i, i + 1] = -alpha[i + 1]
        b[i] = beta[i + 1]
    
    b[-2] = alpha[-1] * b[-1] + beta[-1]
    b[-1] = bound_2(i * tau)
    
    u_0 = np.linalg.solve(A, b)
    if j % n_plot == 0:
          plt.plot(u_0, alpha=0.5, label=f"t = {j}")
          plt.ylim(-2, 3)
          # plt.show()
  plt.legend()
  return u_0
