from firebase import firebase
firebase = firebase.FirebaseApplication('https://prototypedb-4dc8a.firebaseio.com/', None)


items = ["Meat", "Veggies", "Eggs", "Bakery"]
result = firebase.put('','/Coles/',items)
result2 = firebase.put('','/Woolworths/',items)
result3 = firebase.put('','/Aldi/',items)

print("Done")