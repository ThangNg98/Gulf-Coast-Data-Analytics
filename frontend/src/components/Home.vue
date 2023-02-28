<template>
    <main>
    <div>
        <h1 style="text-align: center"> {{ msg }}</h1>
        <p style="text-align:center"> Create a user below </p>
    </div>
    <div style="text-align:center"> 
        <form>
            <label for="fname">First name:</label><br>
            <input type="text" id="fname" name="fname"><br>
            <label for="lname">Last name:</label><br>
            <input type="text" id="lname" name="lname"><br>
            <label for="phone">Phone:</label><br>
            <input type="text" id="phone" name="phone"> <br><br>
            <input type="submit" value="Submit">

        </form>
    </div>
    </main>
</template>

<script>

export default {
    name: 'Home',
    data() {
        return {
            msg : "Welcome to The Living Legacy Center"
        }

    }
}
</script>