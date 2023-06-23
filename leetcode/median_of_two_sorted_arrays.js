/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
// // Two Pointer - O(m + n)
// var findMedianSortedArrays = function (nums1, nums2) {
//   let nums1Ptr = 0;
//   let nums2Ptr = 0;
//   let nums1Len = nums1.length;
//   let nums2Len = nums2.length;
//   let mergedArr = [];

//   while (nums1Ptr < nums1Len && nums2Ptr < nums2Len) {
//     if (nums1[nums1Ptr] >= nums2[nums2Ptr]) {
//       mergedArr.push(nums2[nums2Ptr++]);
//     } else {
//       mergedArr.push(nums1[nums1Ptr++]);
//     }
//   }

//   mergedArr = [
//     ...mergedArr,
//     ...nums1.slice(nums1Ptr),
//     ...nums2.slice(nums2Ptr),
//   ];

//   let mergedArrLen = mergedArr.length;
//   let median = 0;

//   if (mergedArrLen % 2) {
//     median = mergedArr[Math.floor(mergedArrLen / 2)];
//   } else {
//     let medianIdx = mergedArrLen / 2;
//     median = (mergedArr[medianIdx - 1] + mergedArr[medianIdx]) / 2;
//   }

//   return median;
// };

// Binary Search - O(log(min(n , m)))
var findMedianSortedArrays = function (nums1, nums2) {
    let n1Len = nums1.length;
    let n2Len = nums2.length;

    if (n1Len > n2Len) return findMedianSortedArrays(nums2, nums1);

    let start = 0;
    let end = n1Len;

    while (start <= end) {
        let partitionN1 = Math.floor(start + end);
        let partitionN2 = Math.floor((n1Len + n2Len + 1) / 2) - partitionN1;

        let maxLeftN1 = partitionN1 == 0 ? Number.NEGATIVE_INFINITY : nums1[partitionN1 - 1];
        let minRightN1 = partitionN1 == n1Len ? Number.POSITIVE_INFINITY : nums1[partitionN1];
        // m = n 경우
        let maxLeftN2 = partitionN2 == 0 ? Number.NEGATIVE_INFINITY : nums2[partitionN2 - 1];
        let minRightN2 = partitionN2 == n2Len ? Number.POSITIVE_INFINITY : nums2[partitionN2];

        if (maxLeftN1 <= minRightN2 && maxLeftN2 <= minRightN1) {
            if ((n1Len + n2Len) % 2 == 0) {
                return (Math.max(maxLeftN1, maxLeftN2) + Math.min(minRightN1, minRightN2)) / 2
            }
            else {
                return Math.max(maxLeftN1, maxLeftN2);
            }
        }
        else if (maxLeftN1 > minRightN2) {
            end = partitionN1 - 1;
        }
        else {
            start = partitionN1 + 1;
        }
    }
};

const num1 = [1, 2];
const num2 = [3, 4];

console.log(findMedianSortedArrays(num1, num2));
