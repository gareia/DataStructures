/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {
	if(head == null)
		head = new SinglyLinkedListNode(data);
	else if(head.next == null)
		head.next = new SinglyLinkedListNode(data);
	else
		insertNodeAtTail(head.next, data);
	return head;

}

//MAIN
//INPUT
//n [1-1000]
//list[i] [1-1000]
//Call insertNodeAtTail


/*SAMPLE

Input
5
141
302
164
530
474

Output
141
302
164
530
474

*/