import numpy as np
from numpy import cos, sin, arctan2, sqrt, meshgrid, linspace
import matplotlib.pyplot as plt
import numpy.typing as npt
from typing import Callable, NamedTuple

floats = npt.NDArray[np.float64]


def B_constant(
    R0: float, r0: float
) -> Callable[[float, float, float], tuple[float, float, float]]:
    """Constant toroidal magnetic field within radius r0

    R0: torus radius
    r0: poloidal radius
    returns: x, y, z -> B_x, B_y, B_z
    """

    def B(x: float, y: float, z: float) -> tuple[float, float, float]:
        r, theta, zeta = cartesian_to_toroidal(R0, x, y, z)
        if r < r0:
            B_r, B_theta, B_zeta = 0, 0, 1 / R0
        else:
            B_r, B_theta, B_zeta = 0, 0, 0

        x, y, z, f_x, f_y, f_z = toroidal_field_vector_to_cartesian(
            R0, r, theta, zeta, B_r, B_theta, B_zeta
        )

        return f_x, f_y, f_z

    return B


def B_physical(
    R0: float, r0: float
) -> Callable[[float, float, float], tuple[float, float, float]]:
    """Physical (i.e., satisfies Ampere's law) toroidal magnetic field within radius r0

    R0: torus radius
    r0: poloidal radius
    returns: x, y, z -> B_x, B_y, B_z
    """

    def B(x: float, y: float, z: float) -> tuple[float, float, float]:
        r, theta, zeta = cartesian_to_toroidal(R0, x, y, z)
        R = R0 + r * cos(theta)

        if r < r0:
            B_r, B_theta, B_zeta = 0, 0, R0 / R
        else:
            B_r, B_theta, B_zeta = 0, 0, 0

        x, y, z, f_x, f_y, f_z = toroidal_field_vector_to_cartesian(
            R0, r, theta, zeta, B_r, B_theta, B_zeta
        )

        return f_x, f_y, f_z

    return B


def B_twisting(
    R0: float, r0: float
) -> Callable[[float, float, float], tuple[float, float, float]]:
    """Twisting toroidal magnetic field

    R0: torus radius
    r0: poloidal radius
    returns: x, y, z -> B_x, B_y, B_z
    """

    def B(x: float, y: float, z: float) -> tuple[float, float, float]:
        r, theta, zeta = cartesian_to_toroidal(R0, x, y, z)
        R = R0 + r * cos(theta)

        if r < r0:
            B_r, B_theta, B_zeta = 0, r / r0, R0 / R
        else:
            B_r, B_theta, B_zeta = 0, 0, 0

        x, y, z, f_x, f_y, f_z = toroidal_field_vector_to_cartesian(
            R0, r, theta, zeta, B_r, B_theta, B_zeta
        )

        return f_x, f_y, f_z

    return B


def z0_slice(
    f: Callable[[float, float, float], tuple[float, float, float]],
) -> Callable[[float, float], tuple[float, float]]:
    """Return the 2D vector field at z = 0 of a 3D vector field

    f: 3D vector field
    returns: x, y -> f_x, f_y
    """

    def f_xy(x: float, y: float) -> tuple[float, float]:
        f_x, f_y, _ = f(x, y, 0)
        return f_x, f_y

    return f_xy


def toroidal_field_vector_to_cartesian(
    R_0: float,
    r: float,
    theta: float,
    zeta: float,
    f_r: float,
    f_theta: float,
    f_zeta: float,
) -> tuple[float, float, float, float, float, float]:
    """Convert a toroidal field vector to a Cartesian field vector

    (r, theta, zeta): toroidal coordinate
    (f_r, f_theta, f_zeta): vector at that coordinate

    returns (x, y, z, f_x, f_y, f_z)
    """
    f_x = (
        cos(theta) * cos(zeta) * f_r
        - sin(theta) * cos(zeta) * f_theta
        - sin(zeta) * f_zeta
    )
    f_y = (
        cos(theta) * sin(zeta) * f_r
        - sin(theta) * sin(zeta) * f_theta
        + cos(zeta) * f_zeta
    )
    f_z = sin(theta) * f_r + cos(theta) * f_theta

    x, y, z = toroidal_to_cartesian(R_0, r, theta, zeta)

    return x, y, z, f_x, f_y, f_z


def toroidal_to_cartesian(
    R_0: float, r: float, theta: float, zeta: float
) -> tuple[float, float, float]:
    x = (R_0 + r * cos(theta)) * cos(zeta)
    y = (R_0 + r * cos(theta)) * sin(zeta)
    z = r * sin(theta)
    return x, y, z


def cartesian_to_toroidal(
    R_0: float, x: float, y: float, z: float
) -> tuple[float, float, float]:
    r = sqrt((sqrt(x**2 + y**2) - R_0) ** 2 + z**2)
    # 2nd arg is signed distance to central circle (negative if inside)
    theta = arctan2(z, sqrt(x**2 + y**2) - R_0)
    zeta = arctan2(y, x)
    return r, theta, zeta


def plot_2d_cartesian_vector_field(
    f: Callable[[float, float], tuple[float, float]],
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    title: str,
):
    _, ax = plt.subplots(figsize=(12, 8))  # type: ignore

    x_range = linspace(x_min, x_max, 20)
    y_range = linspace(y_min, y_max, 20)
    X, Y = meshgrid(x_range, y_range)

    f_x_grid = np.zeros_like(X)
    f_y_grid = np.zeros_like(Y)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            f_x_grid[i, j], f_y_grid[i, j] = f(X[i, j], Y[i, j])

    ax.quiver(X, Y, f_x_grid, f_y_grid, alpha=0.7)  # type: ignore
    ax.set_xlabel("X")  # type: ignore
    ax.set_ylabel("Y")  # type: ignore
    # ax.set_title(title)  # type: ignore
    ax.set_aspect("equal")  # type: ignore
    plt.tight_layout()  # type: ignore
    # plt.show()  # type: ignore
    filename = f"./images/midterm-2d-{title.lower().replace(' ', '-')}.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")  # type: ignore


def plot_3d_cartesian_vector_field(
    f: Callable[[float, float, float], tuple[float, float, float]],
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    z_min: float,
    z_max: float,
    title: str,
):
    fig = plt.figure(figsize=(12, 8))  # type: ignore
    ax = fig.add_subplot(111, projection="3d")  # type: ignore

    x_range = linspace(x_min, x_max, 20)
    y_range = linspace(y_min, y_max, 20)
    z_range = linspace(z_min, z_max, 20)
    X, Y, Z = meshgrid(x_range, y_range, z_range)
    f_x_grid = np.zeros_like(X)
    f_y_grid = np.zeros_like(Y)
    f_z_grid = np.zeros_like(Z)

    for i in range(len(x_range)):
        for j in range(len(y_range)):
            for k in range(len(z_range)):
                x, y, z = X[i, j, k], Y[i, j, k], Z[i, j, k]
                f_x, f_y, f_z = f(x, y, z)
                f_x_grid[i, j, k] = f_x
                f_y_grid[i, j, k] = f_y
                f_z_grid[i, j, k] = f_z

    ax.quiver(X, Y, Z, f_x_grid, f_y_grid, f_z_grid, length=0.1, normalize=True, alpha=0.7)  # type: ignore
    ax.set_xlabel("X")  # type: ignore
    ax.set_ylabel("Y")  # type: ignore
    ax.set_zlabel("Z")  # type: ignore
    # ax.set_title(title)  # type: ignore
    plt.tight_layout()  # type: ignore
    # plt.show()  # type: ignore
    filename = f"./images/midterm-3d-{title.lower().replace(' ', '-')}.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")  # type: ignore


class Params(NamedTuple):
    # (x, y, z) -> [Bx, By, Bz]
    magnetic_field: Callable[[float, float, float], tuple[float, float, float]]
    # (vx, vy, vz)
    initial_velocity: floats
    # (x, y, z)
    initial_position: floats
    total_time: float


def rk2(r0: floats, v0: floats, dt: float, params: Params) -> tuple[floats, floats]:
    """
    For the IVP: u' = f(t, u), u(a) = u0,
    u_{i+1} = u_i + dt * f(t_i+0.5h, u_i+0.5h*f(t_i, u_i))
    In this case, v is u. v' = v_y hat{x} - v_x hat{y}

    Inputs:
        r0: [x, y, z] dimensionless
        v0: [vx, vy, vz] dimensionless
        dt: timestep dimensionless
        params: Params
    Outputs:
        r: [x, y, z] dimensionless
        v: [vx, vy, vz] dimensionless
    """
    B = params.magnetic_field(r0[0], r0[1], r0[2])
    a_halfway = np.cross(v0, B)
    v_halfway = v0 + (0.5 * dt) * a_halfway

    a = np.cross(v_halfway, B)
    v = v0 + a * dt
    r = r0 + v * dt

    return r, v


def rk4(
    r0: floats,
    v0: floats,
    dt: float,
    params: Params,
) -> tuple[floats, floats]:
    """
    Inputs:
        r0: [x, y, z] dimensionless
        v0: [vx, vy, vz] dimensionless
        dt: timestep dimensionless
        params: Params
    Outputs:
        r: [x, y, z] dimensionless
        v: [vx, vy, vz] dimensionless
    """

    B = params.magnetic_field(r0[0], r0[1], r0[2])
    a = np.cross(v0, B)

    # see Christian, W. (2010) Chapter 3: Simulating particle motion
    k1v = a * dt
    k1x = v0 * dt

    k2v = np.cross(v0 + k1v / 2, B) * dt
    k2x = (v0 + k1v / 2) * dt

    k3v = np.cross(v0 + k2v / 2, B) * dt
    k3x = (v0 + k2v / 2) * dt

    k4v = np.cross(v0 + k3v, B) * dt
    k4x = (v0 + k3v) * dt

    v = v0 + (k1v + 2 * k2v + 2 * k3v + k4v) / 6.0
    r = r0 + (k1x + 2 * k2x + 2 * k3x + k4x) / 6.0

    return r, v


def dynamic_dt_update(
    r0: floats, v0: floats, dt0: float, params: Params
) -> tuple[floats, floats, float, float]:
    """
    Inputs:
        r0: [x, y, z] dimensionless
        v0: [vx, vy, vz] dimensionless
        dt: timestep dimensionless
        params: Params
    Outputs:
        r: [x, y, z] dimensionless
        v: [vx, vy, vz] dimensionless
        dt0: float. dt which was used
        dt_next: float. dt to use for next step
    """
    r_rk2, _ = rk2(r0, v0, dt0, params)
    r_rk4, v_rk4 = rk4(r0, v0, dt0, params)

    Ei = float(np.linalg.norm(r_rk2 - r_rk4))
    # seems to be plenty ...
    epsilon: float = 1e-5
    p: float = 2
    q: float = (epsilon / Ei) ** (1 / (p + 1))

    if q > 10:
        q = 10
    elif q < 0.1:
        q = 0.1

    dt_next: float = q * dt0

    # Note: I originaly tried to use Ei < epsilon, but the error would asymptopte at epsilon but never cross it. This prevents that from happening.
    if Ei < epsilon * 1.01:
        return r_rk4, v_rk4, dt0, dt_next
    else:
        return dynamic_dt_update(r_rk4, v_rk4, dt_next, params)


def run_simulation(params: Params):
    """
    Outputs:
        pos [position vectors at each timestep (dimensionless)]
        vel [velocity vectors at each timestep (dimensionless)]
        time [total time (dimensionless)]
        dt [timestep (dimensionless)]
    """
    t_current: float = 0.0
    dt_current: float = 0.01
    r_current: floats = params.initial_position
    v_current: floats = params.initial_velocity

    pos_list: list[floats] = []
    vel_list: list[floats] = []
    time_list: list[float] = []
    dt_list: list[float] = []

    time_list.append(t_current)
    pos_list.append(r_current)
    vel_list.append(v_current)
    dt_list.append(dt_current)

    while t_current < params.total_time:
        r_next, v_next, dt_used, dt_next = dynamic_dt_update(
            r_current,
            v_current,
            dt_current,
            params,
        )
        t_next = t_current + dt_used

        progress = int(t_current / params.total_time * 100)
        if (
            progress > 0
            and progress <= 100
            and t_current - dt_used < progress * params.total_time / 100
        ):
            print(f"{progress}% complete")

        # store new values
        time_list.append(t_next)
        pos_list.append(r_next)
        vel_list.append(v_next)
        dt_list.append(dt_used)

        # update for next step
        r_current = r_next
        v_current = v_next
        t_current = t_next
        dt_current = dt_next

    return pos_list, vel_list, time_list, dt_list


def plot_time_step(time_list: list[float], dt_list: list[float], title: str) -> None:
    _, ax = plt.subplots()  # type: ignore
    ax.plot(time_list, dt_list)  # type: ignore
    ax.set_xlabel("t")  # type: ignore
    ax.set_ylabel("dt")  # type: ignore
    ax.set_title("Time Step vs. Time (Dimensionless)")  # type: ignore
    time_range = max(time_list) - min(time_list)
    dt_range = max(dt_list) - min(dt_list)
    time_padding = 0.05 * time_range
    dt_padding = 0.05 * dt_range
    ax.set_xlim(min(time_list) - time_padding, max(time_list) + time_padding)
    ax.set_ylim(min(dt_list) - dt_padding, max(dt_list) + dt_padding)
    ax.grid(True)  # type: ignore
    filename = f"./images/midterm-{title.lower().replace(' ', '-')}.png"
    plt.savefig(filename)  # type: ignore


def plot_position_xy(pos_list: list[floats], title: str) -> None:
    """
    Parameters:
        pos_list [list of position arrays]: List of position vectors at each timestep
        output_file_name [string]: Path where to save the plot
    """
    fig, ax = plt.subplots()  # type: ignore
    pos_array = np.array(pos_list)
    ax.plot(pos_array[:, 0], pos_array[:, 1])  # type: ignore
    ax.set_xlabel("x position (Dimensionless)")  # type: ignore
    ax.set_ylabel("y position (Dimensionless)")  # type: ignore

    # Calculate ranges and padding
    x_range = pos_array[:, 0].max() - pos_array[:, 0].min()
    y_range = pos_array[:, 1].max() - pos_array[:, 1].min()
    padding = 0.05 * max(x_range, y_range)

    # Set equal aspect ratio and limits
    ax.set_aspect("equal")  # type: ignore
    x_center = (pos_array[:, 0].max() + pos_array[:, 0].min()) / 2
    y_center = (pos_array[:, 1].max() + pos_array[:, 1].min()) / 2
    max_range = max(x_range, y_range) / 2

    ax.set_xlim(x_center - max_range - padding, x_center + max_range + padding)
    ax.set_ylim(y_center - max_range - padding, y_center + max_range + padding)

    ax.grid(True)  # type: ignore
    filename = f"./images/midterm-{title.lower().replace(' ', '-')}.png"
    fig.savefig(filename, bbox_inches="tight")  # type: ignore
    plt.close(fig)


def plot_position_z(pos_list: list[floats], time_list: list[float], title: str) -> None:
    """Plot z position against time with slope reference line"""
    fig, ax = plt.subplots()  # type: ignore
    pos_array = np.array(pos_list)
    ax.plot(time_list, pos_array[:, 2])  # type: ignore
    ax.set_xlabel("Time (Dimensionless)")  # type: ignore
    ax.set_ylabel("Z Position (Dimensionless)")  # type: ignore

    reference_line = 0.00086 * np.array(time_list)
    ax.plot(time_list, reference_line, color="orange", label="Slope 0.00086")  # type: ignore

    time_range = max(time_list) - min(time_list)
    z_range = pos_array[:, 2].max() - pos_array[:, 2].min()
    time_padding = 0.05 * time_range
    z_padding = 0.05 * z_range

    ax.set_xlim(min(time_list) - time_padding, max(time_list) + time_padding)
    ax.set_ylim(pos_array[:, 2].min() - z_padding, pos_array[:, 2].max() + z_padding)
    ax.legend()  # type: ignore
    ax.grid(True)  # type: ignore

    filename = f"./images/midterm-{title.lower().replace(' ', '-')}.png"
    fig.savefig(filename, bbox_inches="tight")  # type: ignore
    plt.close(fig)


def plot_position_xyz(pos_list: list[floats], title: str) -> None:
    """Plot 3D particle trajectory"""
    fig = plt.figure(figsize=(12, 8))  # type: ignore
    ax = fig.add_subplot(111, projection="3d")  # type: ignore

    pos_array = np.array(pos_list)
    ax.plot(pos_array[:, 0], pos_array[:, 1], pos_array[:, 2])  # type: ignore
    ax.set_xlabel("X Position (Dimensionless)")  # type: ignore
    ax.set_ylabel("Y Position (Dimensionless)")  # type: ignore
    ax.set_zlabel("Z Position (Dimensionless)")  # type: ignore

    x_range = pos_array[:, 0].max() - pos_array[:, 0].min()
    y_range = pos_array[:, 1].max() - pos_array[:, 1].min()
    z_range = pos_array[:, 2].max() - pos_array[:, 2].min()
    padding = 0.05 * max(x_range, y_range, z_range)

    ax.set_xlim(pos_array[:, 0].min() - padding, pos_array[:, 0].max() + padding)
    ax.set_ylim(pos_array[:, 1].min() - padding, pos_array[:, 1].max() + padding)
    ax.set_zlim(pos_array[:, 2].min() - padding, pos_array[:, 2].max() + padding)  # type: ignore

    ax.grid(True)  # type: ignore
    plt.tight_layout()  # type: ignore
    filename = f"./images/midterm-{title.lower().replace(' ', '-')}.png"
    fig.savefig(filename, bbox_inches="tight", pad_inches=0.2)  # type: ignore
    plt.close(fig)


# ---------------------------------------------------
# plot representive mangetic fields
# ---------------------------------------------------
# R0 = 1
# r0 = 0.2
# x_min = -R0 - r0
# x_max = R0 + r0
# y_min = -R0 - r0
# y_max = R0 + r0
# z_min = -R0 - r0
# z_max = R0 + r0

# plot_2d_cartesian_vector_field(
#     z0_slice(B_constant(R0, r0)),
#     x_min,
#     x_max,
#     y_min,
#     y_max,
#     "Uniform Toroidal Magnetic Field",
# )

# plot_2d_cartesian_vector_field(
#     z0_slice(B_physical(R0, r0)),
#     x_min,
#     x_max,
#     y_min,
#     y_max,
#     "Physical Toroidal Magnetic Field",
# )

# plot_2d_cartesian_vector_field(
#     z0_slice(B_twisting(R0, r0)),
#     x_min,
#     x_max,
#     y_min,
#     y_max,
#     "Twisting Toroidal Magnetic Field",
# )

# plot_3d_cartesian_vector_field(
#     B_constant(R0, r0),
#     x_min,
#     x_max,
#     y_min,
#     y_max,
#     z_min,
#     z_max,
#     "Uniform Toroidal Magnetic Field",
# )

# plot_3d_cartesian_vector_field(
#     B_physical(R0, r0),
#     x_min,
#     x_max,
#     y_min,
#     y_max,
#     z_min,
#     z_max,
#     "Physical Toroidal Magnetic Field",
# )

# plot_3d_cartesian_vector_field(
#     B_twisting(R0, r0),
#     x_min,
#     x_max,
#     y_min,
#     y_max,
#     z_min,
#     z_max,
#     "Twisting Toroidal Magnetic Field",
# )


# ---------------------------------------------------
# Run simulation
# ---------------------------------------------------
physical_params = Params(
    magnetic_field=B_physical(870, 217),
    initial_velocity=np.array([1 / sqrt(3)] * 3),
    initial_position=np.array([979, 0, 0]),
    total_time=30000,
)

pos_list, vel_list, time_list, dt_list = run_simulation(physical_params)
# plot_position_xy(pos_list, "Physical Field Position XY")
plot_position_z(pos_list, time_list, "Physical Field Position Z")
plot_position_xyz(pos_list, "Physical Field Position XYZ")

# physical_params = Params(
#     magnetic_field=B_twisting(870, 217),
#     initial_velocity=np.array([1 / sqrt(3)] * 3),
#     initial_position=np.array([979, 0, 0]),
#     total_time=30000,
# )

# pos_list, vel_list, time_list, dt_list = run_simulation(physical_params)
# plot_position_xy(pos_list, "Twisting Field Position XY")
# plot_position_z(pos_list, time_list, "Twisting Field Position Z")
# plot_position_xyz(pos_list, "Twisting Field Position XYZ")
