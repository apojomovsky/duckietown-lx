from typing import Tuple

import numpy as np


def delta_phi(ticks: int, prev_ticks: int, resolution: int) -> Tuple[float, float]:
    """
    Args:
        ticks: Current tick count from the encoders.
        prev_ticks: Previous tick count from the encoders.
        resolution: Number of ticks per full wheel rotation returned by the encoder.
    Return:
        rotation_wheel: Rotation of the wheel in radians.
        ticks: current number of ticks.
    """

    # TODO: these are random values, you have to implement your own solution in here
    ticks = prev_ticks + int(np.random.uniform(0, 10))
    dphi = np.random.random()
    # ---
    return dphi, ticks


def pose_estimation(
    R: float,
    baseline: float,
    x_prev: float,
    y_prev: float,
    theta_prev: float,
    delta_phi_left: float,
    delta_phi_right: float,
) -> Tuple[float, float, float]:

    """
    Calculate the current Duckiebot pose using the dead-reckoning model.

    Args:
        R:                  radius of wheel (both wheels are assumed to have the same size) - this is fixed in simulation,
                            and will be imported from your saved calibration for the real robot
        baseline:           distance from wheel to wheel; 2L of the theory
        x_prev:             previous x estimate - assume given
        y_prev:             previous y estimate - assume given
        theta_prev:         previous orientation estimate - assume given
        delta_phi_left:     left wheel rotation (rad)
        delta_phi_right:    right wheel rotation (rad)

    Return:
        x:                  estimated x coordinate
        y:                  estimated y coordinate
        theta:              estimated heading
    """

    # These are random values, replace with your own

    d_left  = delta_phi_left * R
    d_right = delta_phi_right * R
    delta_distance = (d_right + d_left) / 2.
    delta_theta = (d_right - d_left) / baseline

    delta_x = delta_distance * np.cos(delta_theta)
    delta_y = delta_distance * np.sin(delta_theta)

    o_to_r = np.array([
        [np.cos(theta_prev), -np.sin(theta_prev), x_prev],
        [np.sin(theta_prev), np.cos(theta_prev), y_prev],
        [0, 0, 1]
    ])

    r_to_rfinal = np.array([
        [np.cos(delta_theta), -np.sin(delta_theta), delta_x],
        [np.sin(delta_theta), np.cos(delta_theta), delta_y],
        [0, 0, 1],
    ])

    o_to_rfinal = np.dot(o_to_r, r_to_rfinal)

    x_curr = o_to_rfinal[0][2]
    y_curr = o_to_rfinal[1][2]
    theta_curr = np.arctan2(o_to_rfinal[1][0], o_to_rfinal[0][0])

    # ---
    return x_curr, y_curr, theta_curr
