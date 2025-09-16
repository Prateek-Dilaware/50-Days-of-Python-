from Mod.Vat_Cal import price_and_vat


def testing():
    assert price_and_vat(220, 15) == 253
    assert price_and_vat(500,10) == 550