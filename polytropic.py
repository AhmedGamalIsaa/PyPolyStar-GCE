import numpy as np
from scipy.integrate import solve_ivp

class PolytropicStar:
    def __init__(self, n, rho_c=1e6, K=1.0036e13, xi_max=30.0, rtol=1e-10, atol=1e-10):
        self.n = n
        self.rho_c = rho_c
        self.K = K
        self.xi_max = xi_max
        self.rtol = rtol
        self.atol = atol

        # Physical Constants (cgs)
        self.G = 6.67430e-8
        self.M_sun_cgs = 1.9884e33
        self.R_sun_cgs = 6.957e10

        # Run the solver and physical conversions immediately
        self._solve_lane_emden()
        self._calculate_physical_properties()

    def _solve_lane_emden(self):
        # The Lane-Emden system of ODEs: y = [theta, dtheta_dxi]
        def derivatives(xi, y):
            theta, dtheta_dxi = y

            # Avoid complex numbers if theta dips slightly below 0 numerically
            if theta < 0:
                theta = 0.0

            d2theta_dxi2 = -(theta**self.n) - (2.0 / xi) * dtheta_dxi
            return [dtheta_dxi, d2theta_dxi2]

        # Stop integration when theta hits 0 (surface of the star)
        def surface_event(xi, y):
            return y[0]
        surface_event.terminal = True
        surface_event.direction = -1

        # Initial conditions close to center (Taylor expansion to avoid 1/0 singularity)
        xi_0 = 1e-5
        theta_0 = 1.0 - (xi_0**2) / 6.0 + (self.n * xi_0**4) / 120.0
        dtheta_0 = -xi_0 / 3.0 + (self.n * xi_0**3) / 30.0

        # Solve the Initial Value Problem
        sol = solve_ivp(
            derivatives,
            [xi_0, self.xi_max],
            [theta_0, dtheta_0],
            method='RK45',
            events=surface_event,
            rtol=self.rtol,
            atol=self.atol
        )

        # Store the boundary values
        self.xi_1 = sol.t[-1]
        self.dtheta_dxi_1 = sol.y[1, -1]

    def _calculate_physical_properties(self):
        # Calculate length scale alpha
        exponent = (1.0 / self.n) - 1.0 if self.n != 0 else -1.0
        self.alpha = np.sqrt(((self.n + 1) * self.K) / (4 * np.pi * self.G) * (self.rho_c**exponent))

        # Total Radius
        self.R_cgs = self.alpha * self.xi_1

        # Total Mass
        self.M_cgs = 4 * np.pi * (self.alpha**3) * self.rho_c * (-(self.xi_1**2) * self.dtheta_dxi_1)

        # Final output in Solar Units (as requested by your Figure 1 code)
        self.M_sun = self.M_cgs / self.M_sun_cgs
        self.R_sun = self.R_cgs / self.R_sun_cgs
