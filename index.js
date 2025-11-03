/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let i = 0;
    for (let j = 0; j < nums.length; j++) {
      const num = nums[j];
      if (num != val) {
        nums[i] = num;
        i++
      }
    }
    return i;
};
// removeElement([3,2,2,3], 3);

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let hash = new Map();

    let i = 0;
    for (let j = 0; j < nums.length; j++) {
      const num = nums[j];
      let exists = hash.has(num);
      if (!exists) {
        nums[i] = num;
        i++
        hash.set(num);
        continue;
      }
    }
    return i;
};
// removeDuplicates([1,1,2])


//Remove duplicates pt2
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let hash = new Map();
    let i = 0;

    for (let j = 0; j < nums.length; j++) {
      const num = nums[j];
      let founded = hash.get(num);
      hash.set(num, (founded || 0) + 1);
      if (!founded || (founded && founded < 2)) {
        nums[i] = num;
        i++
      }
    }
    return i;
};
// removeDuplicates([1,1,1,2,2,3])

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let quantity = nums.length;
    let hash = new Map();
    for (let i = 0; i < quantity; i++) {
      const num = nums[i];
      let founded = hash.get(num);
      const newValue = hash.set(num, (founded | 0) + 1).get(num);
      if (newValue > quantity / 2) {
        return num;
      }
    }
};

// majorityElement([3,2,3]);

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {

  let quantity = nums.length;
  let normalizedK = k % quantity;

  function reverse(start, end) {
    while(start < end) {
      [nums[start], nums[end]] = [nums[end], nums[start]];
      start++
      end--;
    }
  }

  reverse(0, quantity -1);

  reverse(0, normalizedK -1);

  reverse(normalizedK, quantity -1);
};

// rotate([-1,-100,3,99], 2);


/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let words = s.split(' ');
    let reversedWords = words.map(word => word.split('').reverse().join(''));
    return reversedWords.join(' ');
};

// console.log(reverseWords("Mr Ding"));


/**
 * @param {string} s
 * @return {number}
 */
var maximumLengthSubstring = function(s) {
  let l = 0;
  let r = 0;
  let max = 1;
  let counter = new Map();
  counter.set(s[0], 1);
  while (r < s.length - 1) {
    r++;
    if (counter.has(s[r])) {
      counter.set(s[r], counter.get(s[r]) + 1);
    } else {
      counter.set(s[r], 1);
    }
    while (counter.get(s[r]) === 3) {
      counter.set(s[l], counter.get(s[l]) - 1);
      l++;
    }
    max = r - l + 1;
  }
  return max;
};

// console.log(maximumLengthSubstring("aadaad"));


var binarySearch = function(arr, target, left = 0, right = null) {
  if (right === null) {
    right = arr.length;
  }
  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) {
      return mid;
    }
  }
};

var exponentialSearch = function(arr, target) {
  if (arr[0] === target) {
    return 0;
  }
  let n = arr.length;
  let i = 1;
  while (i < n && arr[i] < target) {
    i *= 2;
  }
  if (arr[i] === target) {
    return i;
  }
  return binarySearch(arr, target, i / 2, Math.min(i, n - 1));
};


var firstUniqueCharacter = function(s) {
  let d = new Map();
  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (!d.has(char)) {
      d.set(char, [i, 1])
    } else {
      d.set(char, [d.get(char)[0], d.get(char)[1] + 1]);
    }
  }

  for (let [_, value] of d) {
    if (value[1] === 1) {
      return value[0];
    }
  }
  return -1;
};

// console.log(firstUniqueCharacter("loveleetcode"));


// leetcode. 219. Contains Duplicate II

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
  let map = new Map();
  let result = false;
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (map.has(num) && Math.abs(map.get(num) - i) <= k) {
        result = true;
        break;
    }
    map.set(num, i);
  }
  return result;
};

// console.log(containsNearbyDuplicate([1,0,1,1], 1));


// leetcode. 1. Two Sum
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
  let hash = new Map();
  for (let i = 0; nums.length; i++){
    const number = nums[i];

    if (number >= target) {
      continue;
    }

    const diff = target - number;

    if (hash.has(diff)) {
      return [hash.get(diff), i];
    }
    hash.set(number,i);
  }
};

console.log(twoSum([3,3], 6));