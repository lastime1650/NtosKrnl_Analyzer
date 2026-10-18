# PopSetUserShutdownMarkerWorker

- RVA: `0x00754680`–`0x007546BF` (길이 `63` bytes)
- VA: `0x0000000140754680`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `13`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0075468B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x0075469C` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x007546A8` → [PopOkayToQueueNextWorkItem](../../text/4A/PopOkayToQueueNextWorkItem_function_004AED54.md) (function, `0x004AED54`)
- `0x007546B4` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00754684` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00754690` → RVA `0x00E67418` (`.data`; read/write)
- `0x007546A1` → RVA `0x00F0F180` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **4**
  - `0x0075468B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x0075469C` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x007546A8` → [PopOkayToQueueNextWorkItem](../../text/4A/PopOkayToQueueNextWorkItem_function_004AED54.md) (`PAGE` → `.text`)
  - `0x007546B4` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00754680  48 83 EC 28                     sub rsp, 0x28
00754684  48 8D 0D 55 AB 7B 00            lea rcx, [rip + 0x7bab55]
0075468B  E8 B4 C4 CD FF                  call 0x140430b44
00754690  80 0D 81 2D 71 00 04            or byte ptr [rip + 0x712d81], 4
00754697  B9 09 00 00 00                  mov ecx, 9
0075469C  E8 FF E0 D5 FF                  call 0x1404b27a0
007546A1  48 8D 0D D8 AA 7B 00            lea rcx, [rip + 0x7baad8]
007546A8  E8 A7 A6 D5 FF                  call 0x1404aed54
007546AD  48 8D 0D 2C AB 7B 00            lea rcx, [rip + 0x7bab2c]
007546B4  E8 03 B5 B8 FF                  call 0x1402dfbbc
007546B9  48 83 C4 28                     add rsp, 0x28
007546BD  C3                              ret
007546BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSetUserShutdownMarkerWorker(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 8104789, a2, a3, a4);
    result = PopBsdHandleRequest(9, a2, a3, a4);
    result = PopOkayToQueueNextWorkItem(v_rip + 8104664, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 8104748, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopSetUserShutdownMarkerWorker(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 8104789, a2, a3, a4);
    result = PopBsdHandleRequest(9, a2, a3, a4);
    result = PopOkayToQueueNextWorkItem(v_rip + 8104664, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 8104748, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00754680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00754680[BB_00754680]
  bb_007546BE[BB_007546BE]
```
