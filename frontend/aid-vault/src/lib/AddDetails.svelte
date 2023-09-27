<script lang="ts">
    import BodyForm from "./BodyForm.svelte";
    import Food from "./Food.svelte";
    import Slider from "./Slider.svelte";
</script>

<div id="AddDetails">
    <h1 style="margin-top: 3rem;">Details hinzufügen</h1>
    <div class="background-container" style="height: 70%;">
        <h2>Körperregionen</h2>
        <BodyForm></BodyForm>
    </div>

    <div class="background-container">
        <h2>Intensität</h2>
        <Slider></Slider>
    </div>
    
    <div style="margin-bottom: 0.2rem;" class="background-container">
        <h2>Ernährung</h2>
        <Food></Food>
    </div>
</div>

<style>

#AddDetails {
    display: flex;
    height: 98%;
    width: 95%;
    flex-direction: column;
    overflow: scroll;
    border-radius: 0.2rem;
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

.background-container {
    background-color: #fff;
    margin-bottom: 0.6rem;
    border-radius: 0.2rem;
    padding: 0.5rem;
}

</style>