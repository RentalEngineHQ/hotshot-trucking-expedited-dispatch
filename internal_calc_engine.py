# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(gross_load_revenue, trip_fuel, broker_factoring_fees, driver_payout=0.00):
    total_system_expense = float(trip_fuel) + float(broker_factoring_fees) + float(driver_payout)
    gross_route_invoiced = float(gross_load_revenue)
    true_net_cash_margin = gross_route_invoiced - total_system_expense
    return [gross_route_invoiced, total_system_expense, true_net_cash_margin]
