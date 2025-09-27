def search_in_rotated_sorted_array(nums, target):
    """
    在旋转排序数组中搜索目标值。
    例如: nums = [1,2,3，4，,5], target = 1
    """
    n = len(nums)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2  # 使用整数除法

        # 如果找到目标值，直接返回索引
        if nums[mid] == target:
            return mid

        # 判断中间点位于旋转点的左侧（左有序段）还是右侧（右有序段）
        if nums[mid] >= nums[left]:
            # 中间点位于左有序段 (例如 [4, 5, 6] 段)
            if nums[left] <= target < nums[mid]:
                # 如果目标值在左有序段的范围内，在左侧继续搜索
                right = mid - 1
            else:
                # 否则，去右侧搜索
                left = mid + 1
        else:
            # 中间点位于右有序段 (例如 [1, 2, 3] 段)
            if nums[mid] < target <= nums[right]:
                # 如果目标值在右有序段的范围内，在右侧继续搜索
                left = mid + 1
            else:
                # 否则，去左侧搜索
                right = mid - 1

    # 未找到目标值
    return -1

# 测试用例
nums = [4, 5, 6, 1, 2, 3]
target = 1
result = search_in_rotated_sorted_array(nums, target)
print(f"数组: {nums}")
print(f"目标值 {target} 的索引是: {result}")