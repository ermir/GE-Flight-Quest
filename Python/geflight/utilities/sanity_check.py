import pandas as pd

def sanity_check(pred, mode):
    if mode == "training":

        combined_on_id = pd.merge(left=pred.flight_predictions, right=pred.test_data,
            on='flight_history_id', suffixes=('_predicted', '_actual'),  sort=False)

        j = 0; k = 0

        print ""
        print "\t\tPrediction problems:"
        for i, row in combined_on_id.iterrows():
            
            if row['actual_runway_arrival_predicted'] < 0 or row['actual_runway_arrival_predicted'] > 1980:
                print "\t\tSanity prob flight {}! era: {}, ara: {}"\
                .format(row['flight_history_id'], row['actual_runway_arrival_predicted'], row['actual_runway_arrival_actual'])

            if abs(row['actual_runway_arrival_actual'] - row['actual_runway_arrival_predicted']) > 59:
                print "\t\tPred prob flight {}! era: {}, ara: {}, diff: {}"\
                .format(row['flight_history_id'], row['actual_runway_arrival_predicted'], row['actual_runway_arrival_actual'],
                    row['actual_runway_arrival_actual'] - row['actual_runway_arrival_predicted'])

            if row['actual_gate_arrival_predicted'] < 0 or row['actual_gate_arrival_predicted'] > 1980:
                print "\t\tSanity prob flight {}! ega: {}, aga: {}"\
                .format(row['flight_history_id'], row['actual_gate_arrival_predicted'], row['actual_gate_arrival_actual'])

            if abs(row['actual_gate_arrival_actual'] - row['actual_gate_arrival_predicted']) > 59:
                print "\t\tPred prob flight {}! ega: {}, aga: {}, diff: {}"\
                .format(row['flight_history_id'], row['actual_gate_arrival_predicted'], row['actual_gate_arrival_actual'],
                    row['actual_gate_arrival_actual'] - row['actual_gate_arrival_predicted'])

            if abs(row['actual_runway_arrival_actual'] - row['actual_runway_arrival_predicted']) > 10:
                j = j + 1

            if abs(row['actual_gate_arrival_actual'] - row['actual_gate_arrival_predicted']) > 10:
                k = k + 1


        print "\t\tNum runway wrong: {} %".format(100 * j / float(len(combined_on_id)))
        print "\t\tNum gate wrong: {} %".format(100 * k / float(len(combined_on_id)))
        print "\t",

    elif mode == "leaderboard":
        for i, row in pred.flight_predictions.iterrows():
            pass
