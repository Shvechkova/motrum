import { getCookie, showErrorValidation } from "/static/core/js/functions.js";
import { invoiceItem } from "../js/invoice_elems.js";
import { changePayment } from "../js/change_payment.js";

window.addEventListener("DOMContentLoaded", () => {
  const specificationWrapper = document.querySelector(
    '[specification-elem="wrapper"]'
  );
  if (specificationWrapper) {
    const allSpecifications = document.querySelector(
      ".all_specifications_table"
    );
    const specificationContainer = specificationWrapper.querySelector(
      '[specification-elem="container"]'
    );
    let specificationCount = 0;
    let pageCount = 0;
    let lastPage = 0;
    const loader = document.querySelector(".loader");
    const smallLoader = specificationWrapper.querySelector(".small_loader");
    const endContent = specificationWrapper.querySelector(".end_content");
    const catalogButton = endContent.querySelector('[project-elem="button"]');
    const pagination = endContent.querySelector(".pagination");
    const paginationElems = pagination.querySelectorAll(".elem");
    const paginationFirstElem = pagination.querySelector(".first");
    const paginationLastElem = pagination.querySelector(".last");
    const nextBtn = pagination.querySelector(".next");

    function getActivePaginationElem() {
      for (let i = 0; i < paginationElems.length; i++) {
        if (paginationElems[i].textContent == pageCount + 1) {
          paginationElems[i].classList.add("active");
        } else {
          paginationElems[i].classList.remove("active");
        }
      }
      showFirstPagintationElem();
    }

    function showFirstPagintationElem() {
      if (pageCount >= 2) {
        paginationFirstElem.classList.add("show");
      } else {
        paginationFirstElem.classList.remove("show");
      }
      if (pageCount >= lastPage - 2) {
        paginationLastElem.classList.remove("show");
        if (pageCount == lastPage - 1) {
          paginationElems[2].style.display = "none";
        } else {
          paginationElems[2].style.display = "block";
        }
      } else {
        paginationLastElem.classList.add("show");
      }
    }

    let csrfToken = getCookie("csrftoken");

    function loadItems(
      pagintaionFn = false,
      cleanArray = false,
      addMoreBtn = false,
      specification = false
    ) {
      let data = {
        count: !pagintaionFn ? specificationCount : 0,
        page: pageCount,
        addMoreBtn: addMoreBtn ? true : false,
        specification: specification ? "+" : null,
      };
      let params = new URLSearchParams(data);

      fetch(
        `/api/v1/order/load-ajax-specification-list/?${params.toString()}`,
        {
          method: "GET",
          headers: {
            "X-CSRFToken": csrfToken,
          },
        }
      )
        .then((response) => response.json())
        .then(function (data) {
          console.log(data);
          loader.classList.add("hide");
          smallLoader.classList.remove("show");
          lastPage = +data.count;
          const pagintationArray = [];
          paginationLastElem.textContent = `... ${lastPage}`;
          endContent.classList.add("show");

          for (let i in data.data) {
            addAjaxCatalogItem(data.data[i]);
            const currentSpecificatons =
              allSpecifications.querySelectorAll(".table_item");
            currentSpecificatons.forEach((item) => {
              const changeButton = item.querySelector(
                ".change-specification-button"
              );
              const updateButton = item.querySelector(
                ".uptate-specification-button"
              );
              const link = item.querySelector("a");
              const specificationId = item.getAttribute("specification-id");
              const cartId = +link.dataset.cartId;

              function uptadeOrChanegeSpecification(button) {
                button.onclick = () => {
                  button.setAttribute("text-content", button.textContent);
                  button.disabled = true;
                  button.textContent = "";
                  button.innerHTML = "<div class='small_loader'></div>";
                  document.cookie = `cart=${cartId};path=/`;
                  document.cookie = `specificationId=${specificationId};path=/`;
                  const endpoint = `/api/v1/order/${cartId}/update-order-admin/`;
                  fetch(endpoint, {
                    method: "UPDATE",
                    headers: {
                      "Content-Type": "application/json",
                      "X-CSRFToken": csrfToken,
                    },
                  })
                    .then((response) => response.json())
                    .then((response) => {
                      window.location.href =
                        "/admin_specification/current_specification/";
                      setTimeout(() => {
                        button.disabled = false;
                        button.innerHTML = "";
                        button.textContent =
                          button.getAttribute("text-content");
                      }, 3000);
                    });
                };
              }
              if (changeButton) {
                uptadeOrChanegeSpecification(changeButton);
              }
              if (updateButton) {
                uptadeOrChanegeSpecification(updateButton);
              }
            });
          }

          if (data.next) {
            catalogButton.disabled = false;
            nextBtn.classList.add("show");
          } else {
            catalogButton.disabled = true;
            nextBtn.classList.remove("show");
          }

          if (data.small) {
            nextBtn.classList.remove("show");
          }
          for (
            let i = pageCount == 0 ? pageCount : pageCount - 1;
            !data.small
              ? i < pageCount + 2
              : +data.count > 1
              ? i <= pageCount + 1
              : i <= pageCount;
            i++
          ) {
            pagintationArray.push(i);
          }
          if (cleanArray) {
            paginationElems.forEach((elem) => {
              elem.textContent = "";
            });
          }
          paginationElems.forEach((el) => (el.textContent = ""));
          pagintationArray.forEach((el, i) => {
            if (paginationElems[i]) {
              paginationElems[i].textContent = +el + 1;
            }
          });
          getActivePaginationElem();
          invoiceItem(specificationContainer);
          changePayment(specificationContainer, showErrorValidation);
        });
    }

    window.onload = () => {
      loadItems(false, false, false, false);
    };

    paginationFirstElem.onclick = () => {
      pageCount = 0;
      endContent.classList.remove("show");
      specificationContainer.innerHTML = "";
      loader.classList.remove("hide");
      specificationCount = pageCount * 10;
      loadItems(true, true, false, false);
    };
    nextBtn.onclick = () => {
      pageCount += 1;
      endContent.classList.remove("show");
      specificationContainer.innerHTML = "";
      loader.classList.remove("hide");
      specificationCount = pageCount * 10;
      loadItems(false, false, false, false);
    };
    paginationElems.forEach((elem) => {
      elem.onclick = () => {
        pageCount = +elem.textContent - 1;
        specificationContainer.innerHTML = "";
        endContent.classList.remove("show");
        loader.classList.remove("hide");
        specificationCount = pageCount * 10;
        loadItems(false, false, false, false);
      };
    });

    catalogButton.onclick = () => {
      specificationCount += 10;
      +pageCount++;
      endContent.classList.remove("show");
      smallLoader.classList.add("show");
      loadItems(false, false, true, false);
    };

    paginationLastElem.onclick = () => {
      pageCount = lastPage - 1;
      endContent.classList.remove("show");
      specificationContainer.innerHTML = "";
      loader.classList.remove("hide");
      specificationCount = pageCount * 10;
      loadItems(false, true, false, false);
    };

    function renderCatalogItem(orderData) {
      let ajaxTemplateWrapper = document.querySelector(
        '[template-elem="wrapper"]'
      );
      let ajaxCatalogElementTemplate = ajaxTemplateWrapper.querySelector(
        '[specification-elem="specification-item"]'
      ).innerText;

      return nunjucks.renderString(ajaxCatalogElementTemplate, orderData);
    }

    function addAjaxCatalogItem(ajaxElemData) {
      let renderCatalogItemHtml = renderCatalogItem(ajaxElemData);
      specificationContainer.insertAdjacentHTML(
        "beforeend",
        renderCatalogItemHtml
      );
    }
    const allSpecificationsContainer = document.querySelector(
      ".all_specifications_container"
    );
    if (allSpecificationsContainer) {
      let currentUrl = new URL(window.location.href);

      const titles = allSpecificationsContainer.querySelector(".title");
      const ordersWithoutSpecification = titles.querySelector(
        ".orders_without_specifications"
      );
      const titleItems = titles.querySelectorAll("span");
      const smallAllSpecificationTitles =
        allSpecificationsContainer.querySelector(".all_specifications_titles");
      const smallNoSpecificationTitles =
        allSpecificationsContainer.querySelector(".no_specification_titles");
      const searchParams = currentUrl.searchParams;

      for (let i = 0; i < titleItems.length; i++) {
        titleItems[i].onclick = () => {
          if (!titleItems[i].classList.contains("active")) {
            titleItems[i].classList.add("active");
            if (titleItems[i - 1]) {
              titleItems[i - 1].classList.remove("active");
            } else {
              titleItems[i + 1].classList.remove("active");
            }
          } else {
            return;
          }

          if (ordersWithoutSpecification.classList.contains("active")) {
            searchParams.set("specification", "+");
            history.pushState({}, "", currentUrl);
            pageCount = 0;
            smallAllSpecificationTitles.classList.remove("show");
            smallNoSpecificationTitles.classList.add("show");
            endContent.classList.remove("show");
            specificationContainer.innerHTML = "";
            loader.classList.remove("hide");
            specificationCount = pageCount * 10;
            loadItems(false, false, false, true);
          } else {
            searchParams.delete("specification");
            history.pushState({}, "", currentUrl);
            pageCount = 0;
            smallAllSpecificationTitles.classList.add("show");
            smallNoSpecificationTitles.classList.remove("show");
            endContent.classList.remove("show");
            specificationContainer.innerHTML = "";
            loader.classList.remove("hide");
            specificationCount = pageCount * 10;
            loadItems(false, false, false, false);
          }
        };
      }
    }
  }
});
