<script lang="ts">
    import BodyForm from "./BodyForm.svelte";
    import Food from "./Food.svelte";
    import Slider from "./Slider.svelte";
</script>

<div id="AddDetails">
    <h1 style="margin-top: 20px;">Details hinzufügen</h1>
    <h2>Körperregionen</h2>
    <div style="height: 70%;"><BodyForm></BodyForm></div>
    <h2>Intensität</h2>
    <Slider></Slider>
    <h2>Ernährung</h2>
    <Food></Food>
</div>

<style>

#AddDetails {
    display: flex;
    height: 90%;
    width: 80%;
    flex-direction: column;
}

h1 {
    font-size: x-large;
    font-weight: 500;
    margin-bottom: 0.6em;
}

h2 {
    font-size: large;
    font-weight: 500;
}

</style>