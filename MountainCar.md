# MountainCar Report

**Author**: Sheikh Saad Abdullah

## Varying states between 5, 10, 20, 100 with fixed alpha of 0.1:

---

### Mountain Car with 5 states and alpha 0.1

```
State: [-0.44084334 -0.00162612] | Reward: -1.0 | Terminated? False
State: [-0.44308376 -0.00224043] | Reward: -2.0 | Terminated? False
State: [-0.4449222  -0.00183844] | Reward: -3.0 | Terminated? False
State: [-0.44834527 -0.00342305] | Reward: -4.0 | Terminated? False
State: [-0.45232794 -0.00398267] | Reward: -5.0 | Terminated? False
State: [-0.45584106 -0.00351314] | Reward: -6.0 | Terminated? False
State: [-0.4608589  -0.00501783] | Reward: -7.0 | Terminated? False
State: [-0.4663445 -0.0054856] | Reward: -8.0 | Terminated? False
State: [-0.47125742 -0.0049129 ] | Reward: -9.0 | Terminated? False
State: [-0.47756127 -0.00630385] | Reward: -10.0 | Terminated? False
State: [-0.4842093  -0.00664804] | Reward: -11.0 | Terminated? False

...

State: [-0.4841352  -0.00093942] | Reward: -29990.0 | Terminated? False
State: [-4.8436993e-01 -2.3470669e-04] | Reward: -29991.0 | Terminated? False
State: [-0.48489818 -0.00052824] | Reward: -29992.0 | Terminated? False
State: [-0.48671603 -0.00181785] | Reward: -29993.0 | Terminated? False
State: [-0.48780993 -0.0010939 ] | Reward: -29994.0 | Terminated? False
State: [-0.48917174 -0.0013618 ] | Reward: -29995.0 | Terminated? False
State: [-0.49179128 -0.00261955] | Reward: -29996.0 | Terminated? False
State: [-0.49364904 -0.00185774] | Reward: -29997.0 | Terminated? False
State: [-0.4957311  -0.00208206] | Reward: -29998.0 | Terminated? False
State: [-0.49902192 -0.00329083] | Reward: -29999.0 | Terminated? False
State: [-0.5014969  -0.00247499] | Reward: -30000.0 | Terminated? False
State: [-0.5041375  -0.00264063] | Reward: -30001.0 | Terminated? False
Too many iterations. Stopping run...
```

**Observation**: Goal was not reached even after -30K reward.

---

### Mountain Car with 10 states and alpha 0.1

```
State: [-5.814237e-01 -5.727167e-04] | Reward: -1.0 | Terminated? False
State: [-0.5825649 -0.0011412] | Reward: -2.0 | Terminated? False
State: [-0.58326614 -0.00070126] | Reward: -3.0 | Terminated? False
State: [-0.5825223   0.00074386] | Reward: -4.0 | Terminated? False
State: [-0.58133876  0.00118349] | Reward: -5.0 | Terminated? False
State: [-0.5787244   0.00261438] | Reward: -6.0 | Terminated? False
State: [-0.5766985   0.00202594] | Reward: -7.0 | Terminated? False
State: [-0.574276   0.0024225] | Reward: -8.0 | Terminated? False
State: [-0.57047486  0.00380112] | Reward: -9.0 | Terminated? False
State: [-0.5673233   0.00315153] | Reward: -10.0 | Terminated? False
State: [-0.5638448   0.00347853] | Reward: -11.0 | Terminated? False

...

State: [0.29152334 0.02789901] | Reward: -10080.0 | Terminated? False
State: [0.316819  0.0252957] | Reward: -10081.0 | Terminated? False
State: [0.34066144 0.02384242] | Reward: -10082.0 | Terminated? False
State: [0.36419967 0.02353823] | Reward: -10083.0 | Terminated? False
State: [0.38558745 0.02138778] | Reward: -10084.0 | Terminated? False
State: [0.40596947 0.02038202] | Reward: -10085.0 | Terminated? False
State: [0.42648748 0.020518  ] | Reward: -10086.0 | Terminated? False
State: [0.44528738 0.01879992] | Reward: -10087.0 | Terminated? False
State: [0.46350536 0.01821797] | Reward: -10088.0 | Terminated? False
State: [0.48227507 0.01876971] | Reward: -10089.0 | Terminated? False
State: [0.49973565 0.01746058] | Reward: -10090.0 | Terminated? False
State: [0.5170174  0.01728175] | Reward: -10091.0 | Terminated? True
end
```

**Observation**: Goal was reached after -10K reward.

---

### Mountain Car with 20 states and alpha 0.1

```
State: [-0.51691306 -0.00105807] | Reward: -1.0 | Terminated? False
State: [-0.5190213  -0.00210821] | Reward: -2.0 | Terminated? False
State: [-0.5211638  -0.00214254] | Reward: -3.0 | Terminated? False
State: [-0.5223246 -0.0011608] | Reward: -4.0 | Terminated? False
State: [-0.524495   -0.00217036] | Reward: -5.0 | Terminated? False
State: [-0.52665865 -0.00216364] | Reward: -6.0 | Terminated? False
State: [-0.5277993  -0.00114069] | Reward: -7.0 | Terminated? False
State: [-0.52990854 -0.00210919] | Reward: -8.0 | Terminated? False
State: [-0.5319704  -0.00206187] | Reward: -9.0 | Terminated? False
State: [-0.5329695  -0.00099909] | Reward: -10.0 | Terminated? False
State: [-0.5348983  -0.00192882] | Reward: -11.0 | Terminated? False

...

State: [0.40334395 0.01266028] | Reward: -9987.0 | Terminated? False
State: [0.41512176 0.0117778 ] | Reward: -9988.0 | Terminated? False
State: [0.42710027 0.01197851] | Reward: -9989.0 | Terminated? False
State: [0.4373651  0.01026484] | Reward: -9990.0 | Terminated? False
State: [0.44699037 0.00962527] | Reward: -9991.0 | Terminated? False
State: [0.45704612 0.01005576] | Reward: -9992.0 | Terminated? False
State: [0.46560606 0.00855992] | Reward: -9993.0 | Terminated? False
State: [0.47373322 0.00812717] | Reward: -9994.0 | Terminated? False
State: [0.4824878  0.00875457] | Reward: -9995.0 | Terminated? False
State: [0.4899348  0.00744702] | Reward: -9996.0 | Terminated? False
State: [0.49712977 0.00719497] | Reward: -9997.0 | Terminated? False
State: [0.5051264  0.00799666] | Reward: -9998.0 | Terminated? True
end
```

**Observation**: Goal was reached a little before -10K reward.

---

### Mountain Car with 100 states and alpha 0.1

```
State: [-0.4459515  -0.00158869] | Reward: -1.0 | Terminated? False
State: [-0.44911727 -0.00316579] | Reward: -2.0 | Terminated? False
State: [-0.45383704 -0.00471977] | Reward: -3.0 | Terminated? False
State: [-0.4600762  -0.00623917] | Reward: -4.0 | Terminated? False
State: [-0.4677889  -0.00771271] | Reward: -5.0 | Terminated? False
State: [-0.47691825 -0.00912933] | Reward: -6.0 | Terminated? False
State: [-0.48739654 -0.01047829] | Reward: -7.0 | Terminated? False
State: [-0.4991458  -0.01174927] | Reward: -8.0 | Terminated? False
State: [-0.51207834 -0.01293251] | Reward: -9.0 | Terminated? False
State: [-0.52609724 -0.01401889] | Reward: -10.0 | Terminated? False
State: [-0.54109734 -0.01500015] | Reward: -11.0 | Terminated? False

...

State: [0.0106732  0.01742971] | Reward: -29990.0 | Terminated? False
State: [0.02660419 0.01593099] | Reward: -29991.0 | Terminated? False
State: [0.03904314 0.01243895] | Reward: -29992.0 | Terminated? False
State: [0.04999921 0.01095608] | Reward: -29993.0 | Terminated? False
State: [0.05948336 0.00948415] | Reward: -29994.0 | Terminated? False
State: [0.06650721 0.00702385] | Reward: -29995.0 | Terminated? False
State: [0.07108065 0.00457344] | Reward: -29996.0 | Terminated? False
State: [0.07221071 0.00113007] | Reward: -29997.0 | Terminated? False
State: [ 0.07189922 -0.0003115 ] | Reward: -29998.0 | Terminated? False
State: [ 0.06814565 -0.00375357] | Reward: -29999.0 | Terminated? False
State: [ 0.06294414 -0.00520151] | Reward: -30000.0 | Terminated? False
State: [ 0.05428708 -0.00865707] | Reward: -30001.0 | Terminated? False
Too many iterations. Stopping run...
```

**Observation**: Goal was not reached even after -30K reward.

---

## Varying alpha between 0.01, 0.1, 0.5 with fixed state of 10:

---

### Mountain Car with 10 states and alpha 0.01

```
State: [-0.5378605  -0.00089981] | Reward: -1.0 | Terminated? False
State: [-0.53965336 -0.00179288] | Reward: -2.0 | Terminated? False
State: [-0.5413259  -0.00167252] | Reward: -3.0 | Terminated? False
State: [-5.4186553e-01 -5.3962826e-04] | Reward: -4.0 | Terminated? False
State: [-0.5432682 -0.0014027] | Reward: -5.0 | Terminated? False
State: [-0.5445235  -0.00125526] | Reward: -6.0 | Terminated? False
State: [-5.4462194e-01 -9.8428492e-05] | Reward: -7.0 | Terminated? False
State: [-0.5455628  -0.00094086] | Reward: -8.0 | Terminated? False
State: [-0.54633904 -0.00077625] | Reward: -9.0 | Terminated? False
State: [-5.4594487e-01  3.9417107e-04] | Reward: -10.0 | Terminated? False
State: [-0.5453832   0.00056164] | Reward: -11.0 | Terminated? False

...

State: [-0.8297783   0.02014649] | Reward: -29990.0 | Terminated? False
State: [-0.8076451   0.02213328] | Reward: -29991.0 | Terminated? False
State: [-0.78463006  0.023015  ] | Reward: -29992.0 | Terminated? False
State: [-0.75885135  0.02577869] | Reward: -29993.0 | Terminated? False
State: [-0.73145115  0.02740022] | Reward: -29994.0 | Terminated? False
State: [-0.7035911   0.02786004] | Reward: -29995.0 | Terminated? False
State: [-0.67344576  0.03014533] | Reward: -29996.0 | Terminated? False
State: [-0.6412141   0.03223171] | Reward: -29997.0 | Terminated? False
State: [-0.60911846  0.03209563] | Reward: -29998.0 | Terminated? False
State: [-0.57538843  0.03373002] | Reward: -29999.0 | Terminated? False
State: [-0.54127157  0.03411688] | Reward: -30000.0 | Terminated? False
State: [-0.5080222   0.03324936] | Reward: -30001.0 | Terminated? False
Too many iterations. Stopping run...
```

**Observation**: Goal was not reached even after -30K reward.

---

### Mountain Car with 10 states and alpha 0.1

```
State: [-0.5330952 -0.0009358] | Reward: -1.0 | Terminated? False
State: [-0.53495973 -0.00186459] | Reward: -2.0 | Terminated? False
State: [-0.5367392 -0.0017794] | Reward: -3.0 | Terminated? False
State: [-0.53742003 -0.00068087] | Reward: -4.0 | Terminated? False
State: [-0.53899723 -0.00157724] | Reward: -5.0 | Terminated? False
State: [-0.54045904 -0.00146179] | Reward: -6.0 | Terminated? False
State: [-5.4079443e-01 -3.3539603e-04] | Reward: -7.0 | Terminated? False
State: [-0.54200095 -0.00120649] | Reward: -8.0 | Terminated? False
State: [-0.5430695  -0.00106854] | Reward: -9.0 | Terminated? False
State: [-5.4299206e-01  7.7407669e-05] | Reward: -10.0 | Terminated? False
State: [-5.4276931e-01  2.2277533e-04] | Reward: -11.0 | Terminated? False

...

State: [0.28590658 0.02713398] | Reward: -12498.0 | Terminated? False
State: [0.31040516 0.02449857] | Reward: -12499.0 | Terminated? False
State: [0.33441156 0.02400642] | Reward: -12500.0 | Terminated? False
State: [0.35607404 0.02166248] | Reward: -12501.0 | Terminated? False
State: [0.3775323  0.02145827] | Reward: -12502.0 | Terminated? False
State: [0.3969298 0.0193975] | Reward: -12503.0 | Terminated? False
State: [0.4154     0.01847018] | Reward: -12504.0 | Terminated? False
State: [0.43407285 0.01867286] | Reward: -12505.0 | Terminated? False
State: [0.45108232 0.01700946] | Reward: -12506.0 | Terminated? False
State: [0.46755219 0.01646987] | Reward: -12507.0 | Terminated? False
State: [0.48460367 0.0170515 ] | Reward: -12508.0 | Terminated? False
State: [0.50036335 0.0157597 ] | Reward: -12509.0 | Terminated? True
end
```

**Observation**: Goal was reached after -12.5K reward.

---

### Mountain Car with 10 states and alpha 0.5

```
State: [-5.8847058e-01 -5.2035664e-04] | Reward: -1.0 | Terminated? False
State: [-0.58950746 -0.00103688] | Reward: -2.0 | Terminated? False
State: [-5.900532e-01 -5.457833e-04] | Reward: -3.0 | Terminated? False
State: [-0.5891039   0.00094933] | Reward: -4.0 | Terminated? False
State: [-0.58766645  0.00143746] | Reward: -5.0 | Terminated? False
State: [-0.5847514   0.00291502] | Reward: -6.0 | Terminated? False
State: [-0.58238035  0.00237109] | Reward: -7.0 | Terminated? False
State: [-0.57957065  0.00280967] | Reward: -8.0 | Terminated? False
State: [-0.57534313  0.00422749] | Reward: -9.0 | Terminated? False
State: [-0.5717291   0.00361402] | Reward: -10.0 | Terminated? False
State: [-0.5677554   0.00397374] | Reward: -11.0 | Terminated? False

...

State: [0.35974938 0.01581295] | Reward: -10069.0 | Terminated? False
State: [0.37338233 0.01363297] | Reward: -10070.0 | Terminated? False
State: [0.38692644 0.0135441 ] | Reward: -10071.0 | Terminated? False
State: [0.40047398 0.01354753] | Reward: -10072.0 | Terminated? False
State: [0.41411892 0.01364495] | Reward: -10073.0 | Terminated? False
State: [0.42795745 0.01383854] | Reward: -10074.0 | Terminated? False
State: [0.44208848 0.01413103] | Reward: -10075.0 | Terminated? False
State: [0.45461425 0.01252578] | Reward: -10076.0 | Terminated? False
State: [0.46662635 0.01201208] | Reward: -10077.0 | Terminated? False
State: [0.4792132  0.01258686] | Reward: -10078.0 | Terminated? False
State: [0.49046814 0.01125495] | Reward: -10079.0 | Terminated? False
State: [0.50147504 0.01100688] | Reward: -10080.0 | Terminated? True
end
```

**Observation**: Goal was reached after -10K reward.

---

