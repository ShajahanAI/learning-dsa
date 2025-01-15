// Merge Sort has a complexity of O(n log n)

function merge(leftArr, rightArr){
    console.log(leftArr, rightArr);

    let leftIndex = 0;
    let rightIndex = 0;
    const result = [];

    while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
        if (leftArr[leftIndex] < rightArr[rightIndex]){
            result.push(leftArr[leftIndex]);
            leftIndex++;
        }
        else {
            result.push(rightArr[rightIndex])
            rightIndex++;
        }
    }

    return result.concat(leftArr.slice(leftIndex, leftArr.length)).concat(rightArr.slice(rightIndex, rightArr.length));
}

function mergeSort(arr) {
    if (arr.length < 2) {
        return arr
    }

    const midIndex = Math.floor(arr.length/2);
    const leftArr = arr.slice(0, midIndex);
    const rightArr = arr.slice(midIndex, arr.length);

    return merge(mergeSort(leftArr), mergeSort(rightArr))
}

const arr = [2, 5, 1, 3, 5];
const output = mergeSort(arr);
console.log(output);