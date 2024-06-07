const { createApp } = Vue;

    createApp({
        mounted() {
            this.slider = this.$refs.slider;
        },
        methods: {
            scrollLeft() {
                this.slider.scrollBy({ left: -this.slider.clientWidth, behavior: 'smooth' });
            },
            scrollRight() {
                this.slider.scrollBy({ left: this.slider.clientWidth, behavior: 'smooth' });
            },
            alertWaiting(){
                alert("hui");
            }
        }

    }).mount('#app');