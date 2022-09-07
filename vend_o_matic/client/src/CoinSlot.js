export const CoinSlot = ({coinCount, insertCoin, returnCoin, returnedCoinCount}) => {
  return <>
    <button onClick={insertCoin}>Insert Coin</button>
    <button onClick={returnCoin}>Return Coin</button>
    <div>coin count: {coinCount}</div>
    <div>returned coins: {returnedCoinCount}</div>
  </>
}