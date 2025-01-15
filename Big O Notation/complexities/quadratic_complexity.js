function quadratic_complexity(array){
    let x = 20392 * 23145;
    for (let i = 0; i < array.length; i++){
        for (let j = 0; j < array.length; j++){
            console.log(i, j, array[j]);
        }
    }
    console.log('Runs in quadratic time O(n^2)')
};

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
quadratic_complexity(array);