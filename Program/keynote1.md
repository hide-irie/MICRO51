---
layout: default
title: MICRO-51 keynote-1
---

## Keynote 1: 
## From Post-K onto Post-Moore is from FLOPS onto BYTES, and from Homogeneity to Heterogeneity
**Satoshi Matsuoka, Director, Riken-CCS / Professor, Tokyo Institute of Technology**<br>
<img border="0" src="{{ site.baseurl }}/Program/matsuoka.jpg" height ="150" alt="S. Matsuoka"/><br>
9:00-10:00, Monday Oct 22, 2018<br>
Room: The Grand Ball Room

## abst.
The Japanese Flagship “Post-K” next generation exascale supercomputer we are developing with Fujitsu, slated to start functioning as a whole system in 2020, will also be a pivotal machine as we proceed towards the Post-Moore era. The heart of the machine will be the more than 100,000 A64fx processors, each one being a 48 (+4) core Arm v8 CPU with the world’s first SVE (Scalable Vector Extension) implementation --- although being general purpose to boot any breed of Linux as well as Windows, it will be a game-changing CPU with extreme performance characteristics in memory bandwidth of 840 GB/s, on-chip network of over 40GB/s, while being very low power, at 15GFlops/W besting the top GPUs. What A64fx is not, is a chip to pursue FLOPS, still being high there but retaining the BYTES/FLOPS ratio to be around 0.4, while other supercomputer chips aspiring for the first exascale machine will simply focus on FLOPS sacrificing usability and real application performance. Post-K demonstrating that pursuing exaflop Linpack performance is a relatively wasteful gesture for true utility of future high-end computing will be a pivotal signature as we head towards the end of lithography scaling and hence the end of Moore’s Law. Due to logic transistor power saturating to become constant over time, FLOPS will no longer increase, rather, alternative device/architecture/algorithmic increase must be pursued. One is the increase in bandwidth, which Post-K achieves over conventional processors by an order of magnitude using HBM2 and memory controllers and intra-chip network to drive them, while for the future we foresee x10 - x30 increase (10-30 TByte/s) with new memory devices, packaging, computing architectures as well as algorithms and software to drive them. The other is increased specialization, starting from low hanging fruits such as low precision and extreme vectorization that chips such as A64fx and GPU-CPU combinations that already realize, to more novel compute architectures such as neuromorphic, (pseudo-)quantum etc. The latter of course is more challenging due to the narrow nature of such specialization and the need to have them collaborate transparent to the users, as well as discovering new algorithms that will broaden their scope. Collectively, we face one of the most important challenge that computer science has ever faced --- end of performance scaling --- and our endeavor to solve them will lead to innovations for years to come. 

## bio.
Satoshi Matsuoka from April 2018 has become the director of Riken CCS,
the top-tier HPC center that represents HPC in Japan, currently hosting
the K Computer and developing the next generation Arm-based Post-K
machine, along with multitudes of ongoing cutting edge HPC research
being conducted, including investigating Post-Moore era computing. He
was the leader of the TSUBAME series of supercomputers, at Tokyo
Institute of Technology, where he still holds a Professor position, to
continue his research activities in HPC as well as scalable Big Data and
AI. His commendation includes the ACM Gordon Bell Prize in 2011 and the
IEEE Sidney Fernbach Award in 2014, both being one of the highest awards
in the field of HPC, as well as being the Program Chair for SC13.
