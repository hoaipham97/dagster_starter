import os
from pathlib import Path

from dagster import DagsterCodeLocation, define_workspace

# The directory containing your pipelines
PIPELINES_DIR = "quickstart_etl/assets"


def get_pipeline_code_locations():
    """
    Scans the pipelines directory and yields a Dagster CodeLocation for each
    pipeline package it finds.

    This provides both auto-discovery and error isolation. If one pipeline
    fails to load, it is silently skipped.
    """
    pipelines_path = Path(__file__).parent / PIPELINES_DIR
    for filename in os.listdir(pipelines_path):
        filepath = pipelines_path / filename
        # Our convention is that every directory is a pipeline with a definitions.py
        if filepath.is_dir() and (filepath / "definitions.py").exists():
            pipeline_name = filename
            print(f"Discovered pipeline: {pipeline_name}")

            # This try/except block will catch any loading errors from a single
            # pipeline, print a warning to the console, and allow the other
            # pipelines to load successfully without showing an error in the UI.
            try:
                yield DagsterCodeLocation(
                    location_name=f"{pipeline_name}_location",
                    module_name=f"quickstart_etl.assets.{pipeline_name}.definitions",
                )
            except Exception as e:
                # This is the key to skipping errors. If a pipeline is broken,
                # we print a warning to the console logs but continue loading the others.
                print(
                    f"WARNING: Could not load pipeline '{pipeline_name}'. "
                    f"It will be skipped. Error: {e}"
                )


# The `define_workspace` function will now only receive successfully loaded locations.
workspace = define_workspace(
    locations_from_generator=get_pipeline_code_locations()
)