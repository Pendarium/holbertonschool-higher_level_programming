#!/usr/bin/node

// On calcule le nombre d'arguments passés par l'utilisateur
// process.argv contient tous les arguments :
// [0] -> chemin vers node
// [1] -> chemin vers le script
// [2..n] -> arguments réels passés
const argsCount = process.argv.length - 2;

// On vérifie combien d'arguments ont été passés
if (argsCount === 0) {
  // Aucun argument passé
  console.log('No argument');
} else if (argsCount === 1) {
  // Un seul argument passé
  console.log('Argument found');
} else {
  // Deux arguments ou plus
  console.log('Arguments found');
}
