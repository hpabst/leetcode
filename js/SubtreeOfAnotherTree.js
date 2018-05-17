function TreeNode(val){
    this.val = val;
    this.left = this.right = null;
}

function equalSubtrees(n1, n2, tRoot){
    if(n1 == null && n2 == null){
        return true;
    }
    if(n1 == null || n2 == null){
        return false;
    }
    if(n1.val === n2.val && equalSubtrees(n1.left, n2.left, tRoot) && equalSubtrees(n1.right, n2.right, tRoot)){
        return true;
    }
    if(n2 !== tRoot){
        return false;
    }
    return equalSubtrees(n1.left, tRoot, tRoot) || equalSubtrees(n1.right, tRoot, tRoot);
}


var isSubtree = function(s, t) {
    return equalSubtrees(s, t, t);
};