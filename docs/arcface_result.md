# Backbone: MobilenetV2
## Test on fixed LFW

![AUC](/photo/Figure_1.png)

![EU Distance](/photo/eu_dis.png)

## Result

| Threshold | TRP | FPR | Top-left | Acc |
| :---: | --- | --- | --- | --- |
| 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.5000 |
| 0.1000 | 0.0003 | 0.0000 | 0.9997 | 0.5002 |
| 0.2000 | 0.0087 | 0.0000 | 0.9913 | 0.5043 |
| 0.3000 | 0.1440 | 0.0000 | 0.8560 | 0.5720 |
| 0.4000 | 0.5943 | 0.0000 | 0.4057 | 0.7972 |
| 0.5000 | 0.9273 | 0.0017 | 0.0727 | 0.9628 |
| 0.6000 | 0.9963 | 0.0770 | 0.0771 | 0.9597 |
| 0.7000 | 1.0000 | 0.5727 | 0.5727 | 0.7137 |
| 0.8000 | 1.0000 | 0.9807 | 0.9807 | 0.5097 |
| 0.9000 | 1.0000 | 1.0000 | 1.0000 | 0.5000 |

## Confusion matrix: threshold (0.0 > 1.0)
| Theshold | Confusion | >matrix |
| :---: | :---: |:---: |
| 0.1 | 3000 | 0 |
| | 3000 | 0 |
| | |
| 0.2 | 3000 | 0 |
| | 2999 | 1 |
| | |
| 0.3 | 3000 | 0 |
| | 2974 | 26|
| | |
| 0.4 | 3000 | 0 |
| | 2568 | 432 |
| | |
| 0.5 | 3000 | 0 |
| | 1217 | 1783 |
| | |
| 0.6 | 2995 | 5 |
| | 218 | 2782 |
| | |
| 0.7 | 2769 | 231 |
| | 11 | 2989 |
| | |
| 0.8 | 1282 | 1718 |
| | 0 | 3000 |
| | |
| 0.9 | 58 | 2942 |
| | 0 | 3000 | 
| | |
| 1.0 | 3000 | 0 |
| | 3000 | 0 |


## Test on ICPR range(30-60) without distortion

![AUC](/photo/ICPR60_ROC.png)

![EU Distance](/photo/ICPR60_eu_dis.png)

## Result

| Threshold | TRP | FPR | Top-left | Acc |
| :---: | --- | --- | --- | --- |
| 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.5000
| 0.1000 | 0.0000 | 0.0000 | 1.0000 | 0.5000
| 0.2000 | 0.0043 | 0.0000 | 0.9957 | 0.5021
| 0.3000 | 0.0600 | 0.0000 | 0.9400 | 0.5300
| 0.4000 | 0.2300 | 0.0029 | 0.7700 | 0.6136
| 0.5000 | 0.6143 | 0.0286 | 0.3868 | 0.7929
| 0.6000 | 0.9329 | 0.2386 | 0.2478 | 0.8471
| 0.7000 | 0.9914 | 0.8471 | 0.8472 | 0.5721
| 0.8000 | 1.0000 | 0.9957 | 0.9957 | 0.5021
| 0.9000 | 1.0000 | 1.0000 | 1.0000 | 0.5000



## Confusion matrix: threshold (0.0 > 1.0)
| Theshold | Confusion | >matrix |
| :---: | :---: |:---: |
| 0.1 | 700 | 0 |
| | 700 | 0 |
| | |
| 0.2 | 700 | 0 |
| | 700 | 0 |
| | |
| 0.3 | 700 | 0 |
| | 697 | 3 |
| | |
| 0.4 | 700 | 0 |
| | 658 | 42 |
| | |
| 0.5 | 698 | 2 |
| | 539 | 161 |
| | |
| 0.6 | 680 | 20 |
| | 270 | 430 |
| | |
| 0.7 | 533 | 167 |
| | 40 | 653 |
| | |
| 0.8 | 107 | 593 |
| | 6 | 694 |
| | |
| 0.9 | 3 | 697 |
| | 0 | 700 | 
| | |
| 1.0 | 0 | 700 |
| | 0 | 700 | 

## Test on ICPR range(30) without distortion

![AUC](/photo/ICPR30_ROC.png)

![EU Distance](/photo/ICPR30_eu_dis.png)

## Result

| Threshold | TRP | FPR | Top-left | Acc |
| :---: | --- | --- | --- | --- |
| 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.3333
| 0.1000 | 0.0007 | 0.0000 | 0.9993 | 0.3338
| 0.2000 | 0.0414 | 0.0000 | 0.9586 | 0.3610
| 0.3000 | 0.3514 | 0.0000 | 0.6486 | 0.5676
| 0.4000 | 0.7771 | 0.0000 | 0.2229 | 0.8514
| 0.5000 | 0.9750 | 0.0000 | 0.0250 | 0.9833
| 0.6000 | 1.0000 | 0.1029 | 0.1029 | 0.9657
| 0.7000 | 1.0000 | 0.6057 | 0.6057 | 0.7981
| 0.8000 | 1.0000 | 0.9886 | 0.9886 | 0.6705
| 0.9000 | 1.0000 | 1.0000 | 1.0000 | 0.6667


## Confusion matrix: threshold (0.0 > 1.0)
| Theshold | Confusion | >matrix |
| :---: | :---: |:---: |
| 0.1 | 700 | 0 |
| | 1400 | 0 |
| | |
| 0.2 | 700 | 0 |
| | 1399 | 1 |
| | |
| 0.3 | 700 | 0 |
| | 1342 | 58|
| | |
| 0.4 | 700 | 0 |
| | 908 | 492 |
| | |
| 0.5 | 700 | 0 |
| | 312 | 1088 |
| | |
| 0.6 | 700 | 0 |
| | 35 | 1365 |
| | |
| 0.7 | 628 | 72 |
| | 0 | 1400 |
| | |
| 0.8 | 276 | 424 |
| | 0 | 1400 |
| | |
| 0.9 | 8 | 692 |
| | 0 | 1400 | 
| | |
| 1.0 | 0 | 7 |
| | 0 | 1400 | 

# Test on ICPR range(30-60) with distortion
## Gaussian [.1, .5. 1, 2, 5]
lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0114 fpr 0.0000 top left 0.9886 acc 0.5057
thr 0.3000 tpr 0.0714 fpr 0.0000 top left 0.9286 acc 0.5357
thr 0.4000 tpr 0.2614 fpr 0.0000 top left 0.7386 acc 0.6307
thr 0.5000 tpr 0.6414 fpr 0.0243 top left 0.3594 acc 0.8086
thr 0.6000 tpr 0.9429 fpr 0.2614 top left 0.2676 acc 0.8407
thr 0.7000 tpr 1.0000 fpr 0.8429 top left 0.8429 acc 0.5786
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```

lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0100 fpr 0.0000 top left 0.9900 acc 0.5050
thr 0.3000 tpr 0.0743 fpr 0.0000 top left 0.9257 acc 0.5371
thr 0.4000 tpr 0.2600 fpr 0.0000 top left 0.7400 acc 0.6300
thr 0.5000 tpr 0.6543 fpr 0.0229 top left 0.3465 acc 0.8157
thr 0.6000 tpr 0.9443 fpr 0.2614 top left 0.2673 acc 0.8414
thr 0.7000 tpr 1.0000 fpr 0.8414 top left 0.8414 acc 0.5793
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```

lv3
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0114 fpr 0.0000 top left 0.9886 acc 0.5057
thr 0.3000 tpr 0.0643 fpr 0.0000 top left 0.9357 acc 0.5321
thr 0.4000 tpr 0.2629 fpr 0.0000 top left 0.7371 acc 0.6314
thr 0.5000 tpr 0.6743 fpr 0.0271 top left 0.3268 acc 0.8236
thr 0.6000 tpr 0.9343 fpr 0.2757 top left 0.2834 acc 0.8293
thr 0.7000 tpr 1.0000 fpr 0.8757 top left 0.8757 acc 0.5621
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```
lv4
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0129 fpr 0.0000 top left 0.9871 acc 0.5064
thr 0.3000 tpr 0.0771 fpr 0.0014 top left 0.9229 acc 0.5379
thr 0.4000 tpr 0.2714 fpr 0.0086 top left 0.7286 acc 0.6314
thr 0.5000 tpr 0.6486 fpr 0.0600 top left 0.3565 acc 0.7943
thr 0.6000 tpr 0.9429 fpr 0.3829 top left 0.3871 acc 0.7800
thr 0.7000 tpr 0.9986 fpr 0.9143 top left 0.9143 acc 0.5421
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```
lv5
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0171 fpr 0.0000 top left 0.9829 acc 0.5086
thr 0.3000 tpr 0.0714 fpr 0.0029 top left 0.9286 acc 0.5343
thr 0.4000 tpr 0.2629 fpr 0.0114 top left 0.7372 acc 0.6257
thr 0.5000 tpr 0.6357 fpr 0.0757 top left 0.3721 acc 0.7800
thr 0.6000 tpr 0.9400 fpr 0.4914 top left 0.4951 acc 0.7243
thr 0.7000 tpr 1.0000 fpr 0.9429 top left 0.9429 acc 0.5286
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```

## Motion[1, 2, 4, 6, 10]
lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0129 fpr 0.0000 top left 0.9871 acc 0.5064
thr 0.3000 tpr 0.0800 fpr 0.0000 top left 0.9200 acc 0.5400
thr 0.4000 tpr 0.2443 fpr 0.0000 top left 0.7557 acc 0.6221
thr 0.5000 tpr 0.6314 fpr 0.0271 top left 0.3696 acc 0.8021
thr 0.6000 tpr 0.9357 fpr 0.2586 top left 0.2664 acc 0.8386
thr 0.7000 tpr 0.9971 fpr 0.8943 top left 0.8943 acc 0.5514
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```
lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0086 fpr 0.0000 top left 0.9914 acc 0.5043
thr 0.3000 tpr 0.0786 fpr 0.0000 top left 0.9214 acc 0.5393
thr 0.4000 tpr 0.2500 fpr 0.0014 top left 0.7500 acc 0.6243
thr 0.5000 tpr 0.6157 fpr 0.0229 top left 0.3850 acc 0.7964
thr 0.6000 tpr 0.9371 fpr 0.2471 top left 0.2550 acc 0.8450
thr 0.7000 tpr 1.0000 fpr 0.8814 top left 0.8814 acc 0.5593
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv3
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0114 fpr 0.0000 top left 0.9886 acc 0.5057
thr 0.3000 tpr 0.0771 fpr 0.0000 top left 0.9229 acc 0.5386
thr 0.4000 tpr 0.2543 fpr 0.0000 top left 0.7457 acc 0.6271
thr 0.5000 tpr 0.5900 fpr 0.0171 top left 0.4104 acc 0.7864
thr 0.6000 tpr 0.9257 fpr 0.2571 top left 0.2677 acc 0.8343
thr 0.7000 tpr 0.9971 fpr 0.8914 top left 0.8914 acc 0.5529
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```
lv4
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0114 fpr 0.0000 top left 0.9886 acc 0.5057
thr 0.3000 tpr 0.0843 fpr 0.0000 top left 0.9157 acc 0.5421
thr 0.4000 tpr 0.2500 fpr 0.0000 top left 0.7500 acc 0.6250
thr 0.5000 tpr 0.5971 fpr 0.0429 top left 0.4051 acc 0.7771
thr 0.6000 tpr 0.9243 fpr 0.3357 top left 0.3441 acc 0.7943
thr 0.7000 tpr 1.0000 fpr 0.9114 top left 0.9114 acc 0.5443
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```
lv5
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0143 fpr 0.0000 top left 0.9857 acc 0.5071
thr 0.3000 tpr 0.0986 fpr 0.0000 top left 0.9014 acc 0.5493
thr 0.4000 tpr 0.2514 fpr 0.0100 top left 0.7486 acc 0.6207
thr 0.5000 tpr 0.5900 fpr 0.0857 top left 0.4189 acc 0.7521
thr 0.6000 tpr 0.9071 fpr 0.5286 top left 0.5367 acc 0.6893
thr 0.7000 tpr 0.9943 fpr 0.9557 top left 0.9557 acc 0.5193
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```
# Test on ICPR range(0-30) with distortion
## Motion[1, 2, 4, 6, 10]
lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0443 fpr 0.0000 top left 0.9557 acc 0.5221
thr 0.3000 tpr 0.3243 fpr 0.0000 top left 0.6757 acc 0.6621
thr 0.4000 tpr 0.7700 fpr 0.0000 top left 0.2300 acc 0.8850
thr 0.5000 tpr 0.9843 fpr 0.0000 top left 0.0157 acc 0.9921
thr 0.6000 tpr 1.0000 fpr 0.2343 top left 0.2343 acc 0.8829
thr 0.7000 tpr 1.0000 fpr 0.7229 top left 0.7229 acc 0.6386
thr 0.8000 tpr 1.0000 fpr 0.9814 top left 0.9814 acc 0.5093
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0486 fpr 0.0000 top left 0.9514 acc 0.5243
thr 0.3000 tpr 0.3343 fpr 0.0000 top left 0.6657 acc 0.6671
thr 0.4000 tpr 0.7557 fpr 0.0000 top left 0.2443 acc 0.8779
thr 0.5000 tpr 0.9771 fpr 0.0014 top left 0.0229 acc 0.9879
thr 0.6000 tpr 1.0000 fpr 0.2271 top left 0.2271 acc 0.8864
thr 0.7000 tpr 1.0000 fpr 0.7271 top left 0.7271 acc 0.6364
thr 0.8000 tpr 1.0000 fpr 0.9857 top left 0.9857 acc 0.5071
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv3
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0014 fpr 0.0000 top left 0.9986 acc 0.5007
thr 0.2000 tpr 0.0529 fpr 0.0000 top left 0.9471 acc 0.5264
thr 0.3000 tpr 0.3314 fpr 0.0000 top left 0.6686 acc 0.6657
thr 0.4000 tpr 0.7700 fpr 0.0000 top left 0.2300 acc 0.8850
thr 0.5000 tpr 0.9743 fpr 0.0000 top left 0.0257 acc 0.9871
thr 0.6000 tpr 1.0000 fpr 0.2371 top left 0.2371 acc 0.8814
thr 0.7000 tpr 1.0000 fpr 0.7500 top left 0.7500 acc 0.6250
thr 0.8000 tpr 1.0000 fpr 0.9886 top left 0.9886 acc 0.5057
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv4
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0486 fpr 0.0000 top left 0.9514 acc 0.5243
thr 0.3000 tpr 0.3271 fpr 0.0000 top left 0.6729 acc 0.6636
thr 0.4000 tpr 0.7443 fpr 0.0000 top left 0.2557 acc 0.8721
thr 0.5000 tpr 0.9700 fpr 0.0014 top left 0.0300 acc 0.9843
thr 0.6000 tpr 1.0000 fpr 0.2700 top left 0.2700 acc 0.8650
thr 0.7000 tpr 1.0000 fpr 0.7743 top left 0.7743 acc 0.6129
thr 0.8000 tpr 1.0000 fpr 0.9929 top left 0.9929 acc 0.5036
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv5
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0429 fpr 0.0000 top left 0.9571 acc 0.5214
thr 0.3000 tpr 0.2914 fpr 0.0000 top left 0.7086 acc 0.6457
thr 0.4000 tpr 0.6914 fpr 0.0000 top left 0.3086 acc 0.8457
thr 0.5000 tpr 0.9457 fpr 0.0057 top left 0.0546 acc 0.9700
thr 0.6000 tpr 1.0000 fpr 0.3643 top left 0.3643 acc 0.8179
thr 0.7000 tpr 1.0000 fpr 0.9071 top left 0.9071 acc 0.5464
thr 0.8000 tpr 1.0000 fpr 0.9986 top left 0.9986 acc 0.5007
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
## Gaussian [.1, .5. 1, 2, 5]
lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0029 fpr 0.0000 top left 0.9971 acc 0.5014
thr 0.2000 tpr 0.0571 fpr 0.0000 top left 0.9429 acc 0.5286
thr 0.3000 tpr 0.3286 fpr 0.0000 top left 0.6714 acc 0.6643
thr 0.4000 tpr 0.7914 fpr 0.0000 top left 0.2086 acc 0.8957
thr 0.5000 tpr 0.9871 fpr 0.0071 top left 0.0147 acc 0.9900
thr 0.6000 tpr 1.0000 fpr 0.3300 top left 0.3300 acc 0.8350
thr 0.7000 tpr 1.0000 fpr 0.9114 top left 0.9114 acc 0.5443
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0029 fpr 0.0000 top left 0.9971 acc 0.5014
thr 0.2000 tpr 0.0600 fpr 0.0000 top left 0.9400 acc 0.5300
thr 0.3000 tpr 0.3400 fpr 0.0000 top left 0.6600 acc 0.6700
thr 0.4000 tpr 0.7829 fpr 0.0000 top left 0.2171 acc 0.8914
thr 0.5000 tpr 0.9857 fpr 0.0029 top left 0.0146 acc 0.9914
thr 0.6000 tpr 1.0000 fpr 0.3343 top left 0.3343 acc 0.8329
thr 0.7000 tpr 1.0000 fpr 0.9171 top left 0.9171 acc 0.5414
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv3
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0029 fpr 0.0000 top left 0.9971 acc 0.5014
thr 0.2000 tpr 0.0486 fpr 0.0000 top left 0.9514 acc 0.5243
thr 0.3000 tpr 0.3243 fpr 0.0000 top left 0.6757 acc 0.6621
thr 0.4000 tpr 0.7729 fpr 0.0000 top left 0.2271 acc 0.8864
thr 0.5000 tpr 0.9829 fpr 0.0100 top left 0.0198 acc 0.9864
thr 0.6000 tpr 1.0000 fpr 0.3743 top left 0.3743 acc 0.8129
thr 0.7000 tpr 1.0000 fpr 0.9086 top left 0.9086 acc 0.5457
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv4
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0029 fpr 0.0000 top left 0.9971 acc 0.5014
thr 0.2000 tpr 0.0514 fpr 0.0000 top left 0.9486 acc 0.5257
thr 0.3000 tpr 0.2871 fpr 0.0000 top left 0.7129 acc 0.6436
thr 0.4000 tpr 0.7200 fpr 0.0000 top left 0.2800 acc 0.8600
thr 0.5000 tpr 0.9771 fpr 0.0757 top left 0.0791 acc 0.9507
thr 0.6000 tpr 1.0000 fpr 0.4300 top left 0.4300 acc 0.7850
thr 0.7000 tpr 1.0000 fpr 0.8686 top left 0.8686 acc 0.5657
thr 0.8000 tpr 1.0000 fpr 0.9986 top left 0.9986 acc 0.5007
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv5
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0043 fpr 0.0000 top left 0.9957 acc 0.5021
thr 0.2000 tpr 0.0500 fpr 0.0000 top left 0.9500 acc 0.5250
thr 0.3000 tpr 0.2700 fpr 0.0000 top left 0.7300 acc 0.6350
thr 0.4000 tpr 0.7057 fpr 0.0086 top left 0.2944 acc 0.8486
thr 0.5000 tpr 0.9686 fpr 0.1329 top left 0.1365 acc 0.9179
thr 0.6000 tpr 0.9986 fpr 0.5757 top left 0.5757 acc 0.7114
thr 0.7000 tpr 1.0000 fpr 0.8943 top left 0.8943 acc 0.5529
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```

## Cafe2 model test on ICPR range(30-60) with distortion 
## Motion[1, 2, 4, 6, 10]
lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0129 fpr 0.0057 top left 0.9872 acc 0.5036
thr 0.3000 tpr 0.7986 fpr 0.8057 top left 0.8305 acc 0.4964
thr 0.4000 tpr 0.9957 fpr 1.0000 top left 1.0000 acc 0.4979
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0100 fpr 0.0000 top left 0.9900 acc 0.5050
thr 0.3000 tpr 0.7014 fpr 0.6300 top left 0.6972 acc 0.5357
thr 0.4000 tpr 0.9929 fpr 0.9800 top left 0.9800 acc 0.5064
thr 0.5000 tpr 1.0000 fpr 0.9986 top left 0.9986 acc 0.5007
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv3
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0100 fpr 0.0043 top left 0.9900 acc 0.5029
thr 0.3000 tpr 0.7329 fpr 0.7014 top left 0.7506 acc 0.5157
thr 0.4000 tpr 0.9971 fpr 1.0000 top left 1.0000 acc 0.4986
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv4
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0086 fpr 0.0014 top left 0.9914 acc 0.5036
thr 0.3000 tpr 0.7800 fpr 0.7543 top left 0.7857 acc 0.5129
thr 0.4000 tpr 0.9929 fpr 1.0000 top left 1.0000 acc 0.4964
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv5
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0029 fpr 0.0043 top left 0.9972 acc 0.4993
thr 0.3000 tpr 0.7629 fpr 0.7000 top left 0.7391 acc 0.5314
thr 0.4000 tpr 0.9986 fpr 0.9986 top left 0.9986 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```

## Gaussian[0.1, 0.5, 1, 2, 5]
lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0114 fpr 0.0186 top left 0.9887 acc 0.4964
thr 0.3000 tpr 0.8086 fpr 0.8600 top left 0.8810 acc 0.4743
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0043 fpr 0.0114 top left 0.9958 acc 0.4964
thr 0.3000 tpr 0.8100 fpr 0.8357 top left 0.8570 acc 0.4871
thr 0.4000 tpr 0.9986 fpr 1.0000 top left 1.0000 acc 0.4993
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv3
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0071 fpr 0.0071 top left 0.9929 acc 0.5000
thr 0.3000 tpr 0.7971 fpr 0.7757 top left 0.8018 acc 0.5107
thr 0.4000 tpr 1.0000 fpr 0.9971 top left 0.9971 acc 0.5014
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv4
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0029 fpr 0.0029 top left 0.9971 acc 0.5000
thr 0.3000 tpr 0.7429 fpr 0.7671 top left 0.8091 acc 0.4879
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv5
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0000 fpr 0.0057 top left 1.0000 acc 0.4971
thr 0.3000 tpr 0.7586 fpr 0.7500 top left 0.7879 acc 0.5043
thr 0.4000 tpr 0.9957 fpr 0.9971 top left 0.9972 acc 0.4993
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```

## Cafe2 model test on ICPR range(0-30) with distortion 
## Gaussian[0.1, 0.5, 1, 2, 5]

lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0129 fpr 0.0129 top left 0.9872 acc 0.5000
thr 0.3000 tpr 0.8814 fpr 0.8757 top left 0.8837 acc 0.5029
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0129 fpr 0.0057 top left 0.9872 acc 0.5036
thr 0.3000 tpr 0.8886 fpr 0.8957 top left 0.9026 acc 0.4964
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv3
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0186 fpr 0.0214 top left 0.9817 acc 0.4986
thr 0.3000 tpr 0.8186 fpr 0.8229 top left 0.8426 acc 0.4979
thr 0.4000 tpr 0.9986 fpr 1.0000 top left 1.0000 acc 0.4993
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv4
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0114 fpr 0.0029 top left 0.9886 acc 0.5043
thr 0.3000 tpr 0.8057 fpr 0.8329 top left 0.8552 acc 0.4864
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv5
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0043 fpr 0.0057 top left 0.9957 acc 0.4993
thr 0.3000 tpr 0.8671 fpr 0.8086 top left 0.8194 acc 0.5293
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
## Motion[1, 2, 4, 6, 10]
lv1
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0086 fpr 0.0014 top left 0.9914 acc 0.5036
thr 0.3000 tpr 0.9143 fpr 0.8786 top left 0.8827 acc 0.5179
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```
lv2
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0200 fpr 0.0086 top left 0.9800 acc 0.5057
thr 0.3000 tpr 0.8071 fpr 0.7829 top left 0.8063 acc 0.5121
thr 0.4000 tpr 0.9986 fpr 0.9943 top left 0.9943 acc 0.5021
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```

## Cafe2 model test on ICPR range(0-30) without distortion 
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0186 fpr 0.0143 top left 0.9815 acc 0.5021
thr 0.3000 tpr 0.9000 fpr 0.8771 top left 0.8828 acc 0.5114
thr 0.4000 tpr 0.9986 fpr 1.0000 top left 1.0000 acc 0.4993
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
```
## Cafe2 model test on ICPR range(30-60) without distortion 
```
thr 0.0000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.1000 tpr 0.0000 fpr 0.0000 top left 1.0000 acc 0.5000
thr 0.2000 tpr 0.0057 fpr 0.0129 top left 0.9944 acc 0.4964
thr 0.3000 tpr 0.8171 fpr 0.7900 top left 0.8109 acc 0.5136
thr 0.4000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.5000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.6000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.7000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.8000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000
thr 0.9000 tpr 1.0000 fpr 1.0000 top left 1.0000 acc 0.5000

```