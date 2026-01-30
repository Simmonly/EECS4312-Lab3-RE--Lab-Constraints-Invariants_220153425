from datetime import date as Date


# You can expand this later. For now it's a simple source of truth.
MAX_DAILY_DOSE_MG = {
    "amoxicillin": 3000,
    "ibuprofen": 2400,
    "acetaminophen": 4000,
}


class DispenseEvent:

    def __init__(self, patient_id, medication, dose_mg, quantity, dispense_date=None):

        # Basic identifier constraints (reasonable safety constraints)
        if patient_id is None or str(patient_id).strip() == "":
            raise ValueError("patient_id must be non-empty")

        if medication is None or str(medication).strip() == "":
            raise ValueError("medication must be non-empty")

        # Normalize medication key for dose lookups
        med_key = str(medication).strip().lower()

        # Constraint 1: dose must be positive
        try:
            dose_val = float(dose_mg)
        except (TypeError, ValueError):
            raise ValueError("dose_mg must be a number")

        if dose_val <= 0:
            raise ValueError("dose_mg must be positive")

        # Constraint 2: quantity must be a positive integer
        if not isinstance(quantity, int):
            raise ValueError("quantity must be an integer")
        if quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        # Constraint 3: medication has a maximum daily dose
        if med_key not in MAX_DAILY_DOSE_MG:
            raise ValueError(f"Unknown medication '{medication}' (no max daily dose defined)")

        max_daily = MAX_DAILY_DOSE_MG[med_key]

        total_dispensed_mg = dose_val * quantity
        if total_dispensed_mg > max_daily:
            raise ValueError(
                f"Total dispensed ({total_dispensed_mg} mg) exceeds max daily dose ({max_daily} mg) for {med_key}"
            )

        self.patient_id = str(patient_id).strip()
        self.medication = med_key
        self.dose_mg = dose_val
        self.quantity = quantity
        self.dispense_date = dispense_date if dispense_date is not None else Date.today()

    @staticmethod
    def invariant_holds(existing_events, new_event):
        """
        Invariant: A patient may not receive the same medication more than once per day.
        """
        for e in existing_events:
            if (
                e.patient_id == new_event.patient_id
                and e.medication == new_event.medication
                and e.dispense_date == new_event.dispense_date
            ):
                return False
        return True
