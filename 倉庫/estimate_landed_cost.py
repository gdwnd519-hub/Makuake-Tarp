import math

def calculate_landed_cost(qty_tarp=50, qty_hammock=50):
    # Parameters
    EXCHANGE_RATE = 150.0 # JPY/USD
    DUTY_RATE = 0.05 # 5%
    TAX_RATE = 0.10 # 10%
    
    # Products
    # Tarp
    TARP = {
        'name': 'Tarp',
        'price': 31.46,
        'weight': 1.23,
        'vol': (33*10*10)/1000000 # 0.0033
    }
    # Hammock
    HAMMOCK = {
        'name': 'Hammock',
        'price': 34.20,
        'weight': 0.9,
        'vol': (25*15*10)/1000000 # 0.00375
    }

    total_qty = qty_tarp + qty_hammock
    
    # 1. EXW Costs
    exw_tarp_usd = qty_tarp * TARP['price']
    exw_hammock_usd = qty_hammock * HAMMOCK['price']
    
    # 2. Weights & Volumes
    weight_tarp = qty_tarp * TARP['weight']
    weight_hammock = qty_hammock * HAMMOCK['weight']
    total_weight = weight_tarp + weight_hammock
    
    vol_tarp = qty_tarp * TARP['vol']
    vol_hammock = qty_hammock * HAMMOCK['vol']
    total_vol = vol_tarp + vol_hammock

    print(f"--- Simulation: {qty_tarp} Tarps + {qty_hammock} Hammocks (Total {total_qty}) ---")

    def calc_mode(mode_name, freight_total_jpy, fixed_cost_jpy=0):
        # Allocating Freight/Fixed Costs based on WEIGHT (common for mixed general cargo)
        # or VOLUME depending on what triggered the cost.
        # Air is usually weight based. Sea is volume based (if LCL).
        
        # Simple allocation by value ratio is easiest, but by weight/vol is more accurate for logistics.
        # Let's allocate Freight by Weight for Air, and by Volume for Sea.
        
        if mode_name == 'Air':
            tarp_ratio = weight_tarp / total_weight
            hammock_ratio = weight_hammock / total_weight
        else: # Sea
            tarp_ratio = vol_tarp / total_vol
            hammock_ratio = vol_hammock / total_vol

        # Allocated Logistics Cost
        logistics_tarp = (freight_total_jpy + fixed_cost_jpy) * tarp_ratio
        logistics_hammock = (freight_total_jpy + fixed_cost_jpy) * hammock_ratio
        
        # Duty & Tax Calculation (Per Product Total)
        # Tarp
        cif_tarp = (exw_tarp_usd * EXCHANGE_RATE) + logistics_tarp # Approx CIF base
        duty_tarp = cif_tarp * DUTY_RATE
        tax_tarp = (cif_tarp + duty_tarp) * TAX_RATE
        total_tarp = cif_tarp + duty_tarp + tax_tarp
        unit_tarp = total_tarp / qty_tarp if qty_tarp > 0 else 0
        
        # Hammock
        cif_hammock = (exw_hammock_usd * EXCHANGE_RATE) + logistics_hammock
        duty_hammock = cif_hammock * DUTY_RATE
        tax_hammock = (cif_hammock + duty_hammock) * TAX_RATE
        total_hammock = cif_hammock + duty_hammock + tax_hammock
        unit_hammock = total_hammock / qty_hammock if qty_hammock > 0 else 0
        
        print(f"\n[{mode_name}]")
        print(f"  > Tarp Unit Cost:    JPY {unit_tarp:,.0f} (Product: JPY {TARP['price']*EXCHANGE_RATE:,.0f} + Log/Tax: JPY {unit_tarp - (TARP['price']*EXCHANGE_RATE):,.0f})")
        print(f"  > Hammock Unit Cost: JPY {unit_hammock:,.0f} (Product: JPY {HAMMOCK['price']*EXCHANGE_RATE:,.0f} + Log/Tax: JPY {unit_hammock - (HAMMOCK['price']*EXCHANGE_RATE):,.0f})")
        return unit_tarp, unit_hammock

    # --- Mode A: Air ---
    # Rate: 1000 JPY/kg
    vol_weight = total_vol * 1000000 / 5000
    chg_weight_air = max(total_weight, vol_weight)
    freight_air = chg_weight_air * 1000
    calc_mode('Air (Courier)', freight_air)

    # --- Mode B: Sea ---
    # Rate: $50/CBM + Fixed 85,000 JPY
    chg_vol_sea = max(1.0, total_vol)
    freight_ocean = (chg_vol_sea * 50 * EXCHANGE_RATE)
    calc_mode('Sea (LCL)', freight_ocean, fixed_cost_jpy=85000)

if __name__ == "__main__":
    calculate_landed_cost(50, 50)
