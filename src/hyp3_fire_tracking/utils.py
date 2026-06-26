import os
import subprocess
from pathlib import Path


def get_proc_home() -> Path:
    """Get the PROC_HOME environment variable, which is the location of the SRG modules.

    Returns:
        Path to the PROC_HOME directory
    """
    proc_home = os.environ.get('PROC_HOME', None)
    if proc_home is None:
        raise ValueError('PROC_HOME environment variable is not set. Location of Stanford modules is unknown.')
    return Path(proc_home)


def call_fire_module(local_name, args: list = [], work_dir: Path | None = None) -> None:
    """Call a Stanford Processor modules (via subprocess) with the given arguments.

    Args:
        local_name: Name of the module to call (e.g. 'sentinel/sentinel_scene_cpu.py')
        work_dir: Directory to run the module in
        args: List of arguments to pass to the module
    """
    if work_dir is None:
        work_dir = Path.cwd()

    proc_home = get_proc_home()
    script = proc_home / local_name
    args = [str(x) for x in args]
    print(f'Calling {local_name} {" ".join(args)} in directory {work_dir}')
    subprocess.run(['python',str(script), *args], cwd=work_dir, check=True)
