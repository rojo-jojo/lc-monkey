/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0;
    let minPrice = prices[0];
    for (let currentPrice of prices) {
        minPrice = Math.min(minPrice, currentPrice);
        profit = Math.max(profit, currentPrice - minPrice);
        
    }
    return profit
};