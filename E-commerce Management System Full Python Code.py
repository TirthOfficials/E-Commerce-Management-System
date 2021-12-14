#**********E-COMMERCE MANAGEMENT SYSTEM**********

"""

    Creator: Tirth Patel

    
"""
#please enter valid email id whenever asked as we have used 'smptlib' library
import smtplib
import random
from pandas import Series
Price_Array=[]
Name_Array=[]
def Bill():
    print("*********Your Bill is*********")
    print("\n")
    print("Prices                     Products")
    Obj=Series(Name_Array,index=Price_Array)
    print(Obj)
    
    total=sum(Price_Array)
    print("\n*******So the total price to pay will be*******")
    print("\n")
    print(total)
    print("\n*******Please enter your Address*******\n")
    address=input("Address: ")
    print("\n*******Choose your payment method*******")
    print("\npress 1 : Debit Card/ Credit Card \n\npress 2 : Cash On Delivery")
    while (1):
        pay=int(input("\nEnter your choice: "))

        if pay==1:
            
            while(1):
        
                print("\n------TRANSACTION------")
                name1=input("\nEnter name of card holder: ")
                debit1=int(input("\nEnter your (16 digit) credit card or debit card number: "))
                debitt1=str(debit1)
                len1=len(debitt1)
                cvv1=int(input("\nEnter (3 digit) CVV number: "))
                cvvv1=len(str(cvv1))
                
                
                        
        
                if len1==16 and cvvv1==3:
                    number1 = random.randint(1000,9999)
                    y="Your Verification code is ",number1
                    email_user = '<Enter Sender Email Address>'
        
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email_user,'<Enter sender email address password(Valid Google Password)>')
                    message = str(y)
                    server.sendmail(email_user,email_send,message)
                    server.quit()
                    strnum1=str(number1)
                    print("\nPlease check your email address you will get a Verification code")
                    print(" ")
                    while(1):
                        VC1=input("\nEnter your Verification code: ")
                        if(VC1==strnum1):
                            print("\nVerification Successful")
                            print(" ")
                            print("\nMr./Mrs. ",name1," your debit card number with last 4 digit XXXX XXXX XXXX",debitt1[12:16]," \n Rs. ",total," has successfully deducted from your debit card")
                            
                            fbill="Mr./Mrs. ",name1," your debit card number with last 4 digit XXXX XXXX XXXX",debitt1[12:16]," Rs. ",total," has successfully deducted from your debit card. You purchased ",Name_Array, " ----> ",Price_Array,". If your have any query or problem regarding transaction please reply to this email"
                            
                            print("\nYour product will be delivered in 2-3 days at given address ",address,"")
                    
                            server = smtplib.SMTP('smtp.gmail.com',587)
                            server.starttls()
                            server.login(email_user,'<Enter sender email address password(Valid Google Password)>')
                            message = str(fbill)
                            server.sendmail(email_user,email_send,message)
                            server.quit()
                            print("\nPlease go and check your email of your transaction")
                            server = smtplib.SMTP('smtp.gmail.com',587)
                            server.starttls()
                            server.login(email_user,'<Enter sender email address password(Valid Google Password)>')
                            message = 'Thanks for purchasing item from ECMS your product will be delivered in 2-3 days at given address. If your have any other query please reply to this email'
                            server.sendmail(email_user,email_send,message)
                            server.quit()
                            print("\nThank you for choosing our service")
                            D=(input("\nPlease rate our project:"))
                            print("\nThanks for your review")
                            break
                        else:
                            print("Please enter valid OTP")
                    break
                else:
                    print("Incorrect debit card number or CVV number")
                    print("Reenter details")
                    
            break
        elif pay==2:
            print("\nYour product will be delivered in 2-3 days on address ",address,"")
            
            fbill="So in total You have to pay Rs. ",total," by cash. You have purchased ",Name_Array," ----> ",Price_Array,"If your have any other query please reply to this email"
            email_user = '<Enter sender email address>'
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,'<Enter sender email address password(Valid Google Password)>')
            message = str(fbill)
            server.sendmail(email_user,email_send,message)
            
            server.quit()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,'<Enter sender email address password(Valid Google Password)>')
            taddress= 'Thanks for purchasing item from ECMS your product will be delivered in 2-3 days at',address,'. If your have any query or problem regarding delivery please replay to this email'
            message = str(taddress)
            server.sendmail(email_user,email_send,message)
            server.quit()
            print("please go and check your email")
            print("\nThank you for choosing our service")
            D=(input("\nPlease rate our project: "))
            print("\nThanks for your review")
            break
        else:
            print("Please enter valid choice")

def ask_next():
    while(1):
            print("\n\n1.Continue Shopping\n\n2.Complete Shopping\n\n3.Exit")
            d=int(input("\n\nEnter the Choice:"))
            if d==1:
                main()
                break
            
            if d==2:
                Bill()
                break
            if d==3:
                exit
                break
            else:
                    print("\n\nError Plese enter valid choice")


##############
def BeautyHelthcare(a):
    while(1):
        bh_file=open("Beauty_and_healthcare.txt","r")
        while(1):
            x=bh_file.readline()
            if(x==""):
                break
            print(x)
        bh=int(input("\nEnter your choice:"))
        if(bh==1):
            print("\nForest Essentials Nargis Velvet Silk Body Cream, 6.7 Fl Oz-------->Rs=2000")
            pr=2000
            name="Forest Essentials Nargis Velvet Silk Body Cream, 6.7 Fl Oz"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==2):
            print("\nL'Occitane Cherry Blossom Hand Cream-30ml-------->Rs=700")
            pr=700
            name="L'Occitane Cherry Blossom Hand Cream-30ml"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==3):
            print("\nTree Hut Shea Moisturizing Body Lotion Moroccan Rose, 255g-------->Rs=600")
            pr=600
            name="Tree Hut Shea Moisturizing Body Lotion Moroccan Rose, 255g"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==4):
            print("\nYves Rocher Energizing Body Lotion, Mango Coriander, 200ml-------->Rs=500")
            pr=500
            name="Yves Rocher Energizing Body Lotion, Mango Coriander, 200ml"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==5):
            print("\nForest Essentials Night Cream, Kumkumadi Keram, 30g-------->Rs=2075")
            pr=2075
            name="Forest Essentials Night Cream, Kumkumadi Keram, 30g"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==6):
            print("\n Maybelline New York Color Sensational Creamy Matte Lipstick-------->Rs=500")
            pr=500
            name=" Maybelline New York Color Sensational Creamy Matte Lipstick"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==7):
            print("\nLakme Absolute Plump and Shine Lip Gloss, Beige Shine, 3g-------->Rs=400")
            pr=400
            name="Lakme Absolute Plump and Shine Lip Gloss, Beige Shine, 3g"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==8):
            print("\nMaybelline New York Colossal Kajal, Black, 0.35g-------->Rs=150")
            pr=150
            name="Maybelline New York Colossal Kajal, Black, 0.35g"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==9):
            print("\nDeBelle Gel Nail Polish Victorian Beige (Beige Nail Polish), 8ml-------->Rs=270")
            pr=270
            name="DeBelle Gel Nail Polish Victorian Beige (Beige Nail Polish), 8ml"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==10):
            print("\nGeneric Foundation, Eyeshadow Makeup Brush Set, Pink-------->Rs=250")
            pr=250
            name="Generic Foundation, Eyeshadow Makeup Brush Set, Pink"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==11):
            print("\nVicks Vaporub - 50ml-------->Rs=110")
            pr=110
            name="Vicks Vaporub - 50ml"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==12):
            print("\nSkudgear Advanced Breathable Neoprene Ankle Support Compression Brace-------->Rs=400")
            pr=400
            name="Skudgear Advanced Breathable Neoprene Ankle Support Compression Brace"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==13):
            print("\nDr. Morepen 09 Fully Automatic BP Monitor-------->Rs=1400")
            pr=1400
            name="Dr. Morepen 09 Fully Automatic BP Monitor"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==14):
            print("\nTrexgenics Smartvision Advanced Eye Care Multivitamin-------->Rs=900")
            pr=900
            name="Trexgenics Smartvision Advanced Eye Care Multivitamin"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==15):
            print("\nMack'S Ear Care Ultra Soft Foam Earplugs, 50 Count-------->Rs=1700")
            pr=1700
            name="Mack'S Ear Care Ultra Soft Foam Earplugs, 50 Count"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==16):
            print("\nDove Intense Repair Shampoo, 1L-------->Rs=500")
            pr=500
            name="Dove Intense Repair Shampoo, 1L"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==17):
            print("\nTRESemme Keratin Smooth Conditioner-------->Rs=180")
            pr=180
            name="TRESemme Keratin Smooth Conditioner"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==18):
            print("\nNihar Shanti Amla and Badam Hair Oil-------->Rs=140")
            pr=140
            name="Nihar Shanti Amla and Badam Hair Oil"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==19):
            print("\nL'Oreal Paris Excellence Creme Hair Color, Black-------->Rs=530")
            pr=530
            name="L'Oreal Paris Excellence Creme Hair Color, Black"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==20):
            print("\nBEARDO Hair Wax, Strong Hold-------->Rs=200")
            pr=200
            name="BEARDO Hair Wax, Strong Hold"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==21):
            print("\nAxe Signature Dark Temptation-------->Rs=180")
            pr=180
            name="Axe Signature Dark Temptation"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==22):
            print("\nEngage M1 Perfume Spray For Men-------->Rs=160")
            pr=160
            name="Engage M1 Perfume Spray For Men"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==23):
            print("\nFogg Fresh Deodorant Combo for Men-------->Rs=450")
            pr=450
            name="Fogg Fresh Deodorant Combo for Men"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==24):
            print("\nNIVEA Men Deodorant, Fresh Active Original, 150ml-------->Rs=145")
            pr=145
            name="NIVEA Men Deodorant, Fresh Active Original, 150ml"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bh==25):
            print("\nEnvy Men Perfume, 30ml-------->Rs=120")
            pr=120
            name="Envy Men Perfume, 30ml"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        else:
            printf("\nPlease enter valid choice.")

##############
def Bags(a):
    while(1):
        bag_file=open("Bags_and_Luggage.txt","r")
        while(1):
            x=bag_file.readline()
            if(x==""):
                break
            print(x)
        bag=int(input("\nEnter your choice:"))
        if(bag==1):
            print("\nPOLESTAR Noble Blue School Bag-------->Rs=530")
            pr=530
            name="POLESTAR Noble Blue School Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==2):
            print("\nWildcraft 44 Ltrs Wolf_Blk Casual Backpack-------->Rs=1270")
            pr=1270
            name="Wildcraft 44 Ltrs Wolf_Blk Casual Backpack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==3):
            print("\nAmerican Tourister 32 Ltrs Black Casual Backpack-------->Rs=1100")
            pr=1100
            name="American Tourister 32 Ltrs Black Casual Backpack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==4):
            print("\nSkybags SB Marvel 27 Ltrs Red School Backpack-------->Rs=700")
            pr=700
            name="Skybags SB Marvel 27 Ltrs Red School Backpack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==5):
            print("\nDoraemon Digital Print Polyester School Bag-------->Rs=400")
            pr=400
            name="Doraemon Digital Print Polyester School Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==6):
            print("\nWildcraft 45 Ltrs Grey and Orange Rucksack-------->Rs=1400")
            pr=1400
            name="Wildcraft 45 Ltrs Grey and Orange Rucksack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==7):
            print("\nAristocrat 45 Ltrs Black Rucksack-------->Rs=1200")
            pr=1200
            name="Aristocrat 45 Ltrs Black Rucksack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==8):
            print("\nSkybags Sonic 49 Ltrs Green Rucksack-------->Rs=1900")
            pr=1900
            name="Skybags Sonic 49 Ltrs Green Rucksack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==9):
            print("\nF Gear Orion 46 Ltrs Navy Blue, Black Rucksack-------->Rs=1300")
            pr=1300
            name="F Gear Orion 46 Ltrs Navy Blue, Black Rucksack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==10):
            print("\nWILDCRAFT RUCKSACK-------->Rs=1400")
            pr=1400
            name="WILDCRAFT RUCKSACK"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==11):
            print("\nAmerican Tourister Ivy Polypropylene Black Hardsided Check-in Luggage-------->Rs=3000")
            pr=3000
            name="American Tourister Ivy Polypropylene Black Hardsided Check-in Luggage"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==12):
            print("\nSkybags Trooper Polycarbonate Blue Hardsided Cabin Luggage-------->Rs=2500")
            pr=2500
            name="Skybags Trooper Polycarbonate Blue Hardsided Cabin Luggage"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==13):
            print("\nSafari Thorium Sharp Antiscratch Black Check-In Hard Suitcase-------->Rs=3700")
            pr=3700
            name="Safari Thorium Sharp Antiscratch Black Check-In Hard Suitcase"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==14):
            print("\nAmerican Tourister Cruze ABS Black Hardsided Suitcase-------->Rs=4500")
            pr=4500
            name="American Tourister Cruze ABS Black Hardsided Suitcase"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==15):
            print("\nVIP Pisa Polyester Red Softsided Check-in Luggage-------->Rs=4300")
            pr=4300
            name="VIP Pisa Polyester Red Softsided Check-in Luggage"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==16):
            print("\nSwiss Military Canvas Beige Sling Bag-------->Rs=800")
            pr=800
            name="Swiss Military Canvas Beige Sling Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==17):
            print("\nGOCART WITH G LOGO Oxford Cloth Elastic Arm Bag-------->Rs=400")
            pr=400
            name="GOCART WITH G LOGO Oxford Cloth Elastic Arm Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==18):
            print("\nTom & Gee Leather Messenger Bag-------->Rs=550")
            pr=550
            name="Tom & Gee Leather Messenger Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==19):
            print("\nKILLER Men's Sling Bag (Blue)-------->Rs=700")
            pr=700
            name="KILLER Men's Sling Bag (Blue)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==20):
            print("\nCOSMUS Polyester 9 Ltr Navy Blue Messenger Bag-------->Rs=500")
            pr=500
            name="COSMUS Polyester 9 Ltr Navy Blue Messenger Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==21):
            print("\nKILLER Eaton 31 L Polyester Gym Bag-------->Rs=600")
            pr=600
            name="KILLER Eaton 31 L Polyester Gym Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==22):
            print("\nN-Blues Comfortable Casual Gym Bag 20L-------->Rs=600")
            pr=600
            name="N-Blues Comfortable Casual Gym Bag 20L"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==23):
            print("\nPUMA Gym Bag IND II Fig-CASTLEROCK-------->Rs=500")
            pr=500
            name="PUMA Gym Bag IND II Fig-CASTLEROCK"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==24):
            print("\nAUXTER Blacky Leatherette Gym Bag-------->Rs=360")
            pr=360
            name="AUXTER Blacky Leatherette Gym Bag"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(bag==25):
            print("\nTHEDZIRE Medium Travel Duffel Bag,Waterproof Synthetic Leather-------->Rs=350")
            pr=350
            name="THEDZIRE Medium Travel Duffel Bag,Waterproof Synthetic Leather"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        else:
            print("\nPlease enter valid choice.")

##############
def Electronics(a):
    while(1):
        ele_file=open("Electronics.txt","r")
        while(1):
            x=ele_file.readline()
            if(x==""):
                break
            print(x)
        ele=int(input("\nEnter your choice:"))
        if(ele==1):
            print("\nSamsung 32 inches Wondertainment Series HD Ready LED Smart TV-------->Rs=16000")
            pr=16000
            name="Samsung 32 inches Wondertainment Series HD Ready LED Smart TV"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==2):
            print("\nMi TV 4X 50 Inches 4K Ultra HD Android LED TV-------->Rs=35000")
            pr=35000
            name="Mi TV 4X 50 Inches 4K Ultra HD Android LED TV"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==3):
            print("\nLG 55 inches 55SK8500PTA 4K Super UHD LED Smart TV-------->Rs=125000")
            pr=125000
            name="LG 55 inches 55SK8500PTA 4K Super UHD LED Smart TV"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==4):
            print("\nSony Bravia 43 inches Full HD Smart LED TV KDL-43W6603-------->Rs=35000")
            pr=35000
            name="Sony Bravia 43 inches Full HD Smart LED TV KDL-43W6603"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==5):
            print("\nOnePlus Y Series 43 inches Full HD LED Smart Android TV 43Y1-------->Rs=25000")
            pr=25000
            name="OnePlus Y Series 43 inches Full HD LED Smart Android TV 43Y1"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==6):
            print("\nLG 1.5 Ton 5 Star Inverter Split AC Copper, LS-Q18YNZA, Convertible 4-in-1 Cooling-------->Rs=41000")
            pr=41000
            name="LG 1.5 Ton 5 Star Inverter Split AC Copper, LS-Q18YNZA, Convertible 4-in-1 Cooling"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==7):
            print("\nVoltas 1.5 Ton 3 Star Inverter Split AC (Copper 183VCZS)-------->Rs=34000")
            pr=34000
            name="Voltas 1.5 Ton 3 Star Inverter Split AC (Copper 183VCZS)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==8):
            print("\nWhirlpool 1 Ton 3 Star 2020 Split AC with Copper Condenser-------->Rs=25500")
            pr=25500
            name="Whirlpool 1 Ton 3 Star 2020 Split AC with Copper Condenser"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==9):
            print("\nLG 2 Ton 3 Star Inverter Split AC (Copper, 2019 Model, KS-Q24ENXA)-------->Rs=50000")
            pr=50000
            name="LG 2 Ton 3 Star Inverter Split AC (Copper, 2019 Model, KS-Q24ENXA)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==10):
            print("\nPanasonic 1.5 Ton 5 Star Wi-Fi Twin Cool Inverter Split AC (Copper, PM 2.5 Filter, 2020 Model, CS/CU-NU18WKYW)-------->Rs=41000")
            pr=41000
            name="Panasonic 1.5 Ton 5 Star Wi-Fi Twin Cool Inverter Split AC (Copper, PM 2.5 Filter, 2020 Model, CS/CU-NU18WKYW)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==11):
            print("\nGodrej 190 L 5 Star Inverter Direct-Cool Single Door Refrigerator-------->Rs=16000")
            pr=16000
            name="Godrej 190 L 5 Star Inverter Direct-Cool Single Door Refrigerator"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==12):
            print("\nLG 420 L 3 Star Frost Free Double Door Refrigerator (GL-I472QPZX)-------->Rs=41000")
            pr=41000
            name="LG 420 L 3 Star Frost Free Double Door Refrigerator (GL-I472QPZX)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==13):
            print("\nHaier 320 L 2 Star Inverter Frost-Free Double Door Refrigerator-------->Rs=26000")
            pr=26000
            name="Haier 320 L 2 Star Inverter Frost-Free Double Door Refrigerator"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==14):
            print("\nSamsung 198 L 5 Star Inverter Direct Cool Single Door Refrigerator-------->Rs=17500")
            pr=17500
            name="Samsung 198 L 5 Star Inverter Direct Cool Single Door Refrigerator"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==15):
            print("\nGodrej 260 L 3 Star Inverter Frost-Free Double Door Refrigerator-------->Rs=23000")
            pr=23000
            name="Godrej 260 L 3 Star Inverter Frost-Free Double Door Refrigerator"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==16):
            print("\nDell G3 3500 Gaming Laptop with 15.6 Inch-------->Rs=73000")
            pr=73000
            name="Dell G3 3500 Gaming Laptop with 15.6 Inch"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==17):
            print("\nHP Pavilion x360 Touchscreen 2-in-1 FHD 14-inch Laptop -------->Rs=52000")
            pr=52000
            name="HP Pavilion x360 Touchscreen 2-in-1 FHD 14-inch Laptop "
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==18):
            print("\nLenovo ThinkPad E14 AMD Ryzen 5 4500U 14-inch Thin and Light Laptop-------->Rs=50000")
            pr=50000
            name="Lenovo ThinkPad E14 AMD Ryzen 5 4500U 14-inch Thin and Light Laptop"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==19):
            print("\nApple MacBook Pro (16-inch Silver)-------->Rs=240000")
            pr=240000
            name="Apple MacBook Pro (16-inch Silver)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==20):
            print("\nASUS TUF Gaming FX705DT 17.3 FHD Laptop-------->Rs=70000")
            pr=70000
            name="ASUS TUF Gaming FX705DT 17.3 FHD Laptop"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==21):
            print("\nMSI WS75, Intel 10th Gen. i7-10875H, 17.3 Workstation Laptop-------->Rs=290000")
            pr=290000
            name="MSI WS75, Intel 10th Gen. i7-10875H, 17.3 Workstation Laptop"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==22):
            print("\nMi 10i 5G (Midnight Black)-------->Rs=24000")
            pr=24000
            name="Mi 10i 5G (Midnight Black)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==23):
            print("\nOnePlus Nord 5G (Blue Marble)-------->Rs=30000")
            pr=30000
            name="OnePlus Nord 5G (Blue Marble)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==24):
            print("\nOnePlus 8T 5G (Aquamarine Green)-------->Rs=46000")
            pr=46000
            name="OnePlus 8T 5G (Aquamarine Green)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==25):
            print("\nSamsung Galaxy Note 20 Ultra 5G (Mystic Black)-------->Rs=105000")
            pr=105000
            name="Samsung Galaxy Note 20 Ultra 5G (Mystic Black)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==26):
            print("\nVivo V20 Pro 5G (Midnight Jazz)-------->Rs=30000")
            pr=30000
            name="Vivo V20 Pro 5G (Midnight Jazz)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==27):
            print("\nOPPO F17 Pro (Matte Black)-------->Rs=21500")
            pr=21500
            name="OPPO F17 Pro (Matte Black)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(ele==28):
            print("\nApple iPhone 12 Pro Max - Pacific Blue-------->Rs=130000")
            pr=130000
            name="Apple iPhone 12 Pro Max - Pacific Blue"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        else:
            print("\nPlease enter valid choice.")

##############
def GroceryHouseHoldSupplies(a):
    while(1):
        gh_file=open("Grocery_and_household.txt","r")
        while(1):
            x=gh_file.readline()
            if(x==""):
                break
            print(x)
        gro=int(input("\nEnter your choice:"))
        if(gro==1):
            print("\nTetley Green Tea Bags - Ginger, Mint & Lemon, 100 Bags-------->Rs=420")
            pr=420
            name="Tetley Green Tea Bags - Ginger, Mint & Lemon, 100 Bags"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==2):
            print("\n Lipton Honey Lemon Green Tea Bags, 100 Pc-------->Rs=400")
            pr=400
            name=" Lipton Honey Lemon Green Tea Bags, 100 Pc"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==3):
            print("\nWagh Bakri Premium Leaf Tea Poly Pack, 1kg-------->Rs=400")
            pr=400
            name="Wagh Bakri Premium Leaf Tea Poly Pack, 1kg"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==4):
            print("\nTata Tea Gold, 1kg-------->Rs=550")
            pr=550
            name="Tata Tea Gold, 1kg"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==5):
            print("\nNescafe Classic Coffee, 100g Dawn Jar-------->Rs=255")
            pr=255
            name="Nescafe Classic Coffee, 100g Dawn Jar"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==6):
            print("\nZandu Pure Honey, 500g-------->Rs=175")
            pr=175
            name="Tata Tea Gold, 1kg"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==7):
            print("\nFortune Sunlite Refined Sunflower Oil, 1L-------->Rs=145")
            pr=145
            name="Fortune Sunlite Refined Sunflower Oil, 1L"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==8):
            print("\nFortune Kachi Ghani Pure Mustard Oil, 1L (Pet Bottle)-------->Rs=160")
            pr=160
            name="Fortune Kachi Ghani Pure Mustard Oil, 1L (Pet Bottle)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==9):
            print("\nDhampure White Crystal Sugar, 5kg-------->Rs=220")
            pr=220
            name="Dhampure White Crystal Sugar, 5kg"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==10):
            print("\nTata Sampann Turmeric Powder Masala, 200g-------->Rs=55")
            pr=55
            name="Tata Sampann Turmeric Powder Masala, 200g"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==11):
            print("\nSaffola Masala Oats, Classic Masala, 500g-------->Rs=170")
            pr=170
            name="Saffola Masala Oats, Classic Masala, 500g"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==12):
            print("\nQuaker Oats, 2kg-------->Rs=260")
            pr=260
            name="Quaker Oats, 2kg"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==13):
            print("\nKellogg's Corn Flakes Real Almond and Honey, 1 kg-------->Rs=520")
            pr=520
            name="Kellogg's Corn Flakes Real Almond and Honey, 1 kg"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==14):
            print("\nKellogg's Chocos, High in Protein, B Vitamins, Calcium And Iron, 1.2kg Pack-------->Rs=460")
            pr=460
            name="Kellogg's Chocos, High in Protein, B Vitamins, Calcium And Iron, 1.2kg Pack"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==15):
            print("\nNestle NesPlus Breakfast Cereal - Crunchy Flakes with Corn & Oats, 475g Carton-------->Rs=160")
            pr=160
            name="Nestle NesPlus Breakfast Cereal - Crunchy Flakes with Corn & Oats, 475g Carton"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==16):
            print("\nMilton Executive Lunch Box Soft Insulated Tiffin Box (2 SS Container,1 Microwave Safe Container),Green-------->Rs=300")
            pr=300
            name="Milton Executive Lunch Box Soft Insulated Tiffin Box (2 SS Container,1 Microwave Safe Container),Green"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==17):
            print("\nLarah by Borosil Green Leaves Silk Series Opalware Dinner Set, 35 Pieces, White-------->Rs=1800")
            pr=1800
            name="Larah by Borosil Green Leaves Silk Series Opalware Dinner Set, 35 Pieces, White"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==18):
            print("\nMilton Thermosteel Carafe Flask Tea/ Coffee Pot Tea/ Coffee Pot, 1000 ml, Silver-------->Rs=1000")
            pr=1000
            name="Milton Thermosteel Carafe Flask Tea/ Coffee Pot Tea/ Coffee Pot, 1000 ml, Silver"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==19):
            print("\nMilton Astir 750 Thermosteel Hot and Cold Water Bottle, 710 ml, Blue-------->Rs=800")
            pr=800
            name="Milton Astir 750 Thermosteel Hot and Cold Water Bottle, 710 ml, Blue"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==20):
            print("\nBorosil - Carafe Flame Proof Glass Kettle With Stainer, 650 ml-------->Rs=500")
            pr=500
            name="Borosil - Carafe Flame Proof Glass Kettle With Stainer, 650 ml"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==21):
            print("\nAlnico Decor Metal Flower Vase (26 Inches, Black)-------->Rs=1900")
            pr=1900
            name="Alnico Decor Metal Flower Vase (26 Inches, Black)"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==22):
            print("\nAADIT CRREATION Metallic Flower Vase-------->Rs=600")
            pr=600
            name="AADIT CRREATION Metallic Flower Vase"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==23):
            print("\nFabzone Marble Dust Radha Krishna Idol | Radhey Shyam , White, 19 Inches, 1 Piece-------->Rs=9500")
            pr=9500
            name="Fabzone Marble Dust Radha Krishna Idol | Radhey Shyam , White, 19 Inches, 1 Piece"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==24):
            print("\neCraftIndia White Metal Cow and Calf-------->Rs=240")
            pr=240
            name="eCraftIndia White Metal Cow and Calf"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        elif(gro==25):
            print("\nJaipurCrafts Brass Gramophone Showpiece, 17 CM, Gold, 1 Piece-------->Rs=370")
            pr=370
            name="JaipurCrafts Brass Gramophone Showpiece, 17 CM, Gold, 1 Piece"
            Price_Array.append(pr)
            Name_Array.append(name)
            ask_next()
            break
        else:
            print("\nPlease enter valid choice.")
##############
def Books(a):
    while(1):
        Bo_file=open("Books.txt","r")
        while(1):
            y=Bo_file.read()
            if(y==""):
                break
            print(y)
        d=int(input("Enter your choice:"))
        if(d==1):
            print("Treasure Island-------->Rs=130")
            Price=130
            name="Treasure Island"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==2):
            print("Around the World in 80 Days-------->Rs=120")
            Price=120
            name="Around the World in 80 Days"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==3):
            print("2000 LEAGUES UNDER THE SEA-------->Rs=190")
            Price=190
            name="2000 LEAGUES UNDER THE SEA"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==4):
            print("The Adventures of Tom Sawyer-------->Rs=140")
            Price=140
            name="The Adventures of Tom Sawyer"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==5):
            print("The Great Gatsby-------->Rs=190")
            Price=190
            name="The Great Gatsby"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==6):
            print("The Catcher in the Rye-------->Rs=220")
            Price=220
            name="The Catcher in the Rye"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==7):
            print("Chanakya Neeti-------->Rs=218")
            Price=218
            name="Chanakya Neeti"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==8):
            print("Oliver Twist-------->Rs=160")
            Price=160
            name="Oliver Twist"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==9):
            print("THE INVINCIBLE IRON MAN: Armour Wars-------->Rs=1000")
            Price=1000
            name="THE INVINCIBLE IRON MAN: Armour Wars"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==10):
            print("The Killing Joke-------->Rs=850")
            Price=850
            name="The Killing Joke"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==11):
            print("X-MAN:Days of Future Past-------->Rs=1500")
            Price=1500
            name="X-MAN:Days of Future Past"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==12):
            print("Ghost World-------->Rs=450")
            Price=450
            name="Ghost World"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==13):
            print("A Time for Mercy-------->Rs=630")
            Price=630
            name="A Time for Mercy"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==14):
            print("The Murder at the Vicarage-------->Rs=205")
            Price=205
            name="The Murder at the Vicarage"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==15):
            print("The Searcher-------->Rs=1200")
            Price=1200
            name="The Searcher"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break          
        elif(d==16):
            print("The Girl on the Train-------->Rs=200")
            Price=200
            name="The Girl on the Train"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==17):
            print("The Name of the Wind-------->Rs=400")
            Price=400
            name="The Name of the Wind"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==18):
            print("Assassian's Apprentice-------->Rs=400")
            Price=400
            name="Assassian's Apprentice"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==19):
            print("The Magicians-------->Rs=600")
            Price=600
            name="The Magicians"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(d==20):
            print("The Gunslinger-------->Rs=1000")
            Price=1000
            name="The Gunslinger"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        else:
            print("Please enter valid choice.")

##############
def Entertainment(a):
    while(1):
        En_file=open("Entertainment.txt","r")
        while(1):
            x=En_file.readline()
            if(x==""):
                break
            print(x)
        Ent=int(input("Enter your Choice:"))
        if(Ent==1):
            print("TENET-------->Rs=1800")
            Price=1800
            name="TENET"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==2):
            print("Avengers Endgame-------->Rs=3700")
            Price=3700
            name="Avengers Endgame"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==3):
            print("3-idiots-------->Rs=800")
            Price=800
            name="3-iditos"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==4):
            print("Interstellar-------->Rs=3000")
            Price=3000
            name="Interstellar"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==5):
            print("The Matrix-------->Rs=1000")
            Price=1000
            name="The Matrix"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==6):
            print("Joker-------->Rs=1700")
            Price=1700
            name="Joker"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==7):
            print("Titanic-------->Rs=470")
            Price=470
            name="Titanic"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==8):
            print("Iron Man Trilogy-------->Rs=2760")
            Price=2760
            name="Iron Man Trilogy"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==9):
            print("Capitan America Trilogy-------->Rs=2460")
            Price=2460
            name="Captian America Trilogy"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==10):
            print("Thor Trilogy-------->Rs=2700")
            Price=2700
            name="Thor Trilogy"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==11):
            print("Doctor Strange-------->Rs=1500")
            Price=1500
            name="Doctor Strange"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==12):
            print("Justice League-------->Rs=460")
            Price=460
            name="Justice League"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==13):
            print("Sutter Island-------->Rs=500")
            Price=500
            name="Sutter Island"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==14):
            print("The Dark Knight-------->Rs=2000")
            Price=2000
            name="The Dark Knight"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==15):
            print("Avatar-------->Rs=1200")
            Price=1200
            name="Avatar"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==16):
            print("Deadpool-------->Rs=700")
            Price=700
            name="Deadpool"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==18):
            print("Harry Potter-------->Rs=6500")
            Price=6500
            name="Harry Potter"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==19):
            print("Furious 7-------->Rs=500")
            Price=500
            name="Furious 7"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==20):
            print("Jurassic Park-------->Rs=1200")
            Price=1200
            name="Jurassic Park"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(Ent==17):
            print("Mission Impossible-------->Rs=4500")
            Price=4500
            name="Mission Impossible"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        else:
            print("Please enter valid choice.")
    
    


##############
def Sports(a):
    while(1):
        Sp_file=open("Sports.txt","r")
        while(1):
            x=Sp_file.readline()
            if(x==""):
                break
            print(x)
        c=int(input("Enter your Choice:"))
        if(c==1):
            print("Nike Leg Guard-------->Rs=1500")
            Price=1500
            name="Nike Leg Guard"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==2):
            print("SG Leg Guard-------->Rs=500")
            Price=500
            name="SG Leg Guard"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==3):
            print("Navia Leg Guard-------->Rs=1200")
            Price=1200
            name="Navia Leg Guard"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==4):
            print("Nike Helmet-------->Rs=2000")
            Price=2000
            name="Nike Helmet"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==5):
            print("Navia Helmet-------->Rs=2500")
            Price=2500
            name="Navia Helmet"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==6):
            print("SG Helmet-------->Rs=1800")
            Price=1800
            name="SG Helmet"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==7):
            print("Nike Bat-------->Rs=2000")
            Price=2000
            name="Nike Bat"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==8):
            print("Navia Bat-------->Rs=2500")
            Price=2500
            name="Navia Bat"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==9):
            print("SG Bat-------->Rs=1200")
            Price=1200
            name="SG Bat"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==10):
            print("Nike Football-------->Rs=1600")
            Price=1600
            name="Nike Football"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==11):
            print("Adidas Football-------->Rs=2000")
            Price=2000
            name="Adidas Football"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==12):
            print("Cosco Football-------->Rs=2000")
            Price=2000
            name="Cosco Football"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==13):
            print("CR7 MecrualX Shoes-------->Rs=8000")
            Price=8000
            name="CR7 MecrualX Shoes"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==14):
            print("Messi 7x Shoes-------->Rs=7000")
            Price=1200
            name="Messi 7x Shoes"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==15):
            print("SG Shoes-------->Rs=2000")
            Price=2000
            name="SG Shoes"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==16):
            print("Yonex GR 303 Aluminium Badminton Racket-------->Rs=800")
            Price=800
            name="Yonex GR 303 Aluminium Badminton Racket"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==17):
            print("Feroc Aluminium Badminton Racket-------->Rs=500")
            Price=500
            name="Feroc Aluminium Badminton Racket"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==18):
            print("Aster Badminton Flash Shoes-------->Rs=800")
            Price=800
            name="Aster Badminton Flash Shoes"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        elif(c==19):
            print("Adidas Badminton Shoes-------->Rs=1000")
            Price=1000
            name="Adidas Badminton Shoes"
            Price_Array.append(Price)
            Name_Array.append(name)
            ask_next()
            break
        else:
            print("Please enter valid choice.")
                       
##############           
def main():
    print("\nYou can choose any Catagory you want")
    print("\n1. Sports\n\n2. Grocery and Household Supplies\n\n3. Beauty and Healthcare\n\n4. Bags & Luggages\n\n5. Books\n\n6. Entertainment\n\n7. Electronics\n\n")
    while(True):
        a=int(input("\nEnter your choice:"))
        if a==1:
            Sports(a)
            break
        elif a==2:
            GroceryHouseHoldSupplies(a)
            break
        elif a==3:
            BeautyHelthcare(a)
            break
        elif a==4:
            Bags(a)
            break
        elif a==5:
            Books(a)
            break
        elif a==6:
            Entertainment(a)
            break
        elif a==7:
            Electronics(a)
            break
        else:
            print("Plese enter valid category")
        
            
#sign up and login
print(" ---------------------------------")
print("|                                 |")
print("|   E-Commerce Management System  |")
print("|                                 |")
print(" ---------------------------------")
print(" ")
print(" __________________________")
print(" ")
print("| press '1' for Login      |")
print(" __________________________")
print(" ")
print("| press '2' for Sign Up    |")
print(" __________________________")
print(" ")
while(1):    
    choose=int(input("\nEnter your choice for login or sign up: "))
    if choose==1:
        print("\nNote:- Please enter valid email address \nYou will receive login id and password through that email only")
        email_send = input("\nEnter your email address: ")
        email_user = '<Enter sender email address>'
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,'<Enter sender email address password(Valid Google Password)>')
        message = 'Username=fcp_project   and   Password=CSE100'
        server.sendmail(email_user,email_send,message)
        server.quit()
        print("\nWe have send username and password to your email address. Please go and check it")
        while(True):
            
            log=input("\n\nEnter your username: ")
            logp=input("\n\nEnter your password: ")
            if log!='fcp_project':
                print("Invalid username")
            if logp!='CSE100':
                print("Invalid password")
            elif log=='fcp_project' and logp=='CSE100':
                
                break
        print("Login Successful")
        main()
        break
    elif choose==2:
        print(" ")  
        print("Please sign up before moving further")
        print(" ")
        email_send = input("Please enter your email address: ")
        sign=input("Create your username: ")
        password=input("Create your password: ")
        print(" ")
        print("Sign up successful, Now login with your username and password")
        print(" ")
        number = random.randint(1000,9999)
        x="Your Verification code is ",number
        email_user = '<Enter sender email address>'
        
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,'<Enter sender email address password(Valid Google Password)>')
        message = str(x)
        server.sendmail(email_user,email_send,message)
        server.quit()
        strnum=str(number)
        print("\nPlease check your email address you will get a Verification code")
        print(" ")
        while(1):
            VC=input("\nEnter your Verification code: ")
            if(VC==strnum):
                print(" ")
                
                while(True):
                    sign2=input("Enter your username: ")
                    pass2=input("Enter your password: ")
                    if sign2!=sign:
                        print("Invalid username")
                    if pass2!=password:
                        print("Invalid password")
                    elif sign2==sign and pass2==password:
                        break
                print("Login Successful")
                main()
                break
            else:
                print("Please enter valid OTP")
        break
    else:
        print("Invalid choice try again")
