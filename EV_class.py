class EVs:
    EVs_df = pd.DataFrame()

    # __init__ is a constructor , it assigns values to its attributes when a new Cars object is created
    def __init__(self, n_EV, battery_caps, Charger_id):
        self.n_EV = n_EV  # when assigned , attributes are automatically created for the object
        self.battery_cap = battery_caps
        self.Charger_id = Charger_id

    def EVs_df_create(self, df):
        EVs_dict = {
            'EV': list(range(1, self.n_EV + 1)),
            'battery_cap': self.battery_cap,
            'charger_id': self.Charger_id,
        }

        df = pd.DataFrame(EVs_dict)
        return
