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
    fails to load, the others are unaffected because the `define_workspace`
    function handles errors from this generator gracefully.
    """
    pipelines_path = Path(__file__).parent / PIPELINES_DIR
    for filename in os.listdir(pipelines_path):
        filepath = pipelines_path / filename
        # Our convention is that every directory is a pipeline with a definitions.py
        if filepath.is_dir() and (filepath / "definitions.py").exists():
            pipeline_name = filename
            print(f"Discovered pipeline: {pipeline_name}")

            # By removing the try/except, any exception raised here will be
            # caught by the `define_workspace` function. It will then mark
            # this specific code location as failed in the UI, without
            # crashing the entire workspace.
            yield DagsterCodeLocation(
                location_name=f"{pipeline_name}_location",
                module_name=f"quickstart_etl.assets.{pipeline_name}.definitions",
            )


# The `define_workspace` function is robust. It will iterate through the
# generator and gracefully handle any exceptions from individual locations.
workspace = define_workspace(
    locations_from_generator=get_pipeline_code_locations()
)