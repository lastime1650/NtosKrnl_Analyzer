# MiInitializeDynamicRegion

- RVA: `0x00C65C2C`–`0x00C65C43` (길이 `23` bytes)
- VA: `0x0000000140C65C2C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C65C30` → [MiSystemVaToDynamicBitmap](../../text/3B/MiSystemVaToDynamicBitmap_function_003B4F88.md) (function, `0x003B4F88`)
- `0x00C65C38` → [MiBuildDynamicRegion](../../text/67/MiBuildDynamicRegion_function_0067F470.md) (function, `0x0067F470`)

### Direct callers
- [MiInitializeSystemCache](../../page/7F/MiInitializeSystemCache_function_007FE1F0.md) at `0x007FE289`
- [MiBuildPagedPool](MiBuildPagedPool_function_00C64918.md) at `0x00C64934`
- [MiInitializeNonPagedPool](MiInitializeNonPagedPool_function_00C64A24.md) at `0x00C64B7F`
- [MiBuildSystemDataViews](MiBuildSystemDataViews_function_00C64DCC.md) at `0x00C64DEC`
- [MiInitializeKernelStacks](MiInitializeKernelStacks_function_00C680B8.md) at `0x00C681B7`
- [MiInitializeNonCachedMappingRegion](MiInitializeNonCachedMappingRegion_function_00C6A738.md) at `0x00C6A760`
- [MiInitializeSystemPtes](MiInitializeSystemPtes_function_00C6A998.md) at `0x00C6AB0D`
- [MiInitializeSystemImageRegion](MiInitializeSystemImageRegion_function_00C6C05C.md) at `0x00C6C0A2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C65C30` → [MiSystemVaToDynamicBitmap](../../text/3B/MiSystemVaToDynamicBitmap_function_003B4F88.md) (`INIT` → `.text`)
  - `0x00C65C38` → [MiBuildDynamicRegion](../../text/67/MiBuildDynamicRegion_function_0067F470.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C65C2C  48 83 EC 28                     sub rsp, 0x28
00C65C30  E8 53 F3 74 FF                  call 0x1403b4f88
00C65C35  48 8B C8                        mov rcx, rax
00C65C38  E8 33 98 A1 FF                  call 0x14067f470
00C65C3D  48 83 C4 28                     add rsp, 0x28
00C65C41  C3                              ret
00C65C42  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeDynamicRegion(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiSystemVaToDynamicBitmap(a1, a2, a3, a4);
    result = MiBuildDynamicRegion(result, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiInitializeDynamicRegion(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiSystemVaToDynamicBitmap(a1, a2, a3, a4);
    result = MiBuildDynamicRegion(result, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C65C2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C65C2C[BB_00C65C2C]
  bb_00C65C42[BB_00C65C42]
```
