'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function main() {
    const N = parseInt(readLine().trim(), 10);

    // 1. If N is odd, print Weird
    if (N % 2 !== 0) {
        console.log("Weird");
    } 
    // If it's not odd, it's even. Check the ranges:
    else {
        // 2. If N is even and in the inclusive range of 2 to 5
        if (N >= 2 && N <= 5) {
            console.log("Not Weird");
        } 
        // 3. If N is even and in the inclusive range of 6 to 20
        else if (N >= 6 && N <= 20) {
            console.log("Weird");
        } 
        // 4. If N is even and greater than 20
        else if (N > 20) {
            console.log("Not Weird");
        }
    }
}