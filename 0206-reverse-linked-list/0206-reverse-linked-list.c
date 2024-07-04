/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode listnode;
listnode* genlistnode(int val, listnode * nex){
    listnode* node = (listnode*)malloc(sizeof(listnode));
    node->val = val;
    node->next = nex;
    return node;
}

struct ListNode* reverseList(struct ListNode* head) {
    listnode * ans=NULL;
    while(head!=NULL){
        ans = genlistnode(head->val, ans);
        head = head->next;
    }
    return ans;
}