#!/usr/bin/env python3

from conllu import read_conllu


def get_features(sent):
    """
    Given a sentence as defined in conllu.py, return data suitable
    for training a classifier.
    """
    # 先把sentence放進list裡面，再push到stack裡
    # 創建features和parser actions的lists
    # create two empty lists to store the results (POStag & actions)
    features = []
    actions = []
    # stack starts with the Root token, buffer contains the rest of the sentence
    stack = [sent[0]]
    buffer = sent[1:]
    # set of processed token indices (based on position in sent)
    processed = set()

    # parsing step: while the buffer is not empty or the stack has more than one element, continue
    while buffer or len(stack) > 1:
        # get the top element of stack the first token in the buffer (if they exist)
        top = stack[-1] if stack else None
        next = buffer[0] if buffer else None

        # get POS tags for features
        topPOS = top.upos if top else "ROOT"
        nextPOS = next.upos if next else "ROOT"

        # get the indices of the top and next tokens in the original sentence
        top_index = sent.index(top) if top else 0  # index in original sent
        next_index = sent.index(next) if next else None

        # Left Arc: if the top token's head is the next token
        # the top token depends on the next token
        if top and next and top.head == next_index:
            features.append([topPOS, nextPOS])
            actions.append(f"left-arc({top.deprel})")  # record the Left-Arc action with dependency relation
            stack.pop()  # remove top from stack
            processed.add(top_index)  # mark the top token as processed


        # Right-Arc: if the next token's head is the top token and all children of the next token are processed
        # the next token depends on the top token
        elif top and next and next.head == top_index and all(
                child.head != next_index or sent.index(child) in processed for child in sent):
            features.append([topPOS, nextPOS])
            actions.append(f"right-arc({next.deprel})")  # record the Right-Arc action with dependency relation
            buffer.pop(0)  # remove next from buffer
            processed.add(next_index)  # mark the next token as processed


        # special case for root: Right Arc to ROOT
        # when the stack has exactly two tokens (ROOT and one other) and the top token's head is ROOT
        elif len(stack) == 2 and stack[-1].head == 0:
            features.append(["ROOT", stack[-1].upos])
            actions.append("right-arc(root)")
            stack.pop()  # Remove top from stack

        # Shift: if no arc can be formed, move the next token from the buffer to the stack
        else:
            features.append([topPOS, nextPOS])
            actions.append("shift")
            if not buffer:  # If buffer is empty, terminate the loop
                break
            stack.append(buffer.pop(0))  # Move next token to stack

    # return the feature and action data for training
    return features, actions

def is_projective(sent):
    """
    Return True if the sentence is projective, False otherwise.
    """
    n = len(sent) #Number of tokens in the sentence, including the root at index 0
    if n <= 1:  #If only the root is present, the sentence is definitely projective
        return True

    #Step 1: Build a list of children for each token
    children = [[] for _ in range(n)] #Initialize empty child lists for each token
    for i in range(1, n):  #Skip root at index 0
        head = sent[i].head #Get the head index of the current token
        if head != '_':  #Ensure the head is valid (should be an integer in CoNLL-U format)
            children[head].append(i) #Add current token as a child of its head

    #Step 2: Compute spans for each node and check projectivity
    spans = [None] * n   #Each index will store (leftmost, rightmost) positions of the subtree

    #Recursive function to compute spans and check projectivity.
    def compute_span(node):
        if spans[node] is not None: #If the span is already computed, return True
            return True

        #Initialize left and right boundaries to the current node's position
        left, right = node, node

        #Recursively compute spans for children
        for child in children[node]:
            if not compute_span(child): #If any child is non-projective, return False
                return False
            left = min(left, spans[child][0]) #Update left boundary
            right = max(right, spans[child][1]) #Update right boundary

        spans[node] = (left, right)  #Store the computed span

        #Step 3: Check projectivity: all positions in span must be dominated by node
        for pos in range(left, right + 1):
            curr = pos #Start from current position
            while curr != '_' and curr != node:  #until reaching the root
                if curr == node: #If reach the node, it's dominated correctly
                    break
                curr = sent[curr].head #Move to the parent node
            else:
                return False   #If we exit the loop without finding the node, it's non-projective
        return True  #If all checks pass, the node is projective

    #Start from root
    return compute_span(0)

if __name__ == "__main__":
    # The following shows the example usage
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument('conllu', help="CoNLL-U input file.")
    ap.add_argument('--output-file', '-o',
                    help="Output file to write training/test data for classification")
    args = ap.parse_args()
    if not args.output_file:
        args.output_file = args.conllu.replace('.conllu', '.tsv')

    with open(args.output_file, 'wt', encoding="utf8") as outfile:
        for i, sent in enumerate(read_conllu(args.conllu), start=1):
            if is_projective(sent):
                feats, cls = get_features(sent)
                for f, c in zip(feats, cls):
                    print("\t".join(f + [c]), file=outfile)
            else:
                print(f"Sentence {i} is non-projective skipping.")
