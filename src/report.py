"""Plain-text report for the ordering physician."""

HEADER = "LAB REPORT"
FOOTER = "Results validated by the laboratory. Units: SI (mmol/L)."


def build_report(patient_id, lines):
    body = [HEADER, "Patient: " + patient_id]
    body += lines
    body.append(FOOTER)
    return "\n".join(body)
