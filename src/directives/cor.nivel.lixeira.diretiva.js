

export const vCorNivelLixeira = {

    lang: "js",
    setup() {




    },



    mounted(el, binding) {

        if (binding.value < 30) {

            el.children[2].style.backgroundColor = 'green';

        } else if (binding.value >= 30 && binding.value < 60) {

            el.children[2].style.backgroundColor = 'yellow';

        } else {

            el.children[2].style.backgroundColor = 'red';

        }



    },

    updated(el, binding) {

        if (binding.value < 30) {

            el.children[2].style.backgroundColor = 'green';

        } else if (binding.value >= 30 && binding.value < 60) {

            el.children[2].style.backgroundColor = 'yellow';

        } else {

            el.children[2].style.backgroundColor = 'red';

        }

    }


}