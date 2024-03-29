#! https://zhuanlan.zhihu.com/p/555992574
# 比特币随想 - 四个问题

一些关于比特币的经典问题、新问题的思考：

- 比特币作为一个开源项目，为什么修改比特币如此困难，比如 2100 万的上限？
- 量子计算机的商业化会摧毁比特币网络吗？
- 除了投机，有人真的使用比特币吗？
- 有“大公司”已经开始关注、持有、投资比特币吗？


## 为什么 2100 万不能被修改？

这是一个经典问题。这个问题的答案是：不是不能修改，而是没人愿意修改；即使有人修改，硬分叉的网络不会有人参与，理性人会迅速将新分叉的代币，置换成比特币。

我们应该从两个角度理解比特币网络。第一，比特币网络是由运行支持比特币网络协议的节点组成的，这些节点中有一些被称为矿工，他们负责出块；还有一些被称作全节点，他们复杂校验出块，并且把新的块快速的传播到与他相连的节点。第二，比特币网络也是人的网络。每一个参与比特币网络的人都有权运行任何版本的比特币协议，但是如果你运行的节点不能被其他人接受，达成共识，你投票的块不会有其他人接受，因此也就无法被大范围广播。

其实，比特币网络的精髓就是协议和广播。

我举个例子，假设我现在下载了比特币软件的源代码，BitcoinCore，然后再本地修改了该软件，把上限改成 4200 万。现在我就可以启动我的矿工节点，准备出块。我很幸运，很快我就解锁了一个新块，而这个块包含的信息指向了 4200 万的上限。当我广播这个块的时候，周围运行原始版本的代码的节点立刻拒绝这个新块，因为他们运行的软件认为这个块是无效的。一旦我出的块无法被其他节点接受，这个块就没有任何意义，因为他无法被广播到绝大多数节点，形成共识。

再进一步，我知道我无法在原始比特币网络生存，我就去联系风投公司，给我的新比特币网络投资，构建我自己硬分叉网络。在这个网络，比特币的上限是 4200 万。但是，由于这是一个新网络，无论是节点数量，还是网络安全性都无法与比特币主网相比。这个硬分叉很难吸引人加入，即使加入，人们也会倾向把新分叉的代币，置换成更加安全、可用性更高的比特币代币，因为这么做符合经济利益。

事实上，我觉得例子在历史上已经发生过好多次了，其中著名的例子：

- 比特币现金
- BSV
- 比特币黄金

这几个项目基本上就是上面的例子的现实版。而他们现在的状况，也跟例子中描述的一样：**无人问津**。

所以，2100 万可以被修改么？当然可以，可以随意修改。但是这个问题的关键并不是代码能不能改，而是网络中参与的人的共识和经济利益。

## 量子计算机的商业化会摧毁比特币网络吗？

这个问题有两个分支：

- 量子计算机破解公钥密码学，导致私钥泄露
- 量子计算机挖矿，导致算力失衡

简单的答案是：不必担心，也不会摧毁。

### 公钥密码学

众所周知，比特币的核心就是公钥密码学，通过私钥和签名实现 UTXO 的转移。简单说，公钥密码学建立在一个假设上：有一类数学问题，目前的电子计算不能再多项式时间内求解。

而目前的量子计算机研究表明，量子计算机可以在多项式时间内求解这类数学问题中的一部分，这其中就包含比特币使用的加密算法：Elliptic Curve Digital Signature Algorithm or ECDSA。

这里面有几个问题：

首先，能够破解该加密算法的量子算法叫做 Shor 算法。但是，有研究指出，按照目前的量子比特（量子计算的计算单元）质量，至少需要 100 万个量子比特，才有可能破解比特币加密强度的算法。而 2022 年，IBM 拥有的世界上最强大的量子计算机只有 100 多个量子比特。更加重要的是，没人知道量子比特是不是可以发展到 100 万级别，即没有知道这是一个简单的工程问题，还是根本无解的问题。

第二，即便量子计算机实现了突破，可以运行大规模 Shor 算法，密码学界也有应对方案。其实，早在上个世纪 90 年代，量子安全的加密算法就已经出现了（有趣的是，Shor 算法也是上个世纪的产物，只不过但是还没有真的量子计算机）。换句话说，比特币可以通过硬分叉更换加密算法。联系上一个问题，这种硬分叉更容易形成共识，并且符合参与者的经济利益。

最后，退一万步说，真的出现了强大的量子计算机，人们首先应该担心的一定不是比特币，而是整个互联网的安全。众所周知，我们日常的互联网行为都是基于公钥密码学来交换秘钥，对通讯进行加密的。一旦这种计算机出现，而互联网没有更新安全算法，几乎所有的加密通讯都不在成立，你的银行账号密码、邮箱密码都会暴露在互联网上。

### 挖矿

关于挖矿，本质上是在一个极大的搜索空间内，搜索一个数字的问题。而一个叫做 grover 算法的量子算法可以把这种搜索从线性时间，降低成平方根时间。理论上，这种算法可以加速机器的挖矿速度。

但是，跟前一个问题一样，这种级别的搜索，需要大量的量子比特。而比特币网络完全可以硬分叉，增大所搜空间，轻易解决这个问题。

综上，量子计算机商业化不能对比特币网络构成实质性的威胁。

## 除了投机，有人真的使用比特币吗？

如果是 5 年前问这个问题，答案可能是很少或者没有。但是 2022 年，这个问题的答案是肯定的。

萨尔瓦多共和国已经构建了比特币城市，该城市很多店铺可以使用比特币的闪电网络进行支付，其交易速度、吞吐量和成本都远远低于 VISA 网络。萨尔瓦多共和国属于第三世界国家，应急羸弱，长期以来他们只能依靠美金作为货币，来抑制是用本国货币导致的贬值和通胀。但是，大家都清楚一个国家实用外国货币作为法币的问题。因此，他们另辟蹊径，采用比特币作为法币。

## 有“大公司”已经开始关注、持有、投资比特币吗？

2022 年，答案是有。

https://www.buybitcoinworldwide.com/treasuries/

下图是持有比特币的上市公司：

![](https://i.imgur.com/ZFKVmwq.png)

下图是持有比特币的国家和私人公司：

![](https://i.imgur.com/ZkNFvcU.png)

下图是目前作为投资工具的比特币：

![](https://i.imgur.com/geA70rt.png)


之前我翻译过一篇来自全球最大上市对冲基金公司英士曼集团的关于比特币机构用户投资的文章：https://zhuanlan.zhihu.com/p/546096802

还有很多其他投资公司也都在关注比特币：

- [比特币随想 - 机构投资评估 1](https://zhuanlan.zhihu.com/p/528930900)
- Arc Investment
- 富达投资，Fidelity
- 黑石基金，BlackRock