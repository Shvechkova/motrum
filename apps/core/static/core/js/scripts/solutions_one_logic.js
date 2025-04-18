import {
  showErrorValidation,
  maskOptions,
  getCookie,
  setPreloaderInButton,
  hidePreloaderAndEnabledButton,
} from "/static/core/js/functions.js";

import { setErrorModal } from "/static/core/js/error_modal.js";
import { successModal } from "/static/core/js/sucessModal.js";

const csrfToken = getCookie("csrftoken");

window.addEventListener("DOMContentLoaded", () => {
  const wrapper = document.querySelector(".solution_one_container");
  if (wrapper) {
    const slider = new Swiper(".solution_one_slider", {
      slidesPerView: "auto",
    });

    const palettScrollZoneContainer = wrapper.querySelector(
      ".palett_description"
    );

    // анимация при скролле
    // if (palettScrollZoneContainer) {
    //   const tab = document.querySelector(".chars_table");
    //   const palettAnimateElem = palettScrollZoneContainer.querySelector(
    //     ".palett_animate_scroll_up"
    //   );
    //   let deltaY = 0;
    //   let lastKnownScrollPosition = 0;
    //   let rotationValue = 0;
    //   document.onscroll = () => {
    //     let ticking = false;
    //     if (!ticking) {
    //       window.requestAnimationFrame(() => {
    //         deltaY = window.scrollY - lastKnownScrollPosition;
    //         lastKnownScrollPosition = window.scrollY;
    //         ticking = false;
    //       });
    //       ticking = true;
    //     }

    //     let charsScrollTop = tab.getBoundingClientRect().top;
    //     let scrollPosY = palettScrollZoneContainer.getBoundingClientRect().top;

    //     // let translateValue = -deltaY * -5;

    //     if (deltaY > 0) {
    //       rotationValue += -deltaY * 5;
    //       if (rotationValue <= -45) {
    //         rotationValue = -45;
    //       } else {
    //         if (rotationValue >= 0) {
    //           rotationValue = 0;
    //         }
    //       }
    //     } else {
    //       rotationValue -= deltaY * 5;
    //       if (rotationValue <= -45) {
    //         rotationValue = -45;
    //       } else {
    //         if (rotationValue >= 0) {
    //           rotationValue = 0;
    //         }
    //       }
    //     }

    //     if (scrollPosY < 200) {
    //       palettAnimateElem.style.transform = `rotate(${rotationValue}deg)`;
    //     }
    //   };
    // }
  }

  const formContainer = document.querySelector(".demo-form-container");
  if (formContainer) {
    const nameInput = formContainer.querySelector(".name_input");
    const nameError = formContainer.querySelector(".name_error");
    const phoneInput = formContainer.querySelector(".phone_input");
    const phoneError = formContainer.querySelector(".phone_error");
    const submitBtn = formContainer.querySelector(".btn");
    const overlay = document.querySelector(".anchor_overlay");

    const phoneMask = IMask(phoneInput, maskOptions);

    function hideOverlay() {
      if(overlay){
        if (
          overlay.classList.contains("show") ||
          overlay.classList.contains("visible")
        ) {
          overlay.classList.remove("visible");
          setInterval(() => {
            overlay.classList.remove("show");
          }, 600);
        }
      }
    }

    submitBtn.onclick = () => {
      let validate = true;
      if (!nameInput.value) {
        showErrorValidation("Обязательное поле", nameError);
        validate = false;
      }
      if (!phoneInput.value) {
        showErrorValidation("Обязательное поле", phoneError);
        validate = false;
      }
      if (phoneInput.value && phoneInput.value.length < 18) {
        showErrorValidation("Некорректный номер телефона", phoneError);
        validate = false;
      }

      function yandexMetrika() {
        if (submitBtn.getAttribute("btn-form-type") == "cobots_all") {
          ym(37794920, "reachGoal", "send_all_cobots_form");
        }
        if (submitBtn.getAttribute("btn-form-type") == "palett") {
          ym(37794920, "reachGoal", "send_form_palett");
        }
        if (submitBtn.getAttribute("btn-form-type") == "cobot-box") {
          ym(37794920, "reachGoal", "send_form_cobot_box");
        }
        if (submitBtn.getAttribute("btn-form-type") == "cobot-packing") {
          ym(37794920, "reachGoal", "send_form_cobot_packing");
        }
        if (submitBtn.getAttribute("btn-form-type") == "marking") {
          ym(37794920, "reachGoal", "send_form_marking_orange_form");
        }
        if (submitBtn.getAttribute("btn-form-type") == "shkaf") {
          ym(37794920, "reachGoal", "send_form_shkaf");
        }
      }

      if (validate) {
        const dataObj = {
          name: nameInput.value,
          phone: phoneMask.unmaskedValue,
          type: submitBtn.getAttribute("btn-type-cobots")
            ? submitBtn.getAttribute("btn-type-cobots")
            : "",
          url: window.location.href,
        };
        const data = JSON.stringify(dataObj);

        setPreloaderInButton(submitBtn);

        let endpoint;

        if (submitBtn.getAttribute("btn-type-cobots")) {
          endpoint = "/api/v1/core/forms/send-form-demo-visit/";
        }
        if (submitBtn.getAttribute("type-solution") == "shkaf") {
          endpoint = "/api/v1/core/forms/send-form-shkaf-upravleniya/";
        }
        if (submitBtn.getAttribute("type-solution") == "packing") {
          endpoint = "/api/v1/core/forms/send-form-cobots-packing/";
        }
        if (submitBtn.getAttribute("type-solution") == "marking") {
          endpoint = "/api/v1/core/forms/send-form-marking/";
        }

        function resetInputs() {
          phoneInput.value = "";
          nameInput.value = "";
        }

        fetch(endpoint, {
          method: "POST",
          body: data,
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
          },
        }).then((response) => {
          if (response.status >= 200 && response.status < 300) {
            yandexMetrika();
            resetInputs();
            hideOverlay();
            hidePreloaderAndEnabledButton(submitBtn);
            successModal(
              "Спасибо за заявку, мы свяжемся с вами в ближайшее время"
            );
          } else {
            setErrorModal();
            throw new Error("Ошибка");
          }
        });
      }
    };
  }
});
