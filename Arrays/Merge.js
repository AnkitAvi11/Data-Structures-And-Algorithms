
function merge(arr1, arr2) {
    
    let i=0, j=0;

    while (i<arr1.length) {
        if (arr1[i] > arr2[j]) {
            let temp = arr1[i];
            arr1[i] = arr2[j];
            arr2[j] = temp;
            arr2.sort((a,b)=>a-b);
        }
        i+=1;
    }

    arr2.forEach(el => {
        arr1.push(el);
    })

}

arr = [1,3,5,7,9]
arr2 = [2,4,6,8,10]

merge(arr, arr2)

console.log(arr)