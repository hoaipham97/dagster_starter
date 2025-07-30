from dagster import Definitions, load_assets_from_modules

# Import the sub-packages where assets and definitions are now defined
from .assets import hackernews, hoaipham_test

# The `load_assets_from_modules` function discovers the Definitions objects
# from both the hackernews and hoaipham_test packages and merges them.
all_definitions = load_assets_from_modules(
    [hackernews, hoaipham_test],
)

# The main defs object remains incredibly clean and scalable.
defs = Definitions(
    assets=all_definitions,
    # You can add other global objects here, like sensors or resources
)