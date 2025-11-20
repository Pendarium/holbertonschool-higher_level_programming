#!/usr/bin/node

// Récupérer tous les arguments sauf les deux premiers (node et script)
const args = process.argv.slice(2);

// Convertir tous les arguments en nombres entiers
const numbers = args.map(Number);

// Si moins de 2 nombres, afficher 0
if (numbers.length < 2) {
  console.log(0);
} else {
  // Trier les nombres par ordre décroissant et supprimer les doublons
  const sorted = [...new Set(numbers)].sort((a, b) => b - a);
  // Si un seul nombre unique, afficher 0, sinon afficher le deuxième plus grand
  console.log(sorted.length > 1 ? sorted[1] : 0);
}
