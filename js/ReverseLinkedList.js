
function ListNode(val){
    this.val = val;
    this.next = null;
}

var reverseList = function(head){
    if(head === null || head.next === null){
        return head;
    } else {
        var prev = null;
        var curr = head;
        var next = curr.next;
        while(curr !== null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};