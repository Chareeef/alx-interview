#!/usr/bin/node
/* Script that prints all characters names of a Star Wars movie
 * using the 'https://swapi-api.alx-tools.com/api' API
 */

// Import request module
const request = require('request');

// The main API URL
const mainURL = 'https://swapi-api.alx-tools.com/api';

// Get the characters' URLs list for this movie
function fetchCharacters (movieID) {
  // Return a promise that will resolve a characters' URLs list
  return new Promise((resolve, reject) => {
    request.get(mainURL + '/films/' + movieID, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        try {
          const movie = JSON.parse(body);
          resolve(movie.characters);
        } catch (parseError) {
          reject(parseError);
        }
      }
    });
  });
}

// Log characters names in the same order as in '/films/<movieID>' endpoint
function displayCharactersNames (charactersURLs) {
  // List of promises of each character URL request
  const charactersPromises = [];

  for (const url of charactersURLs) {
    // Create a promise of a request for each character name
    const promise = new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          try {
            const character = JSON.parse(body);

            // Resolve character's name
            resolve(character.name);
          } catch (parseError) {
            resolve(parseError);
          }
        }
      });
    });

    // Push this promise to our promises array
    charactersPromises.push(promise);
  }

  // Resolve all promises and print, in order,
  // each one's resolved character's name
  Promise.all(charactersPromises).then((charactersNames) => {
    for (const name of charactersNames) {
      console.log(name);
    }
  });
}

// Get the Movie ID
const movieID = process.argv[2];

// Abracadabra !!
fetchCharacters(movieID)
  .then((charactersURLs) => displayCharactersNames(charactersURLs))
  .catch((error) => console.log(error));
