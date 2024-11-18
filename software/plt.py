import numpy as np
import matplotlib.pyplot as plt

def convergence_rates(n_iterations=20):
    """Simulate convergence rates for different eigenvalue algorithms"""
    iterations = np.arange(1, n_iterations + 1)
    
    # Initial error (start from same point)
    initial_error = 1.0
    
    # QR Algorithm (without and with shifts)
    qr_no_shift = initial_error * np.power(0.8, iterations)  # Linear
    qr_with_shift = initial_error * np.power(0.5, iterations * 2)  # Quadratic
    
    # Divide and Conquer (showing both cases)
    dc_typical = initial_error * np.power(0.6, iterations * 1.5)  # Superlinear
    dc_optimal = initial_error * np.power(0.5, iterations * 2.5)  # Near-cubic
    
    # Laguerre (simple roots)
    laguerre = initial_error * np.power(0.5, iterations * 3)  # Cubic
    
    # Jacobi
    jacobi = initial_error * np.power(0.7, iterations * 2)  # Quadratic
    
    # Arnoldi/Lanczos (for well-separated eigenvalues)
    arnoldi = initial_error * np.power(0.75, iterations * 1.5)  # Superlinear
    
    return iterations, qr_no_shift, qr_with_shift, dc_typical, dc_optimal, laguerre, jacobi, arnoldi

def plot_convergence_rates():
    """Create detailed plot of convergence rates"""
    plt.figure(figsize=(12, 8))
    
    # Get convergence data
    iters, qr_no_shift, qr_with_shift, dc_typical, dc_optimal, laguerre, jacobi, arnoldi = convergence_rates()
    
    # Plot with distinct colors and styles
    plt.semilogy(iters, qr_with_shift, 'b-', label='QR - Quadratic', linewidth=2)
    plt.semilogy(iters, dc_optimal, 'g-', label='D&C  - Near-cubic', linewidth=2)
    plt.semilogy(iters, laguerre, 'r-', label='Laguerre - Cubic', linewidth=2)
    plt.semilogy(iters, jacobi, 'c-', label='Jacobi - Quadratic', linewidth=2)
    plt.semilogy(iters, arnoldi, 'm-', label='Arnoldi/Lanczos - Superlinear', linewidth=2)
    
    # Customize plot
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.xlabel('Iteration', fontsize=12, fontweight='bold')
    plt.ylabel('Error (log scale)', fontsize=12, fontweight='bold')
    plt.title('Convergence Rates of Eigenvalue Algorithms', fontsize=14, fontweight='bold', pad=20)
    
    # Customize legend
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., fontsize=10)
    
    # Add grid and set limits
    plt.grid(True, which='major', linestyle='-', alpha=0.7)
    plt.grid(True, which='minor', linestyle=':', alpha=0.4)
    plt.ylim(1e-16, 2)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return plt.gcf()

# Additional function to show convergence order comparison
def plot_convergence_order_comparison():
    """Create comparison plot of different convergence orders"""
    plt.figure(figsize=(10, 6))
    
    x = np.linspace(0, 1, 100)
    
    # Different orders of convergence
    linear = x
    quadratic = x**2
    superlinear = x**1.5
    cubic = x**3
    
    plt.plot(x, linear, 'b-', label='Linear', linewidth=2)
    plt.plot(x, quadratic, 'r-', label='Quadratic', linewidth=2)
    plt.plot(x, superlinear, 'g-', label='Superlinear', linewidth=2)
    plt.plot(x, cubic, 'm-', label='Cubic', linewidth=2)
    
    plt.grid(True)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Comparison of Convergence Orders', fontsize=14)
    plt.legend()
    plt.tight_layout()
    
    return plt.gcf()

# Generate both plots
if __name__ == "__main__":
    # Plot convergence rates
    fig1 = plot_convergence_rates()
    #plt.figure(1)
    #plt.show()
    
    # Plot convergence order comparison
    fig2 = plot_convergence_order_comparison()
    plt.figure(2)
    plt.show()
