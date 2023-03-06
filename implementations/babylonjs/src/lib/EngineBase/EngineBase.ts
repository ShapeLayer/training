import { Engine, Scene } from '@babylonjs/core';

class EngineBase {
  private _canvas: HTMLCanvasElement
  private _engine: Engine
  private _scene: Scene
  
  get canvas (): HTMLCanvasElement {
    return this._canvas
  }
  get engine (): Engine {
    return this._engine
  }
  get scene (): Scene {
    return this._scene
  }
  set scene (value: Scene) {
    this._scene = value
  }

  constructor (canvas: HTMLCanvasElement) {
    this._canvas = canvas
    this._engine = new Engine(this._canvas, true)
    this._scene = new Scene(this._engine)
  }

  EventHandler__OnMount (): void {
    this._engine.runRenderLoop(() => { this._scene.render() })
  }
  EventHandler__OnResize (): void {
    this._engine.resize()
  }
}

export { EngineBase }
