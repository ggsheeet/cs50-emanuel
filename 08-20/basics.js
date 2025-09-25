//  Primitives
const constante = "Hello" // Constant
var variable = "Hey" // Variable type var
let variableTipoLet = "Hi" // Variable type let
const inClass = true // boolean

// Non-Primitives
const stats = [5, 6, 8, 10] // Array
const students = {"abner": 25, "titi": 26, "anahí": 29} // Object
const scoresByGroups = [[0, 50, 100], [10, 40, 60], [20, 60, 70]]
const menuCategoriesAndItems = {  // Nested Object
  "entradas": 
  {
    "nombre": "alitas", 
    "precio": 100, 
    "aderezos": ["blue cheese", "ranch"]
  }
}

// Function definition
function printMessage(message) { 
  console.log(message)
}
// Function call
printMessage("Hello Students!")

values = [1, 2, 3]

//  iterate: operar/leer un listado (uno por uno)
for (let i = 0; i < values.length; i++) {
  print(values[i])
}