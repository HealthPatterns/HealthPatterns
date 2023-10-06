<script lang="ts">

    import { onMount } from "svelte";

    export let unixtime : number = 1696579823 * 1000;
    export let isRunning : boolean = false;

    var deltaTime = new Date(Math.abs(new Date().getTime() - new Date(unixtime).getTime()));

    let count = deltaTime.getMilliseconds(), hour = deltaTime.getUTCHours(), minute = deltaTime.getMinutes(), second = deltaTime.getSeconds();
    let hrString : string, minString : string, secString : string;

    createStrings();

    onMount (() => {
        if (isRunning) {
            stopWatch();
        }
    }) 


    export function start () {
        isRunning = true;
        //console.log(isRunning);
        stopWatch();
    }

    function stop () {
        isRunning = false;
    }

    function reset () {
        unixtime = new Date().getTime() / 1000;
    };

    export function stop_reset() {
        stop();
        reset();
    }

    function createStrings() {
        hrString = hour < 10 ? "0" + hour.toString() : hour.toString();
        minString = minute < 10 ? "0" + minute.toString() : minute.toString();
        secString = second < 10 ? "0" + second.toString() : second.toString();
    }

    function stopWatch() {
        if (isRunning) {
            deltaTime = new Date(Math.abs(new Date().getTime() - new Date(unixtime).getTime()));
            count = deltaTime.getMilliseconds(), hour = deltaTime.getUTCHours(), minute = deltaTime.getMinutes(), second = deltaTime.getSeconds();
            createStrings();

            setTimeout(stopWatch, 10);
        }
    }
</script>

<div class="circle"><p style="font-size: 3rem;">{hrString}:{minString}:{secString}</p></div>

<style>
    .circle {
        background-color: #F2F1E8;
        height: 50%;
        aspect-ratio: 1 / 1;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>