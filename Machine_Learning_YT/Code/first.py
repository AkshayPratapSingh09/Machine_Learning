import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    #No. of observations
    n = np.size(x)

    #Mean of x anf y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    #Calculating Cross-Deviation and deviation about X
    ss_xy = np.sum(y*x) - n*(m_y)*(m_x)
    ss_xx = np.sum(x*x) - n*(m_x)*(m_x)

    #Calculating Regression Coefficients
    b_1 = ss_xy / ss_xx
    b_0 = m_y - b_1*m_x

    return (b_0, b_1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
  
    # predicted response vector
    y_pred = b[0] + b[1]*x
  
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
  
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
  
    # function to show plot
    plt.show()

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
b = estimate_coef(x,y)
print(plot_regression_line(x,y,b))
