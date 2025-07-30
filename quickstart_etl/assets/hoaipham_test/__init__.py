from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from . import assets

# Load all asset definitions from the `assets.py` file in this folder
hoaipham_test_assets = load_assets_from_modules([assets])

# Define a job that targets only the assets in the "hoaipham_test" group
hoaipham_test_job = define_asset_job(
    name="hoaipham_test_job", selection=AssetSelection.groups("hoaipham_test")
)

# Define a schedule for the job
hoaipham_test_schedule = ScheduleDefinition(
    job=hoaipham_test_job, cron_schedule="0 1 * * *", execution_timezone="UTC"
)

# Create a Definitions object that bundles all components of this pipeline.
# Dagster will discover and load this object.
defs = Definitions(
    assets=hoaipham_test_assets,
    jobs=[hoaipham_test_job],
    schedules=[hoaipham_test_schedule],
)