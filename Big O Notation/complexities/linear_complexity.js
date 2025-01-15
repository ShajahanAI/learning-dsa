function linear_complexity(array){
    let x = 20392 * 23145;
    for (let i = 0; i < array.length; i++){
        console.log(i, array[i]);
    }
    console.log('Runs in linear time O(n)')
};

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
linear_complexity(array);