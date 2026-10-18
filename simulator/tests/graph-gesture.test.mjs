import test from 'node:test';
import assert from 'node:assert/strict';
import {createGraphGesture} from '../graph-gesture.js';

function fixture({captureFails=false}={}) {
 const captures=new Set, moves=[], ends=[], states=[];
 const canvas={setPointerCapture(id){if(captureFails)throw Error('revoked');captures.add(id)},hasPointerCapture:id=>captures.has(id),releasePointerCapture(id){captures.delete(id)}};
 const gesture=createGraphGesture(canvas,{move:(...args)=>moves.push(args),finish:(...args)=>ends.push(args),active:on=>states.push(on)});
 return {gesture,captures,moves,ends,states};
}
const event=(changes={})=>({pointerId:7,button:0,buttons:1,isPrimary:true,clientX:100,clientY:100,prevented:false,preventDefault(){this.prevented=true},...changes});

test('left down prevents native selection and captures the stable canvas',()=>{const f=fixture(),e=event();assert(f.gesture.begin(e,{type:'node'}));assert(e.prevented);assert(f.captures.has(7));assert.deepEqual(f.states,[true])});
test('right click and nonprimary pointers never start graph gestures',()=>{for(const e of [event({button:2}),event({isPrimary:false})]){const f=fixture();assert.equal(f.gesture.begin(e,{}),false);assert.equal(f.gesture.current,null);assert(!e.prevented)}});
test('another pointer cannot replace, move or release the active pointer',()=>{const f=fixture();f.gesture.begin(event(),{type:'pan'});assert.equal(f.gesture.begin(event({pointerId:8}),{}),false);f.gesture.move(event({pointerId:8}));f.gesture.end(event({pointerId:8,buttons:0}));assert.equal(f.moves.length,0);assert(f.gesture.current)});
test('slow movement accumulates distance from origin and release ends once',()=>{const f=fixture();f.gesture.begin(event(),{type:'node'});for(let x=101;x<=120;x++)f.gesture.move(event({clientX:x}));assert.equal(f.moves.length,20);assert(f.gesture.current.moved);assert.equal(f.moves.at(-1)[1],20);const up=event({buttons:0,clientX:120});f.gesture.end(up);f.gesture.end(up);assert.equal(f.ends.length,1);assert.equal(f.gesture.current,null);assert.equal(f.captures.size,0);assert(up.prevented)});
test('movement after release cannot move nodes or the camera',()=>{const f=fixture();f.gesture.begin(event(),{type:'pan'});f.gesture.end(event({buttons:0}));f.gesture.move(event({clientX:400,buttons:0}));assert.equal(f.moves.length,0)});
test('missing pointerup is recovered by the actual left-button state',()=>{const f=fixture();f.gesture.begin(event(),{type:'node'});f.gesture.move(event({clientX:600,buttons:0}));assert.equal(f.moves.length,0);assert.equal(f.gesture.current,null);assert.equal(f.ends[0][2],'buttons-released')});
test('holding only the right button cannot prolong a left drag',()=>{const f=fixture();f.gesture.begin(event(),{});f.gesture.move(event({buttons:2}));assert.equal(f.gesture.current,null)});
test('releasing right button while left is held preserves the left drag',()=>{const f=fixture();f.gesture.begin(event(),{});f.gesture.end(event({button:2,buttons:1}));assert(f.gesture.current)});
for(const reason of ['cancel','capture-lost','blur','hidden','escape','render'])test(reason+' clears capture and active state exactly once',()=>{const f=fixture();f.gesture.begin(event(),{type:'pin'});f.gesture.end(null,reason);f.gesture.end(null,reason);assert.equal(f.gesture.current,null);assert.equal(f.captures.size,0);assert.equal(f.ends.length,1);assert.equal(f.ends[0][2],reason);assert.deepEqual(f.states,[true,false])});
test('capture failure still has release and button-state recovery',()=>{const f=fixture({captureFails:true});f.gesture.begin(event(),{});f.gesture.move(event({buttons:0}));assert.equal(f.gesture.current,null);assert.equal(f.ends.length,1)});
test('stationary pin click remains distinct from dragged wire',()=>{const f=fixture();f.gesture.begin(event(),{type:'pin'});f.gesture.end(event({buttons:0}));assert.equal(f.ends[0][0].moved,false);f.gesture.begin(event(),{type:'pin'});f.gesture.move(event({clientY:110}));f.gesture.end(event({buttons:0}));assert.equal(f.ends[1][0].moved,true)});
test('state is cleared before releasing capture or invoking application callbacks',()=>{let g,seen;const canvas={setPointerCapture(){},hasPointerCapture:()=>true,releasePointerCapture(){g.end(event({buttons:0}),'capture-lost')}};let count=0;g=createGraphGesture(canvas,{move(){},finish(){count++;seen=g.current}});g.begin(event(),{});g.end(event({buttons:0}));assert.equal(count,1);assert.equal(seen,null)});
