"""Pre-analytical checks of specimens."""

HEMOLYSIS_SENSITIVE = ["POTASSIUM", "LDH", "AST"]


def is_hemolyzed(hemolysis_index):
    """Hemolysis index (free hemoglobin) in g/L."""
    return hemolysis_index > 1.0


def validate_specimen(test_name, hemolysis_index):
    if test_name in HEMOLYSIS_SENSITIVE and is_hemolyzed(hemolysis_index):
        return "REJECTED: hemolyzed specimen (HI=%.1f g/L)" % hemolysis_index
    return "OK"
