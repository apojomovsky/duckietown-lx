from typing import Tuple

import numpy as np


def PIDController(
    v_0: float, y_ref: float, y_hat: float, prev_e_y: float, prev_int_y: float, delta_t: float
) -> Tuple[float, float, float, float]:
    """
    PID performing lateral control.

    Args:
        v_0:        linear Duckiebot speed (constant).
        y_ref:      target y coordinate.
        y_hat:      the current estimated y.
        prev_e_y:   tracking error at previous iteration.
        prev_int_y: previous integral error term.
        delta_t:    time interval since last call.

    Returns:
        v_0:        linear velocity of the Duckiebot
        omega:      angular velocity of the Duckiebot
        e:          current tracking error (automatically becomes prev_e_y at next iteration).
        e_int:      current integral error (automatically becomes prev_int_y at next iteration).
    """
    
    # Tracking error
    e = y_ref - y_hat

    # integral of the error
    e_int = prev_int_y + (e * delta_t)

    # anti-windup - preventing the integral error from growing too much
    e_int = max(min(e_int, 2), -2)

    # derivative of the error
    e_der = (e - prev_e_y) / delta_t

    # controller coefficients
    Kp = 4
    Ki = 0.01
    Kd = 15

    # PID controller for omega
    omega = (Kp * e) + (Ki * e_int) + (Kd * e_der)

    # ---
    
    return v_0, omega, e, e_int
