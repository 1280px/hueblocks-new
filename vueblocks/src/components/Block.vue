<script setup>
    import {ref, computed, defineProps} from 'vue'
    import { useGlobalStore } from '@/stores/GlobalStore'
    
    const GlobalStore = useGlobalStore()
    const {blocksetIdx, texture, name} = defineProps({
        blocksetIdx: {
            type: Number,
            required: true,
            default: 'missingNo'
        },
        texture: {
            type: String,
            required: true,
            default: 'missingNo'
        },
        name: {
            type: String,
            required: false
        }
    })

    // We only want to show background when image is not loaded,
    // so textrues with alpha channel will show up normally:
    const isLoaded = ref(false)
</script>

<template>
    <div :class="{ 'loading': !isLoaded }" class="block"
        :style="{'width': GlobalStore?.blockSize || '64px', 'height': GlobalStore?.blockSize || '64px'}"
    >
        <img v-show="isLoaded" @load="isLoaded = true" @error="isLoaded = false"
            :src="GlobalStore.getTexturePath(blocksetIdx, texture)" :alt="name"
        >
        <span v-show="!isLoaded">{{ name || texture || 'Error!' }}</span>
    </div>
</template>

<style lang="scss" scoped>
    @use '@/assets/variables' as *;

    .block {
        image-rendering: pixelated;
        overflow: clip; line-break: anywhere;
        text-align: left;

        &.loading {
            background-color: $accent-light_25;
        }

        & img {
            height: 100%;
        }
    }
</style>
