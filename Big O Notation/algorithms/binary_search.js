// Binary search has a complexity of O(log n)

let arr = [1, 2, 3, 4, 5, 6, 7, 8];
let start = 0;
let end = arr.length - 1;
let target = 8;

function binarySearch(arr, start, end, target) {
    let midIndex = Math.floor((start + end) / 2);
    
    if (start > end) {
        console.log(target, 'Not In Array');
        return false
    }
    
    if (arr[midIndex] == target) {
        console.log('Found Target', target, 'At Index', midIndex);
        return true
    }
    else if (arr[midIndex] < target) {
        return binarySearch(arr, midIndex + 1, end, target)
    }
    else {
        return binarySearch(arr, start, midIndex - 1, target)
    }
}

binarySearch(arr, start, end, target);