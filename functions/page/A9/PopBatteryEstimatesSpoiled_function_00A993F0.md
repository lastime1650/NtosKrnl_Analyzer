# PopBatteryEstimatesSpoiled

- RVA: `0x00A993F0`–`0x00A9942E` (길이 `62` bytes)
- VA: `0x0000000140A993F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065BAC`
- 디코드: `17`개 명령, `62/62` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A9941C` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)

### Direct callers
- [PopEstimateChargeTime](PopEstimateChargeTime_function_00A99264.md) at `0x00A992A3`
- [PopBatteryWorker](../AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE242A`

### Static image references
- `0x00A99400` → RVA `0x00E0B810` (`.data`; read)
- `0x00A99409` → RVA `0x00B02B80` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A9941C` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A993F0  40 53                           push rbx
00A993F2  48 83 EC 20                     sub rsp, 0x20
00A993F6  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
00A99400  48 39 05 09 24 37 00            cmp qword ptr [rip + 0x372409], rax
00A99407  72 21                           jb 0x140a9942a
00A99409  4C 8D 05 70 97 06 00            lea r8, [rip + 0x69770]
00A99410  BA 03 00 00 00                  mov edx, 3
00A99415  B9 92 00 00 00                  mov ecx, 0x92
00A9941A  B3 01                           mov bl, 1
00A9941C  E8 6F FE 8B FF                  call 0x140359290
00A99421  8A C3                           mov al, bl
00A99423  48 83 C4 20                     add rsp, 0x20
00A99427  5B                              pop rbx
00A99428  C3                              ret
00A99429  CC                              int3
00A9942A  32 DB                           xor bl, bl
00A9942C  EB F3                           jmp 0x140a99421
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopBatteryEstimatesSpoiled(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int64 *)(v_rip + 3613705)) < result) goto loc_00A9942A;
    result = DbgPrintEx(146, 3, v_rip + 431984, a4);
loc_00A99421:
    v_rsp = (v_rsp) + (32);
    return 1;
loc_00A9942A:
    v_rbx = 0;
    goto loc_00A99421;
}
```

## 5. (Beta) C Style

```c
void PopBatteryEstimatesSpoiled(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint64_t *)(v_rip + 0x372409)) < result) goto loc_00A9942A;
    result = DbgPrintEx(146, 3, v_rip + 431984, a4);
loc_00A99421:
    local_rsp = (local_rsp) + (32);
    return 1;
loc_00A9942A:
    local_rbx = 0;
    goto loc_00A99421;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A993F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A993F0[BB_00A993F0]
  bb_00A99409[BB_00A99409]
  bb_00A99421[BB_00A99421]
  bb_00A99429[BB_00A99429]
  bb_00A9942A[BB_00A9942A]
  bb_00A993F0 -->|branch| bb_00A9942A
  bb_00A993F0 -->|fallthrough| bb_00A99409
  bb_00A99409 -->|flow| bb_00A99421
  bb_00A99429 -->|flow| bb_00A9942A
  bb_00A9942A -->|branch| bb_00A99421
```
