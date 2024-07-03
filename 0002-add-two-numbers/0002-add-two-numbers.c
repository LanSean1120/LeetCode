/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
typedef struct ListNode ListNode;
ListNode * genListNode(int val, ListNode * next){
    ListNode *node = (ListNode *)malloc(sizeof(ListNode));
    node->val = val;
    node->next = next;
    return node;
}
ListNode * re_genListNode(int val, ListNode * current){
    ListNode * last = genListNode(val, NULL);
    ListNode*ptr = current;
    if(current == NULL) return last;
    while(ptr!=NULL){
        if(ptr->next==NULL){
            ptr->next = last;
            break;
        }
        ptr = ptr->next;
    }
    return current;
}
ListNode* reverseList(ListNode* head) {
    ListNode* prev = NULL;
    ListNode* curr = head;
    ListNode* next = NULL;

    while (curr != NULL) {
        // Store the next node
        next = curr->next;

        // Reverse the current node's pointer
        curr->next = prev;

        // Move pointers one position ahead
        prev = curr;
        curr = next;
    }

    // Update the head to the new first node
    head = prev;
    return head;
}

struct ListNode * addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    ListNode *ans;
    ListNode * previous = NULL;
    while(l1!=NULL && l2!=NULL){
        if(l1->val + l2->val <=9){
            ans = re_genListNode(l1->val + l2->val, previous);
            previous = ans;
        }else{
            ans = re_genListNode((l1->val + l2->val)%10, previous);
            previous = ans;
            if(l1->next!=NULL) l1->next->val+=1;
            if(l1->next==NULL){
                ListNode*temp = NULL;
                l1->next = genListNode(1, temp);
            }
        }
        

        if(l1->next != NULL && l2->next == NULL){
            ListNode * temp = NULL;
            l2->next = genListNode(0, temp);
        }
        if(l2->next != NULL && l1->next == NULL){
            ListNode * temp = NULL;
            l1->next = genListNode(0, temp);
        }
        l1 = l1->next;
        l2 = l2->next;
    }
    return ans;
}