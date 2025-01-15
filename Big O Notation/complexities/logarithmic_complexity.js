function logarithmic_complexity(n){
    let x = 20392 * 23145;
    do {
        console.log(n);
        n = Math.floor(n / 2);
    } while (n > 1);
    console.log('Runs in logarithmic time O(log n)');
};

let n = 64;
logarithmic_complexity(n);