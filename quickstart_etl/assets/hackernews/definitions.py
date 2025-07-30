from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from . import assets

# Load all asset definitions from the `assets.py` file in this folder
hackernews_assets = load_assets_from_modules([assets])

# Define a job that targets only the assets in the "hackernews" group
hackernews_job = define_asset_job(
    name="hackernews_job", selection=AssetSelection.groups("hackernews")
)

# Define a schedule for the job
hackernews_schedule = ScheduleDefinition(
    job=hackernews_job, cron_schedule="0 0 * * *", execution_timezone="UTC"
)

# Create a Definitions object that bundles all components of this pipeline.
# Dagster will discover and load this object.
defs = Definitions(
    assets=hackernews_assets,
    jobs=[hackernews_job],
    schedules=[hackernews_schedule],
)