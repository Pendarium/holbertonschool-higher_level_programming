#!/usr/bin/node

// Récupérer le premier argument utilisateur
const firstArg = process.argv[2];

// Vérifier s'il existe
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
