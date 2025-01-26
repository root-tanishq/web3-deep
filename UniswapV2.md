## Swap Token
- https://www.youtube.com/watch?v=qB2Ulx201wY&list=PLO5VPQH6OWdX-Rh7RonjZhOd9pb9zOnHW&index=1&pp=iAQB
- https://solidity-by-example.org/defi/uniswap-v2/

## Pricing calculation for exchange rate
- https://www.youtube.com/watch?v=IL7cRj5vzEU&list=PLO5VPQH6OWdX-Rh7RonjZhOd9pb9zOnHW&index=2
- calculates with formula `x * y = k`
![](../attachments/Pasted%20image%2020240819155001.png)
- `dx` is the amout of token that you will sell and `dy` is the amout of token you will receive 
- formula for finding out the `dy` value for a exchange `dy = y * 0.997 dx/(x+ 0.997 * dx)`
- Uniswap trading fee = 0.3%
- Uniswap v2 Router contract - https://etherscan.io/address/0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D#readContract
## Add Liquidity
- https://www.youtube.com/watch?v=816kTTNzcHs&list=PLO5VPQH6OWdX-Rh7RonjZhOd9pb9zOnHW&index=3
- Liquidity provider earns trading fees and they provide the liquidity tokens for swap

## Swap Math
- Formula for L *Liquidity* calculation `xy=L^2`
- Swap math calculation `dy = y * dx / x + dx` does not include the fees for the swaps

## Swap Fees
- `f` means fees for the swap of tokens 

 ![](../attachments/Pasted%20image%2020250115193149.png)
- `getAmountOut` means how much tokens you will get from entering this amount where as `getAmountIn` is about I want this much token how much token do I need to give it for 
- `Slippage` => Difference between the price you expect to receive vs what you actually receive
	- Causes of slippage 1. Market movements 2. delay between the time you sent the transaction and execute it  