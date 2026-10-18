# PnprUnlockPagesForReplace

- RVA: `0x0073AA5C`–`0x0073AA87` (길이 `43` bytes)
- VA: `0x000000014073AA5C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0073AA67` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (function, `0x002A39F0`)
- `0x0073AA7C` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (function, `0x003926B0`)

### Direct callers
- [PnprCompleteWake](../../text/5A/PnprCompleteWake_function_005A884C.md) at `0x005A8850`
- [PnpReplacePartitionUnit](PnpReplacePartitionUnit_function_00738550.md) at `0x00738B00`

### Static image references
- `0x0073AA60` → RVA `0x00FC6C00` (`ALMOSTRO`; read)
- `0x0073AA6C` → RVA `0x00EFEDA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0073AA67` → [MmUnlockPagableImageSection](../../text/2A/MmUnlockPagableImageSection_function_002A39F0.md) (`PAGE` → `.text`)
  - `0x0073AA7C` → [ExNotifyCallback](../../text/39/ExNotifyCallback_function_003926B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0073AA5C  48 83 EC 28                     sub rsp, 0x28
0073AA60  48 8B 0D 99 C1 88 00            mov rcx, qword ptr [rip + 0x88c199]
0073AA67  E8 84 8F B6 FF                  call 0x1402a39f0
0073AA6C  48 8B 0D 35 43 7C 00            mov rcx, qword ptr [rip + 0x7c4335]
0073AA73  BA 03 00 00 00                  mov edx, 3
0073AA78  44 8D 42 FE                     lea r8d, [rdx - 2]
0073AA7C  E8 2F 7C C5 FF                  call 0x1403926b0
0073AA81  48 83 C4 28                     add rsp, 0x28
0073AA85  C3                              ret
0073AA86  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnprUnlockPagesForReplace(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MmUnlockPagableImageSection(*(unsigned __int64 *)(v_rip + 8962457), a2, a3, a4);
    result = ExNotifyCallback(*(unsigned __int64 *)(v_rip + 8143669), 3, 3 - 2, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PnprUnlockPagesForReplace(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MmUnlockPagableImageSection(*(uint64_t *)(v_rip + 0x88C199), a2, a3, a4);
    result = ExNotifyCallback(*(uint64_t *)(v_rip + 0x7C4335), 3, 3 - 2, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0073AA5C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0073AA5C[BB_0073AA5C]
  bb_0073AA86[BB_0073AA86]
```
