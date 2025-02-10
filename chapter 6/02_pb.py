marks1=int(input("enter marks of enlish:-"))
marks2=int(input("enter marks of math:-"))
marks3=int(input("enter marks of science:-"))
total_p= 100*(marks1+marks2+marks3)/300

if(total_p>40):
    print("you are pass congratulation")
else:
    print("you fail close but no cigar")