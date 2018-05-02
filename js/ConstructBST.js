
function TreeNode(val){
    this.val = val;
    this.left = this.right = null;
}

var buildTree = function(preorder, inorder){
    return recursiveBuildTree(preorder, inorder, 0, inorder.length-1);
};

var recursiveBuildTree = function(preorder, inorder, startIdx, endIdx){
    if(startIdx === endIdx){
        return new TreeNode(preorder.shift());
    } else if (startIdx > endIdx){
        return null;
    } else {
        let ret = new TreeNode(preorder.shift());
        let index = inorder.indexOf(ret.val);
        ret.left = recursiveBuildTree(preorder, inorder, startIdx, index-1);
        ret.right = recursiveBuildTree(preorder, inorder, index+1, endIdx);
        return ret;
    }
};