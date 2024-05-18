baseurl_fred = 'https://api.stlouisfed.org/fred'

fred_hierarchy = {
    "category": {
        "children": {
            "required": ["category_id"],
            "optional": ["realtime_start", "realtime_end"]
        },
        "related": {
            "required": ["category_id"],
            "optional": ["realtime_start", "realtime_end"]
        },
        "series": {
            "required": ["category_id"],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order", "filter_variable", "filter_value", "tag_names", "exclude_tag_names"]
        },
        "tags": {
            "required": ["category_id"],
            "optional": ["realtime_start", "realtime_end"]
        }
    },
    "releases": {
        "release": {
            "required": ["release_id"],
            "optional": []
        },
        "dates": {
            "required": [],
            "optional": ["release_id", "realtime_start", "realtime_end"]
        },
        "series": {
            "required": ["release_id"],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order", "filter_variable", "filter_value", "tag_names", "exclude_tag_names"]
        },
        "sources": {
            "required": ["release_id"],
            "optional": []
        },
        "tags": {
            "required": ["release_id"],
            "optional": ["realtime_start", "realtime_end"]
        }
    },
    "release": {
        "dates": {
            "required": ["release_id"],
            "optional": ["realtime_start", "realtime_end"]
        },
        "series": {
            "required": ["release_id"],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order", "filter_variable", "filter_value", "tag_names", "exclude_tag_names"]
        },
        "sources": {
            "required": ["release_id"],
            "optional": []
        },
        "tags": {
            "required": ["release_id"],
            "optional": ["realtime_start", "realtime_end"]
        }
    },
    "series": {
        "categories": {
            "required": ["series_id"],
            "optional": []
        },
        "observations": {
            "required": ["series_id"],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "sort_order", "observation_start", "observation_end", "units", "frequency", "aggregation_method", "output_type", "vintage_dates"]
        },
        "release": {
            "required": ["series_id"],
            "optional": []
        },
        "search": {
            "required": ["search_text"],
            "optional": ["search_type", "realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order", "filter_variable", "filter_value", "tag_names", "exclude_tag_names"]
        },
        "tags": {
            "required": ["series_id"],
            "optional": ["realtime_start", "realtime_end"]
        },
        "updates": {
            "required": [],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "filter_value"]
        },
        "vintagedates": {
            "required": ["series_id"],
            "optional": ["realtime_start", "realtime_end"]
        }
    },
    "source": {
        "releases": {
            "required": ["source_id"],
            "optional": []
        }
    },
    "sources": {
        "releases": {
            "required": [],
            "optional": []
        }
    },
    "tags": {
        "series": {
            "required": ["tag_names"],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order", "exclude_tag_names"]
        },
        "related": {
            "required": ["tag_names"],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order"]
        }
    },
    "related_tags": {
        "series": {
            "required": ["tag_names"],
            "optional": ["exclude_tag_names"]
        }
    },
    "tags_series": {
        "series": {
            "required": ["tag_names"],
            "optional": ["realtime_start", "realtime_end", "limit", "offset", "order_by", "sort_order", "exclude_tag_names"]
        }
    }
}