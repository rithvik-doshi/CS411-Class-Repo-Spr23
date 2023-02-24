<script lang="ts">
    import NavBar from "../components/NavBar.svelte";
    import "../app.css"
    import { currentUser } from "../stores/currentUser"
</script>

{#if $currentUser.userId != -1}
    <NavBar/>
{/if}
<slot></slot>
