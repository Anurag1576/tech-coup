
gender=input("Who r u (m/f) : ");
# gender=gender.upper();
match gender:
    case "M"|"m":
        ft=input("Select Your foodtime from(B,L,T,D) for breakfast,lunch,teatime and dinner resp. : ")
        match ft:
            case "B"|"b":
                print("A male should consume 300 callories in Breakfast.....")
            case "L"|"l":
                print("A male should consume 200 callories in Lunch.....")
            case "T"|"t":
                print("A male should consume 150 callories in Tea-Time....")
            case "D"|"d" :
                print("A male should consume 100 callories in Dinner.....")
            case _:
                print("Bas kar yaar.....")
    case "F"|"f":
        ft=input("Select Your foodtime from(B,L,T,D) for breakfast,lunch,teatime and dinner resp. : ")
        match ft:
            case "B"|"b":
                print("A female should consume 350 callories in Breakfast.....")
            case "L"|"l":
                print("A female should consume 300 callories in Lunch.....")
            case "T"|"t":
                print("A female should consume 250 callories in Tea-Time....")
            case "D"|"d" :
                print("A female should consume 150 callories in Dinner.....")
            case _:
                print("Its Over-eating.....")
    case _: print("Invalid Selection.....");
 