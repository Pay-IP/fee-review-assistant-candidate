from pydantic import BaseModel, ConfigDict, Field


class FeeRecord(BaseModel):
    """A fictional card-network fee for one reporting period."""

    model_config = ConfigDict(frozen=True)

    id: int
    scheme: str = Field(min_length=1)
    country: str = Field(min_length=1)
    fee_name: str = Field(min_length=1)
    amount: int = Field(ge=0)
    currency: str = Field(pattern=r"^[A-Z]{3}$")
    previous_amount: int | None = Field(default=None, ge=0)


class FeeExplanation(BaseModel):
    """Deterministic review explanation returned by the API."""

    fee_id: int
    threshold: int
    requires_review: bool
    percentage_change: float | None
    explanation: str

