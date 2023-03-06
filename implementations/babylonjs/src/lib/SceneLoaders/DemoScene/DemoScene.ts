import { 
  Engine, 
  Scene, 
  ArcRotateCamera, 
  Vector3, 
  HemisphericLight, 
  Mesh, 
  MeshBuilder,
  Color4
} from '@babylonjs/core'

class DemoScene {
  private _canvas: HTMLCanvasElement
  private _engine: Engine
  private _scene: Scene

  constructor (canvas: HTMLCanvasElement, engine: Engine, scene: Scene) {
    this._canvas = canvas
    this._engine = engine
    this._scene = scene
  }

  EventHandler__OnMount (): void {
    this.BuildScene()
  }

  BuildScene (): void {
    // Set camera
    let camera: ArcRotateCamera = new ArcRotateCamera('Camera', Math.PI / 2, Math.PI / 2, 2, Vector3.Zero(), this._scene)
    camera.attachControl(this._canvas, true)
    console.log(this._scene)
    this._scene.clearColor = new Color4(.1, .1, .1, 1)
    
    let light1: HemisphericLight = new HemisphericLight('Light1', new Vector3(1, 1, 0), this._scene)
  
    let sphere: Mesh = MeshBuilder.CreateSphere('sphere', { diameter: 1 }, this._scene)
  }
}
export { DemoScene }
