import {render} from 'solid-js/web';
import {Component} from 'solid-js';
import {Application} from 'pixi.js';
import {ICanvas} from "pixi.js";

console.log("Hello World! main.tsx loaded.");

const MyTsComponent: Component = () => {
  return (
    <div>
      <h1>This is a typescript component</h1>
      <h2>This is part of a typescript component, too</h2>
    </div>
  );
};



const canvas = document.getElementById("pixi-canvas") as HTMLCanvasElement;

const app: Application<ICanvas> = new Application({
    view: canvas,
    resolution: window.devicePixelRatio || 1,
    autoDensity: true,
    backgroundColor: 0x333333,
    width: 1024,
    height: 768,
});

app;

render(() => <MyTsComponent />, document.getElementById('app')!);
