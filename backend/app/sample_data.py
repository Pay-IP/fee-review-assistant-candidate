import json
from pathlib import Path

from .models import FeeRecord


DATA_FILE = Path(__file__).resolve().parents[2] / "data" / "fee_records.json"


def load_fee_records(path: Path = DATA_FILE) -> list[FeeRecord]:
    """Load and validate the fictional JSON dataset."""
    try:
        with path.open(encoding="utf-8") as source:
            raw_records = json.load(source)
    except FileNotFoundError as exc:
        raise RuntimeError(f"Fee data file was not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Fee data file is not valid JSON: {path}") from exc

    if not isinstance(raw_records, list):
        raise RuntimeError(f"Fee data must be a JSON array: {path}")

    return [FeeRecord.model_validate(record) for record in raw_records]


FEE_RECORDS = load_fee_records()

