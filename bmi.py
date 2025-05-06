def calculate_bmi(height,weight): 
    print("height ",height)
    print("weight " +str(weight))
    bmi = weight/(height*height)
    print("bmi " +str(bmi))
    
    
    if(bmi < 18.5):
        print("Underweight")
        return -1
    elif (bmi >= 18.5 and bmi <=25):
        print ("Normal weight")
        return 0
    else:
        print("Overweight, go and exercise fatty")
        return 1

     

def main():
    output = calculate_bmi(1.7,60)
    print("Return value based on weight classification:", output)
    

if __name__ == "__main__":
    main()