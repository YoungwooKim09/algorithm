/**
 * @param {string} s
 * @return {number}
 */
// var lengthOfLongestSubstring = function(s) {
//     let maxLen = 0;
//     let strLen = s.length;
//     let front = 0;
//     let rear = 0;

//     let substring = new Set();

//     while (front < strLen && rear < strLen) {
//         if (!isExist(substring, s[front])) {
//             substring.add(s[front]);
//             front++;
//         }
//         else {
//             maxLen = Math.max(front - rear, maxLen);
//             substring.delete(s[rear]);
//             rear++;
//         }
//     }
//     maxLen = Math.max(front - rear, maxLen);

//     return maxLen;
// };

// function isExist(set, s) {
//     if (set.has(s)) return true;

//     return false;
// }

// var lengthOfLongestSubstring = function(s) {
//     let maxLen = 0;
//     let left = 0;
//     let substring = new Set();

//     for (let i = 0; i < s.length; i++) {

//         while(substring.has(s[i])) {
//             substring.delete(s[left]);
//             left++;
//         }

//         substring.add(s[i]);
//         maxLen = Math.max(maxLen, i - left + 1);
//     }

//     return maxLen;
// };

// var lengthOfLongestSubstring = function(s) {
//     let maxLen = 0;
//     let left = 0;
//     let lastIndex = new Map();

//     for (let i = 0; i < s.length; i++) {
//         left = lastIndex.get(s[i]) >= left ? lastIndex.get(s[i]) + 1 : left;
//         lastIndex.set(s[i], i);
//         maxLen = Math.max(maxLen, i - left + 1);
//     }

//     return maxLen;
// };

var lengthOfLongestSubstring = function (s) {
  let left = 0;
  const lastIndex = {};

  return s.split("").reduce((maxLen, val, idx) => {
    left = lastIndex[val] >= left ? lastIndex[val] + 1 : left;
    lastIndex[val] = idx;
    return Math.max(maxLen, idx - left + 1);
  }, 0);
};
