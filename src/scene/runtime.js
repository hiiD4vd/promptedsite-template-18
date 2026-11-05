import {LoadingManager,TextureLoader} from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader.js';
import {DRACOLoader} from 'three/examples/jsm/loaders/DRACOLoader.js';
import {gsap} from 'gsap';
export const state={sliderActiveIndex:0,sliderSwipeDirection:1,isThreeSliderLoaded:false,isThreeScrollLoaded:false,setThreeSliderLoaded(){this.isThreeSliderLoaded=true},setThreeScrollLoaded(){this.isThreeScrollLoaded=true}};
const manager=new LoadingManager();const draco=new DRACOLoader(manager).setDecoderPath('/draco/');const gltf=new GLTFLoader(manager).setDRACOLoader(draco);
export const runtime=()=>({$gsap:gsap,$loadingManager:manager,$gltfLoader:gltf,$dracoLoader:draco,$textureLoader:new TextureLoader(manager)});
