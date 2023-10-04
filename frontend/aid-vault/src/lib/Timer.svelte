<script lang="ts">

    let unixtime : Number;

    let timer : any;

    let count = 0, hour = 0;
    let minute = 0;
    let second = 0;

    let hrString : string, minString : string, secString : string, countString : string;

    createStrings();

    export function start () {
        timer = true;
        stopWatch();
    }

    function stop () {
        timer = false;
    }

    function reset () {
        timer = false;
        hour = 0;
        minute = 0;
        second = 0;
        count = 0
    };

    export function stop_reset() {
        stop();
        reset();
    }

    function createStrings() {
        hrString = hour.toString();
        minString = minute.toString();
        secString = second.toString();
        countString = count.toString();

        if (hour < 10) {
            hrString = "0" + hrString;
        }

        if (minute < 10) {
            minString = "0" + minString;
        }

        if (second < 10) {
            secString = "0" + secString;
        }

        if (count < 10) {
            countString = "0" + countString;
        }
    }

    function stopWatch() {
        if (timer) {
            count++;

            if (count == 100) {
                second++;
                count = 0;
            }

            if (second == 60) {
                minute++;
                second = 0;
            }

            if (minute == 60) {
                hour++;
                minute = 0;
                second = 0;
            }

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