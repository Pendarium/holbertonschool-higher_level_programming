#!/usr/bin/node

// Tableau des lignes
const languages = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

// Construire un tableau temporaire pour ajouter les retours à la ligne
const output = [];
for (let i = 0; i < languages.length; i++) {
  output.push(languages[i]); // ajouter chaque ligne
}

// Afficher tout avec une seule console.log
console.log(output.join('\n'));
