#!/usr/bin/node

// Récupérer le premier argument
const arg = process.argv[2];

// Convertir en entier
const number = parseInt(arg);

// Vérifier si c'est un nombre et afficher le résultat
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
