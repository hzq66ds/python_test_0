class Node(object):
    def __init__(self, score=None):
        self.score = score
        self.left = None
        self.right = None
        self.feature = None
        self.split = None


class RegressionTree(object):
    def __init__(self):
        self.root = Node()
        self.height = 1


def _get_split_mse(self, X, y, idx, feature, split):
    split_sum = [0, 0]
    split_cnt = [0, 0]
    split_sqr_sum = [0, 0]

    for i in idx:
        xi, yi = X[i][feature], y[i]
        if xi < split:
            split_cnt[0] += 1
            split_sum[0] += yi
            split_sqr_sum[0] += yi ** 2
        else:
            split_cnt[1] += 1
            split_sum[1] += yi
            split_sqr_sum[1] += yi ** 2

    split_avg = [split_sum[0] / split_cnt[0], split_sum[1] / split_cnt[1]]
    split_mse = [split_sqr_sum[0] - split_sum[0] * split_avg[0],
                    split_sqr_sum[1] - split_sum[1] * split_avg[1]]
    return sum(split_mse), split, split_avg


def _choose_split_point(self, X, y, idx, feature):
    unique = set([X[i][feature] for i in idx])
    if len(unique) == 1:
        return None

    unique.remove(min(unique))
    mse, split, split_avg = min(
        (self._get_split_mse(X, y, idx, feature, split)
            for split in unique), key=lambda x: x[0])
    return mse, feature, split, split_avg


def _choose_feature(self, X, y, idx):
    m = len(X[0])
    split_rets = [x for x in map(lambda x: self._choose_split_point(
        X, y, idx, x), range(m)) if x is not None]

    if split_rets == []:
        return None
    _, feature, split, split_avg = min(
        split_rets, key=lambda x: x[0])

    idx_split = [[], []]
    while idx:
        i = idx.pop()
        xi = X[i][feature]
        if xi < split:
            idx_split[0].append(i)
        else:
            idx_split[1].append(i)
    return feature, split, split_avg, idx_split


def _expr2literal(self, expr):
    feature, op, split = expr
    op = ">=" if op == 1 else "<"
    return "Feature%d %s %.4f" % (feature, op, split)


def _get_rules(self):
    que = [[self.root, []]]
    self.rules = []

    while que:
        nd, exprs = que.pop(0)
        if not(nd.left or nd.right):
            literals = list(map(self._expr2literal, exprs))
            self.rules.append([literals, nd.score])

        if nd.left:
            rule_left = copy(exprs)
            rule_left.append([nd.feature, -1, nd.split])
            que.append([nd.left, rule_left])

        if nd.right:
            rule_right = copy(exprs)
            rule_right.append([nd.feature, 1, nd.split])
            que.append([nd.right, rule_right])


def fit(self, X, y, max_depth=5, min_samples_split=2):
    self.root.score = sum(y) / len(y)
    idxs = list(range(len(y)))
    que = [(self.depth + 1, self.root, idxs)]

    while que:
        depth, nd, idxs = que.pop(0)

        if depth > max_depth:
            depth -= 1
            break

        if len(idxs) < min_samples_split or \
                len(set(map(lambda i: y[i], idxs))) == 1:
            continue

        split_ret = self._choose_feature(X, y, idxs)
        if split_ret is None:
            continue

        _, feature, split, split_avg = split_ret

        nd.feature = feature
        nd.split = split
        nd.left = Node(split_avg[0])
        nd.right = Node(split_avg[1])

        idxs_split = list_split(X, idxs, feature, split)
        que.append((depth+1, nd.left, idxs_split[0]))
        que.append((depth+1, nd.right, idxs_split[1]))

    self.depth = depth
    self._get_rules()


def print_rules(self):
    for i, rule in enumerate(self.rules):
        literals, score = rule
        print("Rule %d: " % i, ' | '.join(
            literals) + ' => split_hat %.4f' % score)


def _predict(self, row):
    nd = self.root
    while nd.left and nd.right:
        if row[nd.feature] < nd.split:
            nd = nd.left
        else:
            nd = nd.right
    return nd.score


def predict(self, X):
    return [self._predict(Xi) for Xi in X]


print("Tesing the accuracy of RegressionTree...")
#X, y = load_boston_house_prices()
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)

reg = RegressionTree()
reg.fit(X=X_train, y=y_train, max_depth=5)

reg.print_rules()
get_r2(reg, X_test, y_test)


