<script setup>
    import {ref, defineProps} from 'vue'
    import { useSimpleViewStore } from '@/stores/SimpleViewStore'

    import SlottedButton from '@/components/SlottedButton.vue'

    const SimpleViewStore = useSimpleViewStore()
    const {value, bg} = defineProps({
        value: {
            type: Number,
            required: true
        },
        bg: {
            type: Array,
            required: true
        }
    })
</script>

<template>  
    <section class="colorbar__len-segment" :style="{
        'flex': value,
        'background': (`linear-gradient( 
        ${SimpleViewStore.blockDataCfg.useCIELAB ? 'in lab' : ''}
        90deg, ${bg[0]}, ${bg[1]})`)
    }">
        <SlottedButton class="trans">
            <span class="colorbar__len-segment__count">
                {{ value || 'missingNo' }}
            </span>
            <span class="colorbar__len-segment__appendix">
                blocks
            </span>
        </SlottedButton>
    </section>
</template>

<style lang="scss" scoped>
    @use '@/assets/variables' as *;

    .colorbar__len-segment {
        @include flex-center;
        flex: 1;
        container-type: inline-size;

        @container (max-width: 75px) {
            .colorbar__len-segment__appendix {
                display: none;
            }
        }

        & button.trans {
            flex: 1;
            margin: 0 4px;
            text-shadow: $SH_subtle;
        }
    }
</style>
