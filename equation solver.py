            ########################################
      ####################################################
################################################################
########## Equation solver developed by Shubham Gupta ##########
################################################################
      ####################################################
            ########################################


#printing the details of program

print "Hi there, this is Shubham Gupta with his awesome program : The equation solver\n"
print "This program solves 2 linear equations in x & y\n"
print "Have fun checking this program out, and I hope that this helps in your mathematics to quickly solve 2 equations....\n\n"

#taking input of equations

eq = raw_input("Enter equation 1 : ")
eq2 = raw_input("Enter equation 2 : ")
print

#checking if they are solvable equations or not

check = False
if len(eq.split("=")) == 2:         #LHS and RHS both are only present
      if len(eq2.split("=")) == 2:  #LHS and RHS both are only present
            check = True
      else:
            print "Sorry, but expression 2 is not an equation...."
else:
      print "Sorry, but expression 1 is not an equation...."

if check:
      #removing spaces in middle
      
      words = eq.split()
      eq = ''
      for i in words:
            eq += i
      words = eq2.split()
      eq2 = ''
      for i in words:
            eq2 += i
      
      #starting of equation 1
      
      terms = eq.split("+")
      signs = ["+", "+", "+"]             #assume sign +ve if not mentioned (like for first term)
      c1 = [0, 0, 0]                      #the list containing coefficients in order [x, y, constant (on RHS)]
      #put sign of negative and thus, change terms too
      for i in range(len(terms)):
            if "-" in terms[i]:
                  splitted = terms[i].split("-")
                  if splitted[0] == "":
                        i -= 1
                  terms[i] = splitted[0]
                  for j in range(len(splitted)-1):    #neccessary as if more than 1 negative terms
                        terms.insert(i+j+1, splitted[j+1])
                        if splitted[j+1][0] == "x":
                              signs[0] = "-"
                        elif splitted[j+1][0] == "y":
                              signs[1] = "-"
                        else:
                              signs[2] = "-"
      #just removing 1 error that takes place
      if terms[-1] == "":
            terms = terms[:-1]
      #the constant
      for i in range(len(terms)):
            if "=" in terms[i]:
                  splitted = terms[i].split("=")
                  terms[i] = splitted[0]
                  if splitted[1] != "0" and splitted[1] != "":
                        terms.insert(i+1, splitted[1])
                  equal = i
      #seperating coefficients of x & y & the constant term
      for i in range(len(terms)):
            if "x" in terms[i]:
                  num = terms[i].split("x")[0]
                  if num == '':                 #if no coefficient specified, assign coefficient as 1
                        if i<=equal:            #if x on RHS, it's sign will be -ve
                              c1[0] += eval(signs[0]+str(1.0))
                        else:
                              c1[0] -= eval(signs[0]+str(1.0))
                  else:
                        if i<=equal:            #if x on RHS, it's sign will be -ve
                              c1[0] += eval(signs[0]+str(float(num)))
                        else:
                              c1[0] -= eval(signs[0]+str(float(num)))
            elif "y" in terms[i]:
                  num = terms[i].split("y")[0]
                  if num == '':                 #if no coefficient specified, assign coefficient as 1
                        if i<=equal:            #if y on RHS, it's sign will be -ve
                              c1[1] += eval(signs[1]+str(1.0))
                        else:
                              c1[1] -= eval(signs[1]+str(1.0))
                  else:
                        if i<=equal:            #if y on RHS, it's sign will be -ve
                              c1[1] += eval(signs[1]+str(float(num)))
                        else:
                              c1[1] -= eval(signs[1]+str(float(num)))
            else:
                  if i<=equal:            #if constant on RHS, it's sign will be -ve
                        c1[2] -= eval(signs[2]+str(float(terms[i])))
                  else:
                        c1[2] += eval(signs[2]+str(float(terms[i])))
      
      #starting of equation 2
      
      terms = eq2.split("+")
      signs = ["+", "+", "+"]             #assume sign +ve if not mentioned (like for first term)
      c2 = [0, 0, 0]                      #the list containing coefficients in order [x, y, constant (on RHS)]
      #put sign of negative and thus, change terms too
      for i in range(len(terms)):
            if "-" in terms[i]:
                  splitted = terms[i].split("-")
                  if splitted[0] == "":
                        i -= 1
                  terms[i] = splitted[0]
                  for j in range(len(splitted)-1):    #neccessary as if more than 1 negative terms
                        terms.insert(i+j+1, splitted[j+1])
                        if splitted[j+1][0] == "x":
                              signs[0] = "-"
                        elif splitted[j+1][0] == "y":
                              signs[1] = "-"
                        else:
                              signs[2] = "-"
      #just removing 1 error that takes place
      if terms[-1] == "":
            terms = terms[:-1]
      #the constant
      for i in range(len(terms)):
            if "=" in terms[i]:
                  splitted = terms[i].split("=")
                  terms[i] = splitted[0]
                  if splitted[1] != "0" and splitted[1] != "":
                        terms.insert(i+1, splitted[1])
                  equal = i
      #seperating coefficients of x & y & the constant term
      for i in range(len(terms)):
            if "x" in terms[i]:
                  num = terms[i].split("x")[0]
                  if num == '':                 #if no coefficient specified, assign coefficient as 1
                        if i<=equal:            #if x on RHS, it's sign will be -ve
                              c2[0] += eval(signs[0]+str(1.0))
                        else:
                              c2[0] -= eval(signs[0]+str(1.0))
                  else:
                        if i<=equal:            #if x on RHS, it's sign will be -ve
                              c2[0] += eval(signs[0]+str(float(num)))
                        else:
                              c2[0] -= eval(signs[0]+str(float(num)))
            elif "y" in terms[i]:
                  num = terms[i].split("y")[0]
                  if num == '':                 #if no coefficient specified, assign coefficient as 1
                        if i<=equal:            #if y on RHS, it's sign will be -ve
                              c2[1] += eval(signs[1]+str(1.0))
                        else:
                              c2[1] -= eval(signs[1]+str(1.0))
                  else:
                        if i<=equal:            #if y on RHS, it's sign will be -ve
                              c2[1] += eval(signs[1]+str(float(num)))
                        else:
                              c2[1] -= eval(signs[1]+str(float(num)))
            else:
                  if i<=equal:            #if constant on RHS, it's sign will be -ve
                        c2[2] -= eval(signs[2]+str(float(terms[i])))
                  else:
                        c2[2] += eval(signs[2]+str(float(terms[i])))

      
      #solving the equations by elimination method

      #if any equation doesn't have y, assign value of x
      y_e = True
      if c1[1] == 0:
            x = c1[2]/c1[0]
            y_e = False
      if c2[1] == 0:
            x = c2[2]/c2[0]
            y_e = False
      #eliminating x
      x2 = c1[0]
      for i in range(len(c1)):
            c1[i] *= c2[0]
      for i in range(len(c2)):
            c2[i] *= x2
      #assigning values
      if c2[1]-c1[1] == 0:                #ratio of coefficients of x and y same
            if c2[2]-c1[2] == 0:          #ratio of constants same as ratio of x and y
                  print "There is no unique solution of these equations. For every real value of x, you will get some value of y...."
            else:
                  print "Sorry, no solution exists of these equations...."
      else:
            y = (c2[2]-c1[2])/(c2[1]-c1[1])
            if y_e:                       #if equations have value of y, calculate x
                  x = (c1[2]-c1[1]*y)/c1[0]
            #printing x & y
            print "Equations solved successfully!!!"
            print "x =", x, " & y =", y
      
#exit

print
raw_input("Press enter to exit")


            ##################################
      ##############################################
##########################################################
####### ------------------THE END------------------ #######
################################################################
      ##############################################
            ##################################
