<script setup>
    import {ref, computed, defineProps, defineEmits} from 'vue'
    import { useSimpleViewStore } from '@/stores/SimpleViewStore'

    const SimpleViewStore = useSimpleViewStore()
    const {cbIdx} = defineProps({
        cbIdx: {
            type: Number,
            required: true
        }
    })
    const emit = defineEmits([
        'done'
    ])
</script>

<template>
    <div class="popover-inner">
        <input type="number" min=3 max=999
            v-model="SimpleViewStore.colorbarData[cbIdx].steps"
        >
        <button type="submit" @click.prevent="emit('done')">OK</button>
    </div>
</template>

<style lang="sass">
    @use '@/assets/popovers' as *;
</style>
