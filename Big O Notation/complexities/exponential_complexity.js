function exponential_complexity(n){
    if (n == 0) {
        return 0;
    }

    if (n == 1) {
        return 1;
    }
    
    console.log('Runs in exponential time O(2 ^ n)')

    return exponential_complexity(n - 1) + exponential_complexity(n - 2);
};

let output = exponential_complexity(4);
console.log(output);

// 1, 1, 2, 3, 5, 8, 13, 21