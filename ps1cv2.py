class House_hunting:

    def __init__(self, starting_salary):
        found = False
        max_rate = 100000 #100%
        min_rate = 0      #0%
        r = 0.04
        months = 36
        semi_annual_raise = 0.07
        total_cost = 1000000
        steps = 0
        self.starting_salary = starting_salary
        self.portion_down_payment = total_cost*0.25
        self.bisection_steps = steps
        self.portion_saved = int((max_rate + min_rate) / 2)

        while abs(max_rate-min_rate) > 1:
            self.bisection_steps += 1
            annual_salary = self.starting_salary
            monthly_salary = ((annual_salary)/12)*self.portion_saved/10000
            currentsavings = 0.0

            for i in range(1, months + 1):
                currentsavings += currentsavings*r/12 + monthly_salary
                if abs(currentsavings-self.portion_down_payment) < 100:
                    min_rate = max_rate
                    found = True
                    break
                elif currentsavings > self.portion_down_payment + 100:
                    break

                if i % 6 == 0:
                    annual_salary += annual_salary*semi_annual_raise
                    monthly_salary = (annual_salary/12.0)*self.portion_saved/10000

            if currentsavings < self.portion_down_payment - 100:
                min_rate = self.portion_saved
            elif currentsavings > self.portion_down_payment + 100:
                max_rate = self.portion_saved

            self.portion_saved = int((max_rate + min_rate)/2)

        if found:
            print("Best savings rate:", self.portion_saved / 10000)
            print("Steps in bisection search", self.bisection_steps)

        else:
            print("Is is not possible to pay the down payment in three years")

a = House_hunting(10000)
print(a.starting_salary)
