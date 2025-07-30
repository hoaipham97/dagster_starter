from pathlib import Path

from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    graph_asset,
    link_code_references_to_git,
    load_assets_from_package_module,
    op,
    with_source_code_references,
)
from dagster._core.definitions.metadata.source_code import AnchorBasedFilePathMapping

from . import assets

daily_refresh_schedule = ScheduleDefinition(
    job=define_asset_job(name="all_assets_job"), cron_schedule="0 0 * * *"
)


@op
def foo_op():
    return 5


@graph_asset
def my_asset():
    return foo_op()


my_assets = with_source_code_references(
    [
        my_asset,
        *load_assets_from_package_module(assets),
    ]
)

my_assets = link_code_references_to_git(
    assets_defs=my_assets,
    git_url="https://github.com/dagster-io/dagster/",
    git_branch="master",
    file_path_mapping=AnchorBasedFilePathMapping(
        local_file_anchor=Path(__file__).parent,
        file_anchor_path_in_repository="examples/quickstart_etl/quickstart_etl/",
    ),
)

defs = Definitions(
    assets=my_assets,
    schedules=[daily_refresh_schedule],
)

from dagster import define_asset_job, ScheduleDefinition, Definitions
from quickstart_etl.assets.hoai_test import test1, test2

# Aggregate your assets including new ones
all_assets = [
    test1,
    test2,
]

# Define a new job that runs your two assets (test1 and test2)
hoaipham_test_job = define_asset_job(
    name="hoaipham_test_job",
    selection=["test1", "test2"],  # Names must match your asset function names
)

# Define the schedule for this job - e.g., run every day at 3:30 AM Asia/Bangkok time
hoaipham_test_schedule = ScheduleDefinition(
    job=hoaipham_test_job,
    cron_schedule="30 3 * * *",
    execution_timezone="Asia/Bangkok",
)

# Add to your Definitions
defs = Definitions(
    assets=all_assets,
    schedules=[hoaipham_test_schedule],
)
