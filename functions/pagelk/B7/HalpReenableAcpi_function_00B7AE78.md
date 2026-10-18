# HalpReenableAcpi

- RVA: `0x00B7AE78`–`0x00B7AEA6` (길이 `46` bytes)
- VA: `0x0000000140B7AE78`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B7AE89` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B7AE9B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpPowerEarlyRestore](../../text/4A/HalpPowerEarlyRestore_function_004ABAB0.md) at `0x004ABAC5`
- [HaliAcpiSleep](../../text/56/HaliAcpiSleep_function_0056AD60.md) at `0x0056AF49`

### Static image references
- `0x00B7AE7C` → RVA `0x00E11750` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B7AE89` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
  - `0x00B7AE9B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B7AE78  48 83 EC 28                     sub rsp, 0x28
00B7AE7C  48 8B 05 CD 68 29 00            mov rax, qword ptr [rip + 0x2968cd]
00B7AE83  B1 01                           mov cl, 1
00B7AE85  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00B7AE89  E8 42 FC B3 FF                  call 0x1406baad0
00B7AE8E  48 8B 05 BB 68 29 00            mov rax, qword ptr [rip + 0x2968bb]
00B7AE95  B1 01                           mov cl, 1
00B7AE97  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00B7AE9B  E8 30 FC B3 FF                  call 0x1406baad0
00B7AEA0  48 83 C4 28                     add rsp, 0x28
00B7AEA4  C3                              ret
00B7AEA5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpReenableAcpi(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = guard_dispatch_icall(1, a2, a3, a4);
    result = guard_dispatch_icall(1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpReenableAcpi(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = guard_dispatch_icall(1, a2, a3, a4);
    result = guard_dispatch_icall(1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B7AE78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B7AE78[BB_00B7AE78]
  bb_00B7AEA5[BB_00B7AEA5]
```
