function getCurrentPrice(p) {
  const price = p.replace(",", ".");
  return price;
}
let productsSpecificationList = [];

let localStorageSpecification = JSON.parse(
  localStorage.getItem("specificationValues")
);
const saveProduct = (product) => {
  if (localStorageSpecification) {
    localStorageSpecification = localStorageSpecification.filter(
      (item) => item.id !== product.id
    );
    localStorageSpecification.push(product);
    localStorage.setItem(
      "specificationValues",
      JSON.stringify(localStorageSpecification)
    );
  } else {
    localStorage.setItem(
      "specificationValues",
      JSON.stringify(productsSpecificationList)
    );
  }
};

const setProduct = (product) => {
  if (productsSpecificationList.length <= 0) {
    productsSpecificationList.push(product);
  } else {
    productsSpecificationList = productsSpecificationList.filter(
      (item) => item.id !== product.id
    );
    productsSpecificationList.push(product);
  }
  saveProduct(product);
};

window.addEventListener("DOMContentLoaded", () => {
  const specificationContent = document.querySelector(".specification-content");
  const specificationLinkContainer = specificationContent.querySelector(
    ".specification-link-container"
  );
  const specificationLinkContainerProductValue =
    specificationLinkContainer.querySelector("span");
  if (localStorageSpecification) {
    specificationLinkContainerProductValue.textContent =
      localStorageSpecification.length;
  } else {
    specificationLinkContainerProductValue.textContent = 0;
  }

  const catalog = specificationContent.querySelector(
    ".spetification-product-catalog"
  );
  if (catalog) {
    const catalogItems = catalog.querySelectorAll(".catalog-item");
    catalogItems.forEach((catalogItem) => {
      const productId = catalogItem.getAttribute("data-id");
      const productName = catalogItem.querySelector(".name").textContent;
      const productPrice = catalogItem.getAttribute("data-price");
      const productMotrumId = catalogItem.getAttribute("data-motrum-id");
      const productSalerId = catalogItem.getAttribute("data-saler-id");
      const buttonContainer = catalogItem.querySelector(".quantity-buttons");
      const plusButton = buttonContainer.querySelector(".plus-button");
      const minusButton = buttonContainer.querySelector(".minus-button");
      const addSpecificationButton = catalogItem.querySelector(
        ".add-specification-button"
      );
      const countQuantityZone = buttonContainer.querySelector("span");

      let countQuantity = +countQuantityZone.textContent;

      plusButton.onclick = () => {
        countQuantity++;
        countQuantityZone.textContent = countQuantity;
        minusButton.disabled = false;
        addSpecificationButton.disabled = false;

        if (countQuantityZone.textContent.length > 1) {
          countQuantityZone.style.left = "40.5%";
        }
        if (addSpecificationButton.disabled == false) {
          addSpecificationButton.style.cursor = "pointer";
        } else {
          addSpecificationButton.style.cursor = "default";
        }
        if (addSpecificationButton.disabled == false) {
          const product = {
            id: +productId,
            name: productName,
            price: getCurrentPrice(productPrice),
            idMotrum: productMotrumId,
            idSaler: productSalerId,
            quantity: countQuantity,
            totalCost: (getCurrentPrice(productPrice) * countQuantity).toFixed(
              2
            ),
          };
          addSpecificationButton.onclick = () => {
            setProduct(product);
            if (localStorageSpecification) {
              specificationLinkContainerProductValue.textContent =
                localStorageSpecification.length;
            } else {
              specificationLinkContainerProductValue.textContent =
                productsSpecificationList.length;
            }
          };
        }
      };

      minusButton.onclick = () => {
        countQuantity--;
        countQuantityZone.textContent = countQuantity;

        if (countQuantity <= 0) {
          minusButton.disabled = true;
          addSpecificationButton.disabled = true;
        } else {
          minusButton.disabled = false;
          addSpecificationButton.disabled = false;
        }
        if (countQuantityZone.textContent.length <= 1) {
          countQuantityZone.style.left = "45.5%";
        }
        if (addSpecificationButton.disabled == false) {
          addSpecificationButton.style.cursor = "pointer";
        } else {
          addSpecificationButton.style.cursor = "default";
        }
        if (addSpecificationButton.disabled == false) {
          const product = {
            id: +productId,
            name: productName,
            price: getCurrentPrice(productPrice),
            idMotrum: productMotrumId,
            idSaler: productSalerId,
            quantity: countQuantity,
            totalCost: (getCurrentPrice(productPrice) * countQuantity).toFixed(
              2
            ),
          };
          addSpecificationButton.onclick = () => {
            setProduct(product);
            if (localStorageSpecification) {
              specificationLinkContainerProductValue.textContent =
                localStorageSpecification.length;
            } else {
              specificationLinkContainerProductValue.textContent =
                productsSpecificationList.length;
            }
          };
        }
      };

      const priceContainer = catalogItem.querySelector(".price");
      const price = priceContainer.querySelector(".price-count");

      if (price) {
        const priceNumberValue = getCurrentPrice(price.textContent);
        price.textContent = (+priceNumberValue).toLocaleString(undefined, {
          minimumFractionDigits: 2,
        });
      }
    });
  }
});
