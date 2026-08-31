def calcular_produtos(volume_litros: float) -> dict:
    """
    Calcula a dosagem exata dos produtos químicos com base no volume da água.
    
    Proporções padrão (por 1.000 Litros):
    - Cloro: 4g (Manutenção)
    - Barrilha (Soda Ash): 15g (Elevação de pH)
    - Floculante: 6ml (Decantação)
    """
    return {
        "cloro_g": round((volume_litros / 1000) * 4, 1),
        "soda_ash_g": round((volume_litros / 1000) * 15, 1),
        "floculante_ml": round((volume_litros / 1000) * 6, 1)
    }