<script setup>
    import {ref, defineModel, useId} from 'vue'

    import Icon from '@/components/Icon.vue'

    const value = defineModel()
    const id = useId()
</script>

<template>
    <label :for="id">
    <input type="checkbox" v-model="value" :id="id">
        <Icon name="check" class="checkbox-check" :class="{ 'active': value }" />
        <slot></slot>
    </label>
</template>

<style lang="scss" scoped>
    @use '@/assets/variables' as *;

    input {
        appearance: none;
        width: 20px; height: 20px;
        margin-right: 5px;
        color: $accent-dark;
        border: 2px solid $white_80; border-radius: $BR_regular;
        box-shadow: inset 0 0 0 0px $white;
        transition: $TR_regular;

        &:hover {
            background-color: $white_30;
            border-color: $white_80;

            &:active {
                background-color: $white_50;
                border-color: $white;
                box-shadow: inset 0 0 0 2px $white;
                // transition: $TR_fast;
            }
        }

        &:checked {
            background-color: $white_80;
            border-color: $trans;

            &:hover {
                background-color: $white;

                &:active {
                    background-color: $white_80;
                    border-color: $accent-dark_25;
                    box-shadow: inset 0 0 0 2px $accent-dark_25;
                }
            }
        }
    }

    .checkbox-check {
        position: absolute;
        left: 2px;
        color: $trans;
        transition: $TR_regular;
        opacity: .8;

        &.active {
            color: $accent-dark;
        }
    }

    label {
        @include flex-center;
        position: relative;
        font-weight: $FW_bold;
        user-select: none;
    }
</style>
