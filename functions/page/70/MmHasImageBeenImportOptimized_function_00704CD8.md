# MmHasImageBeenImportOptimized

- RVA: `0x00704CD8`–`0x00704CF8` (길이 `32` bytes)
- VA: `0x0000000140704CD8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00704CDC` → [KeIsImportOptimizationEnabled](../../text/4A/KeIsImportOptimizationEnabled_function_004A8FB8.md) (function, `0x004A8FB8`)

### Direct callers
- [MiReapplyImportOptimizationForDriverVerifier](../../text/68/MiReapplyImportOptimizationForDriverVerifier_function_00682268.md) at `0x006822D9`
- [MiUnloadSystemImage](../AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA32D2`
- [MmApplyVerifierToRunningImage](../../pagevrfy/BB/MmApplyVerifierToRunningImage_function_00BB4780.md) at `0x00BB47AD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00704CDC` → [KeIsImportOptimizationEnabled](../../text/4A/KeIsImportOptimizationEnabled_function_004A8FB8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00704CD8  48 83 EC 28                     sub rsp, 0x28
00704CDC  E8 D7 42 DA FF                  call 0x1404a8fb8
00704CE1  84 C0                           test al, al
00704CE3  74 0B                           je 0x140704cf0
00704CE5  8B 41 68                        mov eax, dword ptr [rcx + 0x68]
00704CE8  C1 E8 07                        shr eax, 7
00704CEB  83 E0 01                        and eax, 1
00704CEE  EB 02                           jmp 0x140704cf2
00704CF0  33 C0                           xor eax, eax
00704CF2  48 83 C4 28                     add rsp, 0x28
00704CF6  C3                              ret
00704CF7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmHasImageBeenImportOptimized(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KeIsImportOptimizationEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00704CF0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 104))) >> (7));
    result = (unsigned int)((result) & (1));
    goto loc_00704CF2;
loc_00704CF0:
    result = 0;
loc_00704CF2:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmHasImageBeenImportOptimized(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KeIsImportOptimizationEnabled(Arg1, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00704CF0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x68))) >> (7));
    result = (uint32_t)((result) & (1));
    goto loc_00704CF2;
loc_00704CF0:
    result = 0;
loc_00704CF2:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00704CD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00704CD8[BB_00704CD8]
  bb_00704CE5[BB_00704CE5]
  bb_00704CF0[BB_00704CF0]
  bb_00704CF2[BB_00704CF2]
  bb_00704CF7[BB_00704CF7]
  bb_00704CD8 -->|branch| bb_00704CF0
  bb_00704CD8 -->|fallthrough| bb_00704CE5
  bb_00704CE5 -->|branch| bb_00704CF2
  bb_00704CF0 -->|flow| bb_00704CF2
```
