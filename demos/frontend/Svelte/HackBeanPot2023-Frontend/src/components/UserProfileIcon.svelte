<script lang='ts'>
	import type { UserProps } from "../types";

    export let user: UserProps;
    let color = "blue"
    
</script>

<div class={
    `w-8 h-8
    flex justify-center items-center
    border-2
    rounded-full
    text-black 
    text-xl font-bold
    `
}
>
    {user.firstname.charAt(0)}
</div>