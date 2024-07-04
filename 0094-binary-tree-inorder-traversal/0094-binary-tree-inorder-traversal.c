/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

typedef struct TreeNode tree;
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize = 0;
    int * res = (int *)malloc(sizeof(int)*100);
    
    void sol(tree* root, int*res, int *index){
        if(root!=NULL){
        sol(root->left, res, index);
        res[*index] = root->val;
        (*index) +=1;
        sol(root->right, res, index);
        }
    }
    
    sol(root, res, returnSize);
    return res;
}