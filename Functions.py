def percentage (marks) :
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1= [34, 45, 66, 77]
per1 = percentage(marks1)
marks2= [42, 41, 96, 27]
per2 = percentage(marks2)
marks3= [34, 45, 86, 97]
per3 = percentage(marks3)
marks4= [55, 35, 66, 77]
per4 = percentage(marks4)
print(per1)
print(per2)
print(per3)
print(per4)