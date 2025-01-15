function loglinear_complexity(n){
    // loglinear
    let y = n;
    let iterCount = 0;
    do {
        console.log(n);
        n = Math.floor(n / 2); // logarithmic
        for (let i = 0; i < y; i++){
            console.log(n, y); // linear
            iterCount ++
        }
    } while (n > 1);

    console.log('Ran for', iterCount, 'iterations');
    console.log('Runs in loglinear time O(n * log n)');
};

let n = 64;
loglinear_complexity(n);