import { InventoryItem } from "./InventoryItem";

export const Inventory = ({inventory, purchaseDrink}) => {
  const containerStyle = {
    display: 'flex',
    flexDirection: 'column'
  }

  return <div style={containerStyle}>
      {inventory.map(inventoryItem => <InventoryItem inventoryItem={inventoryItem} key={inventoryItem.id} purchaseDrink={purchaseDrink}/>)}
  </div>
};