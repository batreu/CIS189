class CountyData:
    def __init__(self, rank, per_cap_inc, med_house_inc, med_fam_inc, pop, num_house):
        self.rank = rank
        self.per_cap_inc = per_cap_inc
        self.med_house_inc = med_house_inc
        self.med_fam_inc = med_fam_inc
        self.pop = pop
        self.num_house = num_house


    def __str__(self):
        return "{:}, {:}, {:}, {:}, {:}, {:}".format(self.rank, self.per_cap_inc, self.med_house_inc,
                                                     self.med_house_inc, self.pop, self.num_house)

    def __repr__(self):
        return "PerCapIncomeRank:{:}, PerCapIncome:{:}, MedianHouseIncome{:}, MedianFamIncome:{:}" \
               "Population:{:}, NumberOfHouseholds:{:}"\
            .format(self.rank, self.per_cap_inc, self.med_house_inc,self.med_house_inc, self.pop, self.num_house)