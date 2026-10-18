# PopSetCleanShutdownMarker

- RVA: `0x00754644`–`0x00754677` (길이 `51` bytes)
- VA: `0x0000000140754644`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0075464F` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00754660` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x0075466C` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopGracefulShutdown](../../pagelk/B6/PopGracefulShutdown_function_00B6BEC8.md) at `0x00B6C0E4`

### Static image references
- `0x00754648` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00754654` → RVA `0x00E67418` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0075464F` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00754660` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x0075466C` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00754644  48 83 EC 28                     sub rsp, 0x28
00754648  48 8D 0D 91 AB 7B 00            lea rcx, [rip + 0x7bab91]
0075464F  E8 F0 C4 CD FF                  call 0x140430b44
00754654  80 25 BD 2D 71 00 FE            and byte ptr [rip + 0x712dbd], 0xfe
0075465B  B9 09 00 00 00                  mov ecx, 9
00754660  E8 3B E1 D5 FF                  call 0x1404b27a0
00754665  48 8D 0D 74 AB 7B 00            lea rcx, [rip + 0x7bab74]
0075466C  E8 4B B5 B8 FF                  call 0x1402dfbbc
00754671  48 83 C4 28                     add rsp, 0x28
00754675  C3                              ret
00754676  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopSetCleanShutdownMarker(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 8104849, a2, a3, a4);
    result = PopBsdHandleRequest(9, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 8104820, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopSetCleanShutdownMarker(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 8104849, a2, a3, a4);
    result = PopBsdHandleRequest(9, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 8104820, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00754644&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00754644[BB_00754644]
  bb_00754676[BB_00754676]
```
