<template>
    <main>
    <div class="container">
        <div>
            <h1 style="text-align: center; margin-top: 2rem; margin-bottom: 2rem"> {{ msg }}</h1>
        </div>
        <form style="text-align: center;" @submit.prevent="handleSubmitForm">
            <div style="text-align: center">
                <h2>Enter Phone Number</h2>
            </div>
            <input type="tel" required style="width: 50%" @keydown="reviewKey" v-model="phoneNumber">
            <p v-if="error" style="color: red">
                Phone number must be 10 digits.
            </p>
        </form>
    </div>
    </main>
</template>

<script>

export default {
    name: 'Home',
    data() {
        return {
            msg : "Welcome to The Living Legacy Center",
            phoneNumber: null,
            acceptedKeys: [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "Backspace",
                "Delete",
                "ArrowLeft",
                "ArrowRight",
                "Enter"
            ],
            error: false
        }
    },
    methods: {
        handleSubmitForm() {
            const phoneNumberRegex = /^\d{10}$/; // regular expression to match 10 digits
            if (phoneNumberRegex.test(this.phoneNumber)) {
                this.error = false
                alert('Submitted');
            } else {
                this.error = true
            }
        },
        reviewKey(e) {
            console.log(e)
            if (!this.acceptedKeys.includes(e.key)) {
                e.preventDefault()
            }
        }
    }
}
</script>

<style>
.container {
  margin: auto;

}
</style>