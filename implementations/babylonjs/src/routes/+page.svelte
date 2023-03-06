<script lang="ts">
// https://doc.babylonjs.com/guidedLearning/createAGame/gettingSetUp
// https://doc.babylonjs.com/features/introductionToFeatures/chap1/first_scene

import '@babylonjs/core/Debug/debugLayer'
import '@babylonjs/inspector'
import '@babylonjs/loaders/glTF'
import { EngineBase } from '$lib/EngineBase'
import { Engine, Scene, ArcRotateCamera, Vector3, HemisphericLight, Mesh, MeshBuilder } from '@babylonjs/core'
import { onMount } from 'svelte'
import { DemoScene } from '$lib/SceneLoaders/DemoScene'

let canvas: HTMLCanvasElement

onMount(() => {
  const engineBase = new EngineBase(canvas)
  const engine: Engine = engineBase.engine
  const scene: Scene = engineBase.scene

  engineBase.EventHandler__OnMount()

  let sceneLoader: DemoScene = new DemoScene(canvas, engine, scene)
  sceneLoader.BuildScene()
})

const EventHandler__OnResize = (e: Event) => {
  engineBase.EventHandler__OnResize()
}

const EventHandler__OnKeyDown = (e: KeyboardEvent) => {
  if (e.shiftKey && e.ctrlKey && e.altKey && e.key === 'i') {
    if (scene.debugLayer.isVisible()) scene.debugLayer.hide()
    else scene.debugLayer.show()
  }
}
</script>

<svelte:window
  on:resize={ EventHandler__OnResize }
  on:keydown={ EventHandler__OnKeyDown }
/>

<canvas bind:this={canvas}></canvas>

<style lang="scss">
  canvas {
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
</style>
