<script lang="ts">
    import head from "../../src/assets/head.svg"
    import upperShoulderLeft from "../../src/assets/upper_shoulder_left.svg"
    import neck from "../../src/assets/neck.svg"
    import upperShoulderRight from "../../src/assets/upper_shoulder_right.svg"

    import chest from "../../src/assets/chest.svg"
    import lower_torso_left from "../../src/assets/lower_torso_left.svg"
    import lower_torso_mid from "../../src/assets/lower_torso_mid.svg"
    import lower_torso_right from "../../src/assets/lower_torso_right.svg"
  </script>
  
  <main class="flex grow-0 flex-col justify-center">
    <img src={head} alt="test"/>  
    <div id="neck" class="flex flex-row gap-1 justify-center">
      <img src={upperShoulderLeft} alt="test"/>  
      <img src={neck} alt="test"/>  
      <img src={upperShoulderRight} alt="test"/>  
    </div>

    <div id="turso" class="flex flex-col gap-1 justify-center">
      <img src={chest} alt="test"/>  
      <div id="lower-torso relative" class="flex flex-row gap-1 justify-center">
        <img class="absolute left-0 top-0" src={lower_torso_left} alt="test"/>  
        <img src={lower_torso_mid} alt="test"/>  
        <img src={lower_torso_right} alt="test"/>  
      </div>
    </div>

  </main>
  
  
  
  
  
  <style>
  </style>