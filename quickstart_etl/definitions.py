import importlib
import pkgutil
from pathlib import Path

from dagster import Definitions, load_assets_from_modules

# Import the top-level 'assets' package to know where to start scanning
from . import assets

def get_pipeline_packages(package):
    """
    Dynamically discovers and imports all sub-packages within a given package.
    This allows for automatic loading of new data pipelines.
    """
    # The path to the top-level package (e.g., .../quickstart_etl/assets)
    package_path = Path(package.__file__).parent
    package_name = package.__name__

    discovered_packages = []
    # Scan the directory for modules/packages
    for _, module_name, is_pkg in pkgutil.iter_modules([str(package_path)]):
        # We only care about packages (directories with an __init__.py)
        # as this is our convention for a self-contained pipeline.
        if is_pkg:
            try:
                # Dynamically import the module (e.g., 'quickstart_etl.assets.hackernews')
                module = importlib.import_module(f".{module_name}", package=package_name)
                discovered_packages.append(module)
            except ImportError as e:
                # Optional: Add logging for debugging if a module fails to import
                print(f"Warning: Could not import pipeline package '{module_name}'. Error: {e}")

    return discovered_packages

# Automatically discover all pipeline packages within the 'assets' directory.
# This list will now contain the imported `hackernews` and `hoaipham_test` modules.
all_pipeline_packages = get_pipeline_packages(assets)

# The `load_assets_from_modules` function discovers the Definitions objects
# from all the dynamically loaded packages and merges them into one.
all_definitions = load_assets_from_modules(all_pipeline_packages)

# The main defs object is now fully automated.
# No changes are needed here when you add a new pipeline.
defs = Definitions(
    assets=all_definitions,
    # You can add other global objects here, like sensors or resources
)
