#Part A: House Hunting
   #1.total_cost
   #2.portion_dow n_payment​ (assume that portion_down_payment = 0.25 (25%))
   #​3.current_savings​. You start with a currentsavings of $0.
   #4.current_savings*r/12 (Assume that your investments earn a return of r = 0.04 (4%))
   #5.annual_salary
   #6.portion_saved​. (This variable should be in decimal form (i.e. 0.1for 10%))
   #​7. ​monthly salary ​(annual salary / 12)

class House_hunting:

    def __init__(self, total_cost, portion_saved, annual_salary, semi_annual_raise):
        self.total_cost = total_cost
        self.portion_saved = float(portion_saved)
        self.annual_salary = annual_salary
        self.semi_annual_raise = float(semi_annual_raise)


        self.portion_down_payment = (self.total_cost)*0.25
        currentsavings = 0
        r = 0.04
        monthly_salary = (self.annual_salary)/12
        self.number_of_months = 0
        months = 0



        while self.portion_down_payment > currentsavings:
            currentsavings += currentsavings*r/12 + monthly_salary*float(self.portion_saved)
            self.number_of_months = self.number_of_months + 1
            if self.number_of_months % 6 == 0:
                monthly_salary += monthly_salary*self.semi_annual_raise



#create another variable for numbers of months
#that variable will be equal to the numbers of months divide at six
#later will be a conditional function that verify if the number is int or float


a = House_hunting(500000, 0.05, 120000, 0.03)
b = House_hunting(800000, 0.1, 80000, 0.03)


print(b.number_of_months)
print(b.semi_annual_raise)
