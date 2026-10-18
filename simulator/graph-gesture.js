// One owner per pointer gesture. Capture belongs to the stable canvas, never a
// node that may be replaced while the inspector or runtime is rendering.
export function createGraphGesture(canvas, {move, finish, active = () => {}}) {
  let session = null;
  return {
    get current() { return session; },
    begin(event, data) {
      if (session || event.button !== 0 || event.isPrimary === false) return false;
      event.preventDefault();
      session = {...data, pointerId:event.pointerId, startX:event.clientX, startY:event.clientY, moved:false};
      try { canvas.setPointerCapture(event.pointerId); } catch { /* Window fallbacks still terminate the gesture. */ }
      active(true);
      return true;
    },
    move(event) {
      const s = session;
      if (!s || event.pointerId !== s.pointerId) return;
      if (!(event.buttons & 1)) { this.end(null, 'buttons-released'); return; }
      event.preventDefault();
      const dx=event.clientX-s.startX, dy=event.clientY-s.startY;
      if (Math.abs(dx)+Math.abs(dy)>5) s.moved=true;
      move(s, dx, dy);
    },
    end(event, reason='release') {
      const s=session;
      if (!s || (event && event.pointerId !== s.pointerId)) return;
      // Releasing another mouse button must not terminate a left-button drag.
      if (reason==='release' && event && (event.buttons & 1)) return;
      event?.preventDefault();
      session=null;
      try { if(canvas.hasPointerCapture(s.pointerId)) canvas.releasePointerCapture(s.pointerId); }
      catch { /* Capture can already have been revoked by the browser. */ }
      active(false);
      finish(s, event, reason);
    }
  };
}
