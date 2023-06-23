// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  return iter(l1, l2, 0);
};

function iter(l1, l2, rest) {
  if (!l1 && !l2 && !rest) return null;

  let sum = (l1?.val || 0) + (l2?.val || 0) + rest;
  carry = Math.floor(sum / 10);

  return new ListNode(sum % 10, iter(l1?.next, l2?.next, carry));
}

// var addTwoNumbers = function(l1, l2) {
//     let result = new ListNode();
//     let current = result;

//     let sum = 0;
//     let carry = 0;

//     while (l1 !== null || l2 !== null || sum > 0) {

//         if (l1) {
//             sum += l1.val;
//             l1 = l1.next;
//         }

//         if (l2) {
//             sum += l2.val;
//             l2 = l2.next;
//         }

//         if (sum >= 10) {
//             carry = 1;
//             sum -= 10;
//         }

//         current.next = new ListNode(sum);
//         current = current.next;

//         sum = carry;
//         carry = 0;
//     }

//     return result.next;

// };

let l1 = new ListNode(2);
l1.next = new ListNode(4);
l1.next.next = new ListNode(3);

let l2 = new ListNode(5);
l2.next = new ListNode(6);
l2.next.next = new ListNode(4);

console.log(addTwoNumbers(l1, l2));
