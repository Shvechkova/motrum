import { getCookie } from "/static/core/js/functions.js";

export function invoiceItem(container) {
  if (container) {
    const invoiceOverlay = document.querySelector(".invoice-overlay");
    const modalWindow = invoiceOverlay.querySelector(".modal-window");
    const invoiceContainer = modalWindow.querySelector(
      '[invoice-elem="container"]'
    );

    function loadInvoiceItems(specificationId) {
      let csrfToken = getCookie("csrftoken");
      fetch(`/api/v1/order/${specificationId}/get-specification-product/`, {
        method: "GET",
        headers: {
          "X-CSRFToken": csrfToken,
        },
      })
        .then((response) => response.json())
        .then(function (data) {
          for (let i in data) {
            addAjaxCatalogItem(data[i]);
          }
        });
    }
    function renderCatalogItem(orderData) {
      let ajaxTemplateWrapper = document.querySelector(
        '[template-elem="wrapper"]'
      );
      let ajaxCatalogElementTemplate = ajaxTemplateWrapper.querySelector(
        '[invoice-elem="invoice-item"]'
      ).innerText;

      return nunjucks.renderString(ajaxCatalogElementTemplate, orderData);
    }

    function addAjaxCatalogItem(ajaxElemData) {
      let renderCatalogItemHtml = renderCatalogItem(ajaxElemData);
      invoiceContainer.insertAdjacentHTML("beforeend", renderCatalogItemHtml);
    }

    if (container) {
      const interval = setInterval(() => {
        const specificationsItems = container.querySelectorAll(
          ".specification_item"
        );
        if (specificationsItems.length > 0) {
          clearInterval(interval);
          specificationsItems.forEach((specificationItem) => {
            const createInvoiceContainer = specificationItem.querySelector(
              ".invoice-table_item_value"
            );
            const invoiceBtn = createInvoiceContainer.querySelector(
              ".create-bill-button"
            );
            const invoiceLink =
              createInvoiceContainer.querySelector(".invoice-link");

            const specificationId =
              specificationItem.getAttribute("specification-id");
            if (invoiceBtn) {
              function openInvoiceModal() {
                invoiceOverlay.classList.add("show");
                document.body.style.overflowY = "hidden";
                setTimeout(() => {
                  invoiceOverlay.classList.add("visible");
                }, 600);
                loadInvoiceItems(specificationId);

                const interval = setInterval(() => {
                  const invoiceItems =
                    invoiceContainer.querySelectorAll(".invoice-item");
                  if (invoiceItems.length > 0) {
                    clearInterval(interval);
                    const createInvoiceBtn =
                      modalWindow.querySelector(".invoice-btn");
                    createInvoiceBtn.onclick = () => {
                      let validate = true;
                      const inputs = modalWindow.querySelectorAll(
                        ".invoice-data-input"
                      );
                      for (let i = 0; i < inputs.length; i += 1) {
                        if (!inputs[i].value) {
                          validate = false;
                          break;
                        }
                      }
                      if (validate == true) {
                        const csrfToken = getCookie("csrftoken");
                        const dataArray = [];
                        invoiceItems.forEach((el) => {
                          const id = el.getAttribute("invoice-elem-id");
                          const value = el.querySelector(
                            ".invoice-data-input"
                          ).value;

                          const dataObject = {
                            id: id,
                            text_delivery: value,
                          };
                          dataArray.push(dataObject);
                        });

                        const data = JSON.stringify(dataArray);

                        fetch(
                          `/api/v1/order/${specificationId}/create-bill-admin/`,
                          {
                            method: "UPDATE",
                            headers: {
                              "Content-Type": "application/json",
                              "X-CSRFToken": csrfToken,
                            },
                            body: data,
                          }
                        )
                          .then((response) => {
                            if (response.status === 200) {
                              return response.json();
                            } else {
                              throw new Error("Ошибка");
                            }
                          })
                          .then((response) => {
                            invoiceOverlay.classList.remove("visible");
                            if (invoiceOverlay.classList.contains("show")) {
                              document.body.style.overflowY = "scroll";
                            }
                            setTimeout(() => {
                              invoiceOverlay.classList.remove("show");
                              invoiceContainer.innerHTML = "";
                            }, 600);
                            if (!invoiceLink) {
                              invoiceBtn.classList.add("changed");
                              invoiceBtn.textContent = "Обновить счет";
                              const link =
                                specificationItem.querySelector(
                                  ".invoice-link"
                                );
                              if (link) {
                                link.remove();
                              }
                              createInvoiceContainer.innerHTML += `<a class="invoice-link" href='${response.pdf}'>Счет ссылка</a>`;

                              const btn =
                                specificationItem.querySelector(".changed");
                              btn.onclick = () => openInvoiceModal();
                            } else {
                              invoiceBtn.classList.add("changed");
                              invoiceBtn.textContent = "Обновить счет";
                              const link =
                                specificationItem.querySelector(
                                  ".invoice-link"
                                );
                              link.remove();
                              createInvoiceContainer.innerHTML += `<a class="invoice-link" href='${response.pdf}'>Счет ссылка</a>`;
                              const btn =
                                specificationItem.querySelector(".changed");
                              btn.onclick = () => openInvoiceModal();
                            }
                          });
                      }
                    };
                  }
                });
              }
              invoiceBtn.onclick = () => openInvoiceModal();
              invoiceOverlay.onclick = () => {
                invoiceOverlay.classList.remove("visible");
                if (invoiceOverlay.classList.contains("show")) {
                  document.body.style.overflowY = "scroll";
                }
                setTimeout(() => {
                  invoiceOverlay.classList.remove("show");
                  invoiceContainer.innerHTML = "";
                }, 600);
              };
              modalWindow.onclick = (e) => {
                e.stopPropagation();
              };
            }
          });
        }
      });
    }
  }
}

window.addEventListener("DOMContentLoaded", () => {
  const specificationContainer = document.querySelector(
    ".specification_container"
  );
  invoiceItem(specificationContainer);
});