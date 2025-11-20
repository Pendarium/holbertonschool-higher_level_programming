#!/usr/bin/node

// Définir la fonction add qui additionne deux entiers
function add (a, b) {
  return a + b;
}

// Rendre la fonction visible depuis l'extérieur
module.exports.add = add;
