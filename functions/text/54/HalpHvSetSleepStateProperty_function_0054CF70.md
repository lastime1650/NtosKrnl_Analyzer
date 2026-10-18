# HalpHvSetSleepStateProperty

- RVA: `0x0054CF70`–`0x0054CF90` (길이 `32` bytes)
- VA: `0x000000014054CF70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054CF85` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B801`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B883`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070B8FF`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070BA39`
- [HaliAcpiMachineStateInit](../../page/70/HaliAcpiMachineStateInit_function_0070B730.md) at `0x0070BA99`

### Static image references
- `0x0054CF74` → RVA `0x00FC1C90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054CF70  48 83 EC 28                     sub rsp, 0x28
0054CF74  4C 8B 0D 15 4D A7 00            mov r9, qword ptr [rip + 0xa74d15]
0054CF7B  33 C0                           xor eax, eax
0054CF7D  4D 85 C9                        test r9, r9
0054CF80  74 08                           je 0x14054cf8a
0054CF82  49 8B C1                        mov rax, r9
0054CF85  E8 46 DB 16 00                  call 0x1406baad0
0054CF8A  48 83 C4 28                     add rsp, 0x28
0054CF8E  C3                              ret
0054CF8F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpHvSetSleepStateProperty(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (*(unsigned __int64 *)(v_rip + 10964245) != 0) {
        result = *(unsigned __int64 *)(v_rip + 10964245);
        result = guard_dispatch_icall(a1, a2, a3, *(unsigned __int64 *)(v_rip + 10964245));
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpHvSetSleepStateProperty(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (*(uint64_t *)(v_rip + 0xA74D15) != 0) {
        result = *(uint64_t *)(v_rip + 0xA74D15);
        result = guard_dispatch_icall(a1, a2, a3, *(uint64_t *)(v_rip + 0xA74D15));
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054CF70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054CF70[BB_0054CF70]
  bb_0054CF82[BB_0054CF82]
  bb_0054CF8A[BB_0054CF8A]
  bb_0054CF8F[BB_0054CF8F]
  bb_0054CF70 -->|branch| bb_0054CF8A
  bb_0054CF70 -->|fallthrough| bb_0054CF82
  bb_0054CF82 -->|flow| bb_0054CF8A
```
