def can_win_mahjong(hand, new_tile):
    """
    判断四川麻将是否能和牌

    参数:
    hand: 长度为13的列表，表示手牌，每张牌格式为"花色数字"，如"万1", "条5"
    new_tile: 新摸的牌，格式同手牌

    返回:
    bool: 是否能和牌
    """
    # 组合所有牌
    all_tiles = hand + [new_tile]

    # 将牌转换为内部表示格式 (花色, 数字)
    def parse_tile(tile):
        if len(tile) == 2:
            color = tile[0]
            number = int(tile[1])
        else:  # 处理"万10"这种情况（虽然正常不会出现）
            color = tile[0]
            number = int(tile[1:])
        return (color, number)

    tiles = [parse_tile(tile) for tile in all_tiles]

    # 按花色分组
    def group_by_color(tiles):
        groups = {'万': [], '条': [], '筒': []}
        for color, number in tiles:
            if color in groups:
                groups[color].append(number)
        # 对每种花色的数字排序
        for color in groups:
            groups[color].sort()
        return groups

    # 检查七对子
    def check_seven_pairs(tiles):
        if len(tiles) != 14:
            return False

        from collections import Counter
        count = Counter(tiles)

        # 检查是否有7个对子且没有重复的对子
        pairs = 0
        for tile, cnt in count.items():
            if cnt == 2:
                pairs += 1
            elif cnt == 4:  # 两个对子
                pairs += 2
            elif cnt not in [0, 2, 4]:
                return False

        return pairs == 7

    # 检查标准和牌
    def check_standard_win(tiles):
        if len(tiles) != 14:
            return False

        # 尝试每种可能的将对
        unique_tiles = list(set(tiles))
        for pair_tile in unique_tiles:
            tile_count = tiles.count(pair_tile)
            if tile_count >= 2:
                # 移除将对
                remaining = tiles.copy()
                remaining.remove(pair_tile)
                remaining.remove(pair_tile)

                # 检查剩余12张牌是否能组成4个面子
                if can_form_melds(remaining):
                    return True

        return False

    # 递归检查是否能组成面子
    def can_form_melds(tiles):
        if len(tiles) == 0:
            return True

        # 尝试找刻子
        if len(tiles) >= 3:
            for i in range(len(tiles) - 2):
                if tiles[i] == tiles[i + 1] == tiles[i + 2]:
                    # 找到刻子，递归检查剩余牌
                    remaining = tiles.copy()
                    del remaining[i:i + 3]
                    if can_form_melds(remaining):
                        return True
                    break

        # 尝试找顺子（只在同花色内）
        groups = group_by_color(tiles)
        for color in groups:
            numbers = groups[color]
            if len(numbers) < 3:
                continue

            # 检查连续数字
            for i in range(len(numbers) - 2):
                if numbers[i] + 1 == numbers[i + 1] and numbers[i] + 2 == numbers[i + 2]:
                    # 找到顺子，递归检查剩余牌
                    remaining_tiles = tiles.copy()
                    # 移除这三张牌
                    to_remove = [(color, numbers[i]), (color, numbers[i] + 1), (color, numbers[i] + 2)]
                    for tile in to_remove:
                        if tile in remaining_tiles:
                            remaining_tiles.remove(tile)

                    if can_form_melds(remaining_tiles):
                        return True
                    break

        return False

    # 主逻辑
    if check_seven_pairs(tiles):
        return True

    if check_standard_win(tiles):
        return True

    return False


# 测试用例
if __name__ == "__main__":
    # 测试用例1: 标准和牌
    hand1 = ["万1", "万1", "万2", "万3", "万4", "万5", "条2", "条3", "条4", "筒5", "筒5", "筒5", "万9"]
    new_tile1 = "万1"
    print(can_win_mahjong(hand1, new_tile1))  # True

    # 测试用例2: 七对子
    hand2 = ["万1", "万1", "万2", "万2", "万3", "万3", "万4", "万4", "万5", "万5", "万6", "万6", "万7"]
    new_tile2 = "万7"
    print(can_win_mahjong(hand2, new_tile2))  # True

    # 测试用例3: 不能和牌
    hand3 = ["万1", "万2", "万3", "万4", "万5", "万6", "万7", "万8", "万9", "条1", "条2", "条3", "筒1"]
    new_tile3 = "筒2"
    print(can_win_mahjong(hand3, new_tile3))  # False