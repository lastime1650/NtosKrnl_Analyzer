# HalpTimerClockStop

- RVA: `0x004C0690`–`0x004C06EE` (길이 `94` bytes)
- VA: `0x00000001404C0690`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C34C`
- 디코드: `23`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004C06AF` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x004C06BE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x004C06D4` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x004C06E3` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [HalpTimerClockPowerChange](../54/HalpTimerClockPowerChange_function_005481A0.md) at `0x00548202`

### Static image references
- `0x004C06A5` → RVA `0x00FC40F0` (`.data`; read)
- `0x004C06CA` → RVA `0x00FC4108` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C0690  40 53                           push rbx
004C0692  48 83 EC 20                     sub rsp, 0x20
004C0696  65 48 8B 1C 25 20 00 00 00      mov rbx, qword ptr gs:[0x20]
004C069F  F6 43 22 02                     test byte ptr [rbx + 0x22], 2
004C06A3  75 25                           jne 0x1404c06ca
004C06A5  48 8B 15 44 3A B0 00            mov rdx, qword ptr [rip + 0xb03a44]
004C06AC  48 8B CA                        mov rcx, rdx
004C06AF  E8 4C 8E D4 FF                  call 0x140209500
004C06B4  48 8B C8                        mov rcx, rax
004C06B7  48 8B 82 88 00 00 00            mov rax, qword ptr [rdx + 0x88]
004C06BE  E8 0D A4 1F 00                  call 0x1406baad0
004C06C3  48 83 C4 20                     add rsp, 0x20
004C06C7  5B                              pop rbx
004C06C8  C3                              ret
004C06C9  CC                              int3
004C06CA  48 8B 15 37 3A B0 00            mov rdx, qword ptr [rip + 0xb03a37]
004C06D1  48 8B CA                        mov rcx, rdx
004C06D4  E8 27 8E D4 FF                  call 0x140209500
004C06D9  48 8B C8                        mov rcx, rax
004C06DC  48 8B 82 88 00 00 00            mov rax, qword ptr [rdx + 0x88]
004C06E3  E8 E8 A3 1F 00                  call 0x1406baad0
004C06E8  80 63 22 FD                     and byte ptr [rbx + 0x22], 0xfd
004C06EC  EB D5                           jmp 0x1404c06c3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerClockStop(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 34)) & (2)) != 0) goto loc_004C06CA;
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 11549252), *(unsigned __int64 *)(v_rip + 11549252), a3, a4);
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(v_rip + 11549252), a3, a4);
loc_004C06C3:
    v_rsp = (v_rsp) + (32);
    return result;
loc_004C06CA:
    result = HalpTimerGetInternalData(*(unsigned __int64 *)(v_rip + 11549239), *(unsigned __int64 *)(v_rip + 11549239), a3, a4);
    result = guard_dispatch_icall(result, *(unsigned __int64 *)(v_rip + 11549239), a3, a4);
    goto loc_004C06C3;
}
```

## 5. (Beta) C Style

```c
void HalpTimerClockStop(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x22)) & (2)) != 0) goto loc_004C06CA;
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xB03A44), *(uint64_t *)(v_rip + 0xB03A44), a3, a4);
    result = guard_dispatch_icall(result, *(uint64_t *)(v_rip + 0xB03A44), a3, a4);
loc_004C06C3:
    local_rsp = (local_rsp) + (32);
    return result;
loc_004C06CA:
    result = HalpTimerGetInternalData(*(uint64_t *)(v_rip + 0xB03A37), *(uint64_t *)(v_rip + 0xB03A37), a3, a4);
    result = guard_dispatch_icall(result, *(uint64_t *)(v_rip + 0xB03A37), a3, a4);
    goto loc_004C06C3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C0690&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C0690[BB_004C0690]
  bb_004C06A5[BB_004C06A5]
  bb_004C06C3[BB_004C06C3]
  bb_004C06C9[BB_004C06C9]
  bb_004C06CA[BB_004C06CA]
  bb_004C0690 -->|branch| bb_004C06CA
  bb_004C0690 -->|fallthrough| bb_004C06A5
  bb_004C06A5 -->|flow| bb_004C06C3
  bb_004C06C9 -->|flow| bb_004C06CA
  bb_004C06CA -->|branch| bb_004C06C3
```
