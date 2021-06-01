#!/bin/python3

import sys

def main(args):
    nodes = int(args[1]) # number of nodes
    conns = int(args[2]) # number of connections
    perce = float(args[3]) # hidden information percentage
    es_co = [int(x) for x in args[4::2]]
    es_tp = [int(x) for x in args[5::2]]
    estim = zip(es_co, es_tp) # estimate values

    total_conns = nodes * (nodes - 1) / 2
    negatives = total_conns - conns
    given_conns = int(conns * (1 - perce))
    accuracy = []
    precision = []
    recall = []
    f1 = []
    cnt = 0

    for ec, tp in estim:
        fn = conns - tp
        fp = ec - tp
        tn = total_conns - fp
        accuracy.append((tp+tn)/(tp+fp+fn+tn))
        precision.append((tp)/(tp+fp))
        recall.append((tp)/(tp+fn))
        f1.append(2*(recall[cnt]*precision[cnt])/(recall[cnt]+precision[cnt]))

        print("\n========== " + str(cnt) + " ==========")
        print("Estimate connections: " + str(ec))
        print("True positive: " + str(tp))
        print("False negative: " + str(fn))
        print("False positive: " + str(fp))
        print("True negative: " + str(tn))
        print("Accuracy: " + str(accuracy[cnt]))
        print("precision: " + str(precision[cnt]))
        print("Recall: " + str(recall[cnt]))
        print("F1 score: " + str(f1[cnt]))

        cnt = cnt + 1
    
    print("\n======== EVEN =========")
    print("Accuracy: " + str(sum(accuracy)/len(accuracy)))
    print("Precision: " + str(sum(precision)/len(precision)))
    print("Recall: " + str(sum(recall)/len(recall)))
    print("F1 score: " + str(sum(f1)/len(f1)))

    print("\n======== BEST =========")
    print("Accuracy: " + str(max(accuracy)))
    print("Precision: " + str(max(precision)))
    print("Recall: " + str(max(recall)))
    print("F1 score: " + str(max(f1)))

    print("\n======== WORST ========")
    print("Accuracy: " + str(min(accuracy)))
    print("Precision: " + str(min(precision)))
    print("Recall: " + str(min(recall)))
    print("F1 score: " + str(min(f1)))

if __name__ == "__main__":
    main(sys.argv)