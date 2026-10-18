# MmAllocateIndependentPages

- RVA: `0x00AA0CE0`–`0x00AA0CF5` (길이 `21` bytes)
- VA: `0x0000000140AA0CE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AA0CEA` → [MmAllocateIndependentPagesEx](MmAllocateIndependentPagesEx_function_00AA0CFC.md) (function, `0x00AA0CFC`)

### Direct callers
- [IopLiveDumpAllocateDumpBuffers](../../text/3F/IopLiveDumpAllocateDumpBuffers_function_003F5AE8.md) at `0x003F5CA3`
- [KeAllocateInterrupt](../../text/49/KeAllocateInterrupt_function_00493F50.md) at `0x00493FBA`
- [HvlStartBootLogicalProcessors](../../text/58/HvlStartBootLogicalProcessors_function_00584E18.md) at `0x00584EFD`
- [HvlStartBootLogicalProcessors](../../text/58/HvlStartBootLogicalProcessors_function_00584E18.md) at `0x00584F28`
- [HvlpInitializeHvCrashdump](../../text/58/HvlpInitializeHvCrashdump_function_0058BCCC.md) at `0x0058BD3E`
- [IopLiveDumpAllocateExtraBuffers](../../text/59/IopLiveDumpAllocateExtraBuffers_function_00599A9C.md) at `0x00599D2F`
- [IopLiveDumpAllocateIptBuffers](../../text/59/IopLiveDumpAllocateIptBuffers_function_0059A694.md) at `0x0059A72C`
- [IopLiveDumpAllocateIptBuffers](../../text/59/IopLiveDumpAllocateIptBuffers_function_0059A694.md) at `0x0059A7E7`
- [KeAllocateProcessorProfileStructures](../../text/5B/KeAllocateProcessorProfileStructures_function_005B14B0.md) at `0x005B1572`
- [KiAllocateProcessorStateInitializationParameters](../../text/5B/KiAllocateProcessorStateInitializationParameters_function_005B6F24.md) at `0x005B6F43`
- [sub_006EB392](../../text/6E/Unknown_function_006EB392.md) at `0x006EB5D8`
- [KiInitializePrcbContext](../../pagelk/B6/KiInitializePrcbContext_function_00B66D70.md) at `0x00B66DCC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA0CE0  48 83 EC 28                     sub rsp, 0x28
00AA0CE4  45 33 C9                        xor r9d, r9d
00AA0CE7  45 33 C0                        xor r8d, r8d
00AA0CEA  E8 0D 00 00 00                  call 0x140aa0cfc
00AA0CEF  48 83 C4 28                     add rsp, 0x28
00AA0CF3  C3                              ret
00AA0CF4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmAllocateIndependentPages(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    a3 = 0;
    result = MmAllocateIndependentPagesEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmAllocateIndependentPages(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    Arg3 = 0;
    result = MmAllocateIndependentPagesEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA0CE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA0CE0[BB_00AA0CE0]
  bb_00AA0CF4[BB_00AA0CF4]
```
