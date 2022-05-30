/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */


//iteration
 var mergeTwoLists = function(l1, l2) {
    let list = new ListNode();
    let change = list;
    
    while (l1 !== null && l2 !== null) {
        if (l1.val < l2.val) {
            list.next = new ListNode(l1.val);
            l1 = l1.next;
        } else {
            list.next = new ListNode(l2.val);
            l2 = l2.next;
        }
        list = list.next;
    }
    
    list.next = l1 || l2;
    return change.next
};


//recursion
var mergeTwoLists = function(l1, l2) {
    if (!l1 || !l2) return (l1 ? l1 : l2);
    if (l1.val < l2.val) {
        l1.next = new mergeTwoLists(l1.next, l2);
        return l1;
    } else {
        l2.next = new mergeTwoLists(l2.next, l1);
        return l2;
    }
};