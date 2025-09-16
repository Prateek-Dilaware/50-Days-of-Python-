def price_and_vat(price : float,vat : float) -> float:
    total_price = price + (price * vat/100)
    return total_price

    
    