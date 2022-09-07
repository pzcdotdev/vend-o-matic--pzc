export const Inventory = ({inventory}) => {

  return <div>
      {inventory.map(drink => <div key={drink.id}>{drink.type}: {drink.quantity}</div>)}
  </div>
};