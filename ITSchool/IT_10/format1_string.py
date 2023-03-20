user_info = {
    "first_name": "Mihai",
    "last_name": "Dinu",
    "address": "Bucharest",
    "country": "Ro"
}

#print("Nume: {} Prenume: {} Country: {} ".format(
#    user_info("last_name") , user_info("first_name"), user_info("country")
#))

auto = {
    "marca" : "Audi",
    "model" : "A4",
    "usi" : 4
}

USER_TEMPLATE = "Nume: {} Prenume: {} Country: {}"

print(USER_TEMPLATE.format(
        user_info["last_name"], user_info["first_name"], user_info["country"]
))

#Detin o masina marca Audi,model A4 si are 4 usi.

car_template = "Detin o masina marca {},model {} si are {} usi."
print(car_template.format(
    auto["marca"], auto["model"] , auto["usi"]
 ))