/*
 * @lc app=leetcode id=704 lang=javascript
 *
 * [704] Binary Search
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if(nums.length===0){return -1;}
    let left=0;
    let right=nums.length-1;
    let mid;
    
    while(left<=right){
        mid=Math.floor(left+(right-left)/2)
        if(nums[mid]===target){
            return mid;
        }else if(nums[mid]<target){
            left=mid+1;
        }else if(nums[mid]>target){
            right=mid-1;
        }
    }

    return -1;
};
// @lc code=end

