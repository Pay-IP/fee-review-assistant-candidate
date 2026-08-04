from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status

from .. import services
from ..models import FeeExplanation, FeeRecord
from ..sample_data import FEE_RECORDS


router = APIRouter(prefix="/fees", tags=["fees"])
PositiveThreshold = Annotated[int, Query(gt=0, description="Review threshold in fee currency units")]


@router.get("", response_model=list[FeeRecord])
def list_fees(
    scheme: str | None = None,
    country: str | None = None,
) -> list[FeeRecord]:
    """List fees, optionally filtered by scheme and country."""
    return services.filter_fee_records(FEE_RECORDS, scheme=scheme, country=country)


@router.get("/anomalies", response_model=list[FeeRecord])
def list_anomalies(threshold: PositiveThreshold) -> list[FeeRecord]:
    """List records that exceed a configurable threshold."""
    # TODO(candidate): connect this route to the service-layer anomaly rule.
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Anomaly detection has not been implemented",
    )


@router.get("/{fee_id}", response_model=FeeRecord)
def get_fee(fee_id: int) -> FeeRecord:
    """Return one fee or a clear 404 response."""
    record = services.find_fee_record(FEE_RECORDS, fee_id)
    if record is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Fee record {fee_id} was not found",
        )
    return record


@router.get("/{fee_id}/explanation", response_model=FeeExplanation)
def get_fee_explanation(fee_id: int, threshold: PositiveThreshold) -> FeeExplanation:
    """Return a deterministic explanation of a fee's review status."""
    # TODO(candidate): return 404 for a missing fee and call the explanation service.
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Fee explanations have not been implemented",
    )

