import argparse
from isaaclab.app import AppLauncher

# create argparser
parser = argparse.ArgumentParser(description="Tutorial on creating an empty stage.")
AppLauncher.add_app_launcher_args(parser)
args_cli = parser.parse_args()

# --- Low graphics config ---
app_launcher = AppLauncher(
    args_cli,
    enable_window=True,         # show a window
    width=800,                  # low resolution
    height=600,
    renderer="RayTracedLighting",
    rtx_mode=0,                 # disable RTX ray tracing
    skip_dlss=True,             # disable DLSS
    anti_aliasing=0,            # disable AA
    use_vulkan=True             # Vulkan backend
)

# Access the simulation app
simulation_app = app_launcher.app

# Now we can safely import Isaac Lab modules
from isaaclab.sim import SimulationCfg, SimulationContext


def main():
    sim_cfg = SimulationCfg(dt=0.01)
    sim = SimulationContext(sim_cfg)
    sim.set_camera_view((2.5, 2.5, 2.5), (0.0, 0.0, 0.0))

    sim.reset()
    print("[INFO]: Setup complete...")

    while simulation_app.is_running():
        sim.step()


if __name__ == "__main__":
    main()
    simulation_app.close()
