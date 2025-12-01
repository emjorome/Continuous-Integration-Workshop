def get_membership_plans():
    """Retorna los planes disponibles y sus costos base."""
    return {
        "1": {"name": "Basic", "cost": 100},
        "2": {"name": "Premium", "cost": 150},  # Plan con características premium
        "3": {"name": "Family", "cost": 200}
    }


def get_additional_features():
    """Retorna las características adicionales disponibles."""
    return {
        "1": {"name": "Personal Training", "cost": 50},
        "2": {"name": "Group Classes", "cost": 30},
        "3": {"name": "Sauna Access", "cost": 20}
    }


def calculate_total(base_cost, features_cost, count, is_premium):
    """Realiza el cálculo matemático (Núcleo lógico)."""
    
    # Req 10: Validación de entradas
    if base_cost < 0 or count < 1:
        return -1
    
    # Req 3: Costo base + extras por persona
    subtotal = (base_cost + features_cost) * count

    # Req 4: Descuento por grupo (10%)
    if count >= 2:
        subtotal *= 0.90

    # Req 6: Recargo premium (15%)
    if is_premium:
        subtotal *= 1.15
    
    # Req 5: Descuentos especiales escalonados
    if subtotal > 400:
        subtotal -= 50
    elif subtotal > 200:
        subtotal -= 20
    
    return int(subtotal)


def main():
    print("=== GYM MEMBERSHIP SYSTEM ===")
    
    # --- REQUISITO 1: Selección de Membresía ---
    plans = get_membership_plans()
    print("\nPlanes Disponibles:")
    for key, val in plans.items():
        print(f"{key}. {val['name']} (${val['cost']})")
    
    # Validación de disponibilidad (Req 7)
    plan_choice = input("Seleccione un plan (1-3): ")
    if plan_choice not in plans:
        print("Error: Plan no disponible. Intente de nuevo.")
        return -1

    selected_plan = plans[plan_choice]
    is_premium = (selected_plan["name"] == "Premium")

    # --- REQUISITO 2: Características Adicionales ---
    features = get_additional_features()
    print("\nCaracterísticas Adicionales:")
    for key, val in features.items():
        print(f"{key}. {val['name']} (${val['cost']})")
    
    feature_choice = input("Seleccione característica extra (0 para ninguna): ")
    features_cost = 0
    feature_name = "Ninguna"
    
    # Validación de característica (Req 7)
    if feature_choice != "0":
        if feature_choice in features:
            features_cost = features[feature_choice]["cost"]
            feature_name = features[feature_choice]["name"]
        else:
            print("Error: Característica no válida.")
            return -1

    # Cantidad de personas
    try:
        member_count = int(input("\nNúmero de personas a inscribir: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return -1

    # Cálculo preliminar para la confirmación
    total_cost = calculate_total(selected_plan["cost"], features_cost, member_count, is_premium)

    # --- REQUISITO 8: Confirmación del Usuario ---
    print("\n--- CONFIRMACIÓN DE MEMBRESÍA ---")
    print(f"Plan: {selected_plan['name']}")
    print(f"Extra: {feature_name}")
    print(f"Cantidad de personas: {member_count}")
    print(f"Costo Total Estimado: ${total_cost}")
    
    confirm = input("¿Confirmar membresía? (s/n): ").lower()
    
    if confirm == 's':
        # Req 9: Output final
        print(f"\n¡Éxito! El costo final a pagar es: ${total_cost}")
        return total_cost
    else:
        print("\nOperación cancelada por el usuario.")
        return -1


if __name__ == "__main__":
    main()
