function factorial_complexity(n){
    if (n === 0) {
        console.log('Runs in Factorial Time');
        return
    }

    for (let i = 0; i < n; i++){
        factorial_complexity(n - 1)
    }
};

factorial_complexity(5);