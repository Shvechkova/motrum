import { getCookie } from "/static/core/js/functions.js";

let currentUrl = new URL(window.location.href);

window.addEventListener("DOMContentLoaded", () => {
  const catalogWrapper = document.querySelector('[catalog-elem="wrapper"]');
  if (catalogWrapper) {
    const category = document
      .querySelector("[data-category-id]")
      .getAttribute("data-category-id");
    const group = document
      .querySelector("[data-group-id]")
      .getAttribute("data-group-id");
    let productCount = 0;
    let pageCount = 0;
    let lastPage = 0;
    let paramsArray = [];
    const loader = catalogWrapper.querySelector(".loader");
    const btn = catalogWrapper.querySelector(".add_more");
    const catalogContainer = catalogWrapper.querySelector(
      '[catalog-elem="container"]'
    );

    // // let productsVendorId = "1";
    const smallLoader = catalogWrapper.querySelector(".small_loader");
    const endContent = catalogWrapper.querySelector(".end_content");
    const catalogButton = endContent.querySelector('[catalog-elem="button"]');
    const pagination = catalogWrapper.querySelector(".pagination");
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

    function loadItems(
      pagintaionFn = false,
      cleanArray = false,
      vendor = false
    ) {
      let data = {
        count: !pagintaionFn ? productCount : 10,
        sort: "+",
        page: !pagintaionFn ? "1" : pageCount,
        category: category,
        group: !group ? "" : group,
        vendor: !vendor ? "" : vendor,
      };

      let params = new URLSearchParams(data);

      let csrfToken = getCookie("csrftoken");
      fetch(`/api/v1/product/load-ajax-product-list/?${params.toString()}`, {
        method: "GET",
        headers: {
          "X-CSRFToken": csrfToken,
        },
      })
        .then((response) => response.json())
        .then(function (data) {
          lastPage = +data.count;
          paginationLastElem.textContent = `... ${lastPage}`;
          loader.style.display = "none";
          endContent.classList.add("show");
          smallLoader.classList.remove("show");

          for (let i in data.data) {
            addAjaxCatalogItem(data.data[i]);
          }
          if (data.next) {
            catalogButton.disabled = false;
            nextBtn.classList.add("show");
          } else {
            catalogButton.disabled = true;
            nextBtn.classList.remove("show");
          }
          const pagintationArray = [];

          for (
            let i = pageCount == 0 ? pageCount : pageCount - 1;
            !data.small ? i < pageCount + 2 : i <= pageCount;
            i++
          ) {
            pagintationArray.push(i);
          }
          if (cleanArray) {
            paginationElems.forEach((elem) => {
              elem.textContent = "";
            });
          }
          pagintationArray.forEach((el, i) => {
            paginationElems[i].textContent = +el + 1;
          });
          getActivePaginationElem();
        });
    }

    window.onload = () => {
      loadItems(false, false, false);
    };

    paginationFirstElem.onclick = () => {
      pageCount = 0;
      endContent.classList.remove("show");
      catalogContainer.innerHTML = "";
      loader.style.display = "block";
      loadItems(true, true, paramsArray.length > 0 ? paramsArray : false);
      productCount = pageCount * 10;
    };

    nextBtn.onclick = () => {
      pageCount += 1;
      endContent.classList.remove("show");
      catalogContainer.innerHTML = "";
      loader.style.display = "block";
      loadItems(true, false, paramsArray.length > 0 ? paramsArray : false);
      productCount = pageCount * 10;
    };

    paginationElems.forEach((elem) => {
      elem.onclick = () => {
        pageCount = +elem.textContent - 1;
        endContent.classList.remove("show");
        catalogContainer.innerHTML = "";
        loader.style.display = "block";
        loadItems(true, false, paramsArray.length > 0 ? paramsArray : false);
        productCount = pageCount * 10;
      };
    });
    catalogButton.onclick = () => {
      productCount += 10;
      pageCount++;
      endContent.classList.remove("show");
      smallLoader.classList.add("show");
      loadItems(false, false, paramsArray.length > 0 ? paramsArray : false);
    };

    paginationLastElem.onclick = () => {
      pageCount = lastPage - 1;
      endContent.classList.remove("show");
      catalogContainer.innerHTML = "";
      loader.style.display = "block";
      loadItems(true, true, paramsArray.length > 0 ? paramsArray : false);
      productCount = pageCount * 10;
    };

    function renderCatalogItem(productData) {
      let ajaxTemplateWrapper = document.querySelector(
        '[template-elem="wrapper"]'
      );
      let ajaxCatalogElementTemplate = ajaxTemplateWrapper.querySelector(
        '[catalog-elem="product-item"]'
      ).innerText;

      return nunjucks.renderString(ajaxCatalogElementTemplate, productData);
    }

    function addAjaxCatalogItem(ajaxElemData) {
      let renderCatalogItemHtml = renderCatalogItem(ajaxElemData);
      catalogContainer.insertAdjacentHTML("beforeend", renderCatalogItemHtml);
    }

    const filters = document.querySelectorAll(".filter_elem");
    filters.forEach((filterElem) => {
      const title = filterElem.querySelector(".filter_title");
      const filterContent = filterElem.querySelector(".filter-wrapper-content");
      const arrow = filterElem.querySelector(".arrow");
      const filterValues = filterElem.querySelectorAll(".filter_elem_content");

      filterValues.forEach((filterValue) => {
        const checkbox = filterValue.querySelector(".checked");
        const vendorParam = filterValue.getAttribute("param");
        filterValue.onclick = () => {
          paramsArray.push(vendorParam);
          checkbox.classList.toggle("show");
          if (checkbox.classList.contains("show")) {
            if (window.location.href.includes("?")) {
              currentUrl.searchParams.set("vendor", paramsArray.join());
              loader.style.display = "block";
              catalogContainer.innerHTML = "";
              endContent.classList.remove("show");
              pageCount = "1";
              loadItems(false, false, paramsArray);
            } else {
              currentUrl.searchParams.set("vendor", paramsArray.join(","));
              loader.style.display = "block";
              catalogContainer.innerHTML = "";
              endContent.classList.remove("show");
              pageCount = "1";
              loadItems(false, false, paramsArray);
            }
          } else {
            const searchParams = currentUrl.searchParams;
            const filteredParamsArray = paramsArray.filter(
              (el) => el !== vendorParam
            );
            paramsArray = filteredParamsArray;
            searchParams.set("vendor", paramsArray.join());
            loader.style.display = "block";
            catalogContainer.innerHTML = "";
            endContent.classList.remove("show");
            pageCount = "1";
            loadItems(false, true, paramsArray);
            if (filteredParamsArray.length == 0) {
              searchParams.delete("vendor", paramsArray.join());
              loader.style.display = "block";
              catalogContainer.innerHTML = "";
              endContent.classList.remove("show");
              loadItems(false, false, false);
            }
          }
          history.pushState({}, "", currentUrl);
        };
      });
      title.onclick = () => {
        filterContent.classList.toggle("is_open");
        arrow.classList.toggle("rotate");
      };
    });
  }
});