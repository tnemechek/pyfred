# pyfred FRED API Client

## Installation

1. Install the package:

    ```bash
    pip install pyfred
    ```

2. Create a `.env` file in your program root directory with your API key:

    ```text
    FRED_API_KEY=your_api_key_here
    ```

## Usage

```python
from pyfred import FredAPIClient

client = FredAPIClient(
    # api_key: str (Optional) 
    # if not provided, will look for the FRED_API_KEY environment variable
    )

# Get category children in a dataframe format
category_children = client.category.children.get_dataframe(category_id=0)
print(category_children)

# Get series observations in json -> dict format
series_observations = client.series.observations.get_data(series_id='GNPCA')
print(series_observations)

# access the ".frame" attribute to get the data in a pandas dataframe
print(series_observations.frame)

# access the raw response
print(client.series.observations.get(series_id='GNPCA'))

# Get the release dates for a series
release_dates = client.series.release_dates.get_dataframe(series_id='GNPCA')
print(release_dates)

# Get the series search results in a dataframe format
series_search = client.series.search.get_dataframe(search_text='GDP')
print(series_search)
```
