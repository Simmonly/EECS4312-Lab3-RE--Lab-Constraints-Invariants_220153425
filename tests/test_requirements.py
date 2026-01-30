import pytest
from datetime import date

from src.dispense import DispenseEvent


# R1 (Constraint): dose must be positive
def test_rejects_zero_or_negative_dose():
    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="ibuprofen", dose_mg=0, quantity=1, dispense_date=date(2026, 1, 30))

    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="ibuprofen", dose_mg=-5, quantity=1, dispense_date=date(2026, 1, 30))


# R2 (Constraint): quantity must be a positive integer
def test_rejects_invalid_quantity():
    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="ibuprofen", dose_mg=200, quantity=0, dispense_date=date(2026, 1, 30))

    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="ibuprofen", dose_mg=200, quantity=-2, dispense_date=date(2026, 1, 30))

    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="ibuprofen", dose_mg=200, quantity=1.5, dispense_date=date(2026, 1, 30))


# R3 (Constraint): total dispensed must not exceed max daily dose
def test_rejects_exceeding_max_daily_dose():

    with pytest.raises(ValueError):
        DispenseEvent(patient_id="P1", medication="ibuprofen", dose_mg=800, quantity=4, dispense_date=date(2026, 1, 30))


# R4 (Invariant): no duplicate same patient + same medication + same day
def test_prevents_duplicate_dispensing_same_day():
    d = date(2026, 1, 30)
    existing = [DispenseEvent("P1", "ibuprofen", 200, 1, dispense_date=d)]
    new_event = DispenseEvent("P1", "ibuprofen", 200, 1, dispense_date=d)

    assert DispenseEvent.invariant_holds(existing, new_event) is False


def test_allows_same_medication_different_day():
    d1 = date(2026, 1, 30)
    d2 = date(2026, 1, 31)
    existing = [DispenseEvent("P1", "ibuprofen", 200, 1, dispense_date=d1)]
    new_event = DispenseEvent("P1", "ibuprofen", 200, 1, dispense_date=d2)

    assert DispenseEvent.invariant_holds(existing, new_event) is True
