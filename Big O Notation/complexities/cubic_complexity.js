function cubic_complexity(array){
    let x = 20392 * 23145;
    for (let i = 0; i < array.length; i++){
        for (let j = 0; j < array.length; j++){
            for (let k = 0; k < array.length; k++){
                console.log(i, j, array[k]);
            }
        }
    }
    console.log('Runs in cubic time O(n^3)')
};

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
cubic_complexity(array);