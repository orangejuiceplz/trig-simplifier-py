import math
from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 10

class TrigSimplifier:
    def __init__(self):
        self.special_angles = {
            "pi/6": {
                "sin": "1/2",
                "cos": "sqrt(3)/2",
                "tan": "1/sqrt(3)"
            },
            "pi/4": {
                "sin": "sqrt(2)/2",
                "cos": "sqrt(2)/2",
                "tan": "1"
            },
            "pi/3": {
                "sin": "sqrt(3)/2",
                "cos": "1/2",
                "tan": "sqrt(3)"
            },
            "pi/2": {
                "sin": "1",
                "cos": "0",
                "tan": "undefined"
            },
            "pi": {
                "sin": "0",
                "cos": "-1",
                "tan": "0"
            }
        }
        
        self.mode = "rad"
    
    def set_mode(self, mode):
        """Set angle mode to either 'rad' or 'deg'"""
        if mode.lower() in ["rad", "deg"]:
            self.mode = mode.lower()
            return f"Mode set to {self.mode}"
        return "Invalid mode. Use 'rad' or 'deg'"
    
    def normalize_angle(self, angle_str):
        """Convert angle string to normalized form"""
        angle_str = angle_str.lower().replace(" ", "")
        
        if self.mode == "deg":
            try:
                angle = float(angle_str)
                return str(angle * math.pi / 180)
            except ValueError:
                return angle_str
        
        return angle_str
    
    def simplify(self, expression):
        """Simplify trigonometric expression"""
        expression = expression.lower().replace(" ", "")
        
        for func in ["sin", "cos", "tan"]:
            if func in expression:
                angle_str = expression[expression.find("(") + 1:expression.find(")")]
                angle_str = self.normalize_angle(angle_str)
                
                for special_angle, values in self.special_angles.items():
                    if angle_str == special_angle:
                        return f"{func}({angle_str}) = {values[func]}"
                
                try:
                    if "pi" in angle_str:
                        angle_str = angle_str.replace("pi", str(math.pi))
                    angle = eval(angle_str)
                    
                    if func == "sin":
                        result = math.sin(angle)
                    elif func == "cos":
                        result = math.cos(angle)
                    else:  
                        result = math.tan(angle)
                    
                    result = round(result, 10)
                    return f"{func}({angle_str}) ≈ {result}"
                except:
                    return "Invalid expression"
        
        return "Invalid expression"

def main():
    simplifier = TrigSimplifier()
    
    while True:
        print("\nTrigonometric Expression Simplifier")
        print("==================================")
        print(f"Current mode: {simplifier.mode}")
        print("\nOptions:")
        print("1. Change mode (rad/deg)")
        print("2. Simplify expression")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            mode = input("Enter mode (rad/deg): ")
            print(simplifier.set_mode(mode))
        
        elif choice == "2":
            expr = input("Enter trigonometric expression (e.g., sin(pi/6)): ")
            result = simplifier.simplify(expr)
            print(result)
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()