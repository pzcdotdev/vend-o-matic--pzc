export const InventoryItem = ({ inventoryItem, purchaseDrink }) => {

  return <button data-id={inventoryItem.id} onClick={purchaseDrink}>{inventoryItem.type}</button>

}