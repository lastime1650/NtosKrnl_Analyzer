# MmUnlockPreChargedPagedPool

- RVA: `0x00AC5940`–`0x00AC5979` (길이 `57` bytes)
- VA: `0x0000000140AC5940`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `15`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AC5947` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (function, `0x0043E130`)
- `0x00AC596E` → [MiUnlockCodePage](../../text/2A/MiUnlockCodePage_function_002A2AB8.md) (function, `0x002A2AB8`)

### Direct callers
- [HalpMcUpdateUnlock](../../text/4B/HalpMcUpdateUnlock_function_004B81D8.md) at `0x004B81FF`
- [MiDeleteSubsectionLargePages](../../text/4D/MiDeleteSubsectionLargePages_function_004D51E0.md) at `0x004D5496`
- [PopFreeHiberContext](../70/PopFreeHiberContext_function_00704F1C.md) at `0x00705099`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AC5947` → [MiGetPteAddress](../../text/43/MiGetPteAddress_function_0043E130.md) (`PAGE` → `.text`)
  - `0x00AC596E` → [MiUnlockCodePage](../../text/2A/MiUnlockCodePage_function_002A2AB8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC5940  48 83 EC 28                     sub rsp, 0x28
00AC5944  4C 8B C1                        mov r8, rcx
00AC5947  E8 E4 87 97 FF                  call 0x14043e130
00AC594C  48 8D 8A FF 0F 00 00            lea rcx, [rdx + 0xfff]
00AC5953  41 81 E0 FF 0F 00 00            and r8d, 0xfff
00AC595A  49 03 C8                        add rcx, r8
00AC595D  45 33 C0                        xor r8d, r8d
00AC5960  48 C1 E9 0C                     shr rcx, 0xc
00AC5964  48 FF C9                        dec rcx
00AC5967  48 8D 14 C8                     lea rdx, [rax + rcx*8]
00AC596B  48 8B C8                        mov rcx, rax
00AC596E  E8 45 D1 7D FF                  call 0x1402a2ab8
00AC5973  48 83 C4 28                     add rsp, 0x28
00AC5977  C3                              ret
00AC5978  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmUnlockPreChargedPagedPool(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiGetPteAddress(a1, a2, a1, a4);
    a3 = (unsigned int)((a1) & (0xFFFULL));
    a1 = (a2 + 4095) + (a3);
    a3 = 0;
    a1 = (a1) >> (12);
    a1 = (a1) - 1;
    result = MiUnlockCodePage(result, result + a1 * 8, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmUnlockPreChargedPagedPool(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiGetPteAddress(Arg1, Arg2, Arg1, a4);
    a3 = (uint32_t)((Arg1) & (0xFFFULL));
    Arg1 = (Arg2 + 4095) + (a3);
    a3 = 0;
    Arg1 = (Arg1) >> (12);
    Arg1 = (Arg1) - 1;
    result = MiUnlockCodePage(result, result + Arg1 * 8, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC5940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC5940[BB_00AC5940]
  bb_00AC5978[BB_00AC5978]
```
