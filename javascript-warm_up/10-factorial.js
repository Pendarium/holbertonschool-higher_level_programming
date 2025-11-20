#!/usr/bin/node

function factorial (n) {
  // Si n n'est pas un nombre ou est inférieur ou égal à 0, retourner 1
  if (isNaN(n) || n <= 0) {
    return 1;
  }
  // Sinon, retourner n multiplié par la factorielle de (n-1)
  return n * factorial(n - 1);
}

// Récupérer le premier argument de la ligne de commande et le convertir en entier
const num = parseInt(process.argv[2]);

// Afficher le résultat de la factorielle
console.log(factorial(num));
