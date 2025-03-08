import numpy as np

def euler_method(f, t0, y0, t_end, n):
    t_values = np.linspace(t0, t_end, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0
    h = (t_end - t0) / n
    
    for i in range(n):
        y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return y_values[-1]

def runge_kutta_method(f, t0, y0, t_end, n):
    t_values = np.linspace(t0, t_end, n+1)
    y_values = np.zeros(n+1)
    y_values[0] = y0
    h = (t_end - t0) / n
    
    for i in range(n):
        k1 = h * f(t_values[i], y_values[i])
        k2 = h * f(t_values[i] + h/2, y_values[i] + k1/2)
        k3 = h * f(t_values[i] + h/2, y_values[i] + k2/2)
        k4 = h * f(t_values[i] + h, y_values[i] + k3)
        y_values[i+1] = y_values[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return y_values[-1]

def function(t, y):
    return t - y**2

if __name__ == "__main__":
    t0, y0, t_end, n = 0, 1, 2, 10
    
    result_euler = euler_method(function, t0, y0, t_end, n)
    result_rk = runge_kutta_method(function, t0, y0, t_end, n)
    
    print(result_euler)
    print(result_rk)
