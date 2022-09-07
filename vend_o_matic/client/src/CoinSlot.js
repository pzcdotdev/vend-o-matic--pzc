export const CoinSlot = ({coin_count, insertCoin}) => {
  return <>
    <button onClick={insertCoin}>Insert Coin</button>
    <div>coin count: {coin_count}</div>
  </>
}