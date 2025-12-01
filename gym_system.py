def calculate_total(plan_price, extras, people, is_premium):
    # --- Validación (REQ 7) ---
    if people <= 0:
        return -1

    # --- Cálculo base ---
    subtotal = plan_price * people + extras

    # --- Recargo premium (REQ 6) ---
    if is_premium:
        subtotal *= 1.15  # +15%

    # --- Descuento por grupo (REQ 4) ---
    if people >= 2:
        subtotal *= 0.90  # 10% descuento

    # --- Oferta especial si total > 200 (REQ 5) ---
    if subtotal > 200:
        subtotal -= 20

    # Los tests esperan enteros
    return int(subtotal)