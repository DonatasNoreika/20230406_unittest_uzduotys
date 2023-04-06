
def kmi(svoris, ugis):
    if svoris < 30:
        raise ValueError("Svoris per mažas")
    if svoris > 200 and ugis < 1.5:
        raise ValueError("Svoris per didelis")
    if ugis < 0.5 and svoris > 20:
        raise ValueError("Svoris per didelis")
    if ugis > 3:
        raise ValueError("Ūgis per didelis")
    return svoris / ugis ** 2