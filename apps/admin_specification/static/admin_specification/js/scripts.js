window.addEventListener("DOMContentLoaded", () => {
  const catalog = document.querySelector(".spetification-product-catalog");
  if (catalog) {
    const catalogItems = catalog.querySelectorAll(".catalog-item");
    catalogItems.forEach((catalogItem) => {
      const buttonContainer = catalogItem.querySelector(".quantity-buttons");
      const plusButton = buttonContainer.querySelector(".plus-button");
      const minusButton = buttonContainer.querySelector(".minus-button");
      const countQuantityZone = buttonContainer.querySelector("span");
      let countQuantity = +countQuantityZone.textContent;

      plusButton.onclick = () => {
        countQuantity++;
        countQuantityZone.textContent = countQuantity;
        minusButton.disabled = false;

        if (countQuantityZone.textContent.length > 1) {
          countQuantityZone.style.left = "40.5%";
        }
      };

      minusButton.onclick = () => {
        countQuantity--;
        countQuantityZone.textContent = countQuantity;
        if (countQuantity <= 0) {
          minusButton.disabled = true;
        } else {
          minusButton.disabled = false;
        }

        if (countQuantityZone.textContent.length <= 1) {
          countQuantityZone.style.left = "45.5%";
        }
      };

      const priceContainer = catalogItem.querySelector(".price");
      const price = priceContainer.querySelector(".price-count");

      if (price) {
        const priceNumberValue = price.textContent.replace(",", ".");

        price.textContent = (+priceNumberValue).toLocaleString(undefined, {
          minimumFractionDigits: 2,
        });
      }
    });
  }
});
