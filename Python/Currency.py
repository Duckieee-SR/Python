pesos = int(input("How many pesos do you have?: "))
soles = int(input("How many soles do you have?: "))
reais = int(input("How many reais do you have?: "))
euros = int(input("How many euros do you have?: "))

pesos_to_dollars = 0.059
soles_to_dollars = 0.27
reais_to_dollars = 0.2
euros_to_dollars = 1.09

dollars = (pesos * pesos_to_dollars) + (soles * soles_to_dollars) + (reais * reais_to_dollars) + (euros * euros_to_dollars)
print("You have $" + str(dollars) + " dollars.")


