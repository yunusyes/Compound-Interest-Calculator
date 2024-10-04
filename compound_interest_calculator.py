class compound_interest_calculator:
    
    def __init__(self):
        self.amount = 0
        self.interest_rate = 0
        self.years = 0
    
    def calculate(self):
        self.amount = int(input("Enter the principle amount: "))
        self.interest_rate = int(input("Enter the interest rate: "))
        self.years = int(input("Enter the time in years: "))
        calculated_amount = self.amount*(1 + self.interest_rate/100)**self.years
        return calculated_amount
        
def main():
    calc = compound_interest_calculator()
    result = calc.calculate()
    print(result)
    
if __name__ == "__main__":
    main()


    
    