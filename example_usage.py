from client import AlgorithmicPpcBidPaceOptimizerClient

def main():
    client = AlgorithmicPpcBidPaceOptimizerClient()
    res = client.optimize_hourly_bid_pacing(4.2, 550.00, 3500.00)
    print('PPC Bid Pace Optimizer: ' + res['bid_decision_id'] + ' (Target ROAS: ' + str(res['target_roas']) + ')')
    print('Bid Multiplier: ' + str(res['adjusted_cpc_bid_multiplier']) + 'x | Budget Utilization: ' + str(res['projected_eod_budget_utilization_pct']) + '%')
    print('Telemetry URL: ' + res['bid_adjustment_telemetry_url'])

if __name__ == '__main__':
    main()
