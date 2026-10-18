# IaLpssWriteCmdStatus

- RVA: `0x006AB70C`–`0x006AB741` (길이 `53` bytes)
- VA: `0x00000001406AB70C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `16`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x006AB72D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [IaLpssPciSetPower](IaLpssPciSetPower_function_006AB358.md) at `0x006AB3E5`
- [IaLpssPciSetPower](IaLpssPciSetPower_function_006AB358.md) at `0x006AB444`

### Static image references
- `0x006AB710` → RVA `0x00EF0100` (`.data`; read)
- `0x006AB726` → RVA `0x00E039E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AB70C  48 83 EC 28                     sub rsp, 0x28
006AB710  4C 8B 05 E9 49 84 00            mov r8, qword ptr [rip + 0x8449e9]
006AB717  4D 85 C0                        test r8, r8
006AB71A  74 1A                           je 0x1406ab736
006AB71C  48 85 C9                        test rcx, rcx
006AB71F  74 15                           je 0x1406ab736
006AB721  8B 11                           mov edx, dword ptr [rcx]
006AB723  49 8B C8                        mov rcx, r8
006AB726  48 8B 05 BB 82 75 00            mov rax, qword ptr [rip + 0x7582bb]
006AB72D  E8 9E F3 00 00                  call 0x1406baad0
006AB732  33 C0                           xor eax, eax
006AB734  EB 05                           jmp 0x1406ab73b
006AB736  B8 02 00 00 00                  mov eax, 2
006AB73B  48 83 C4 28                     add rsp, 0x28
006AB73F  C3                              ret
006AB740  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IaLpssWriteCmdStatus(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 8669673) == 0) goto loc_006AB736;
    if (a1 == 0) goto loc_006AB736;
    result = guard_dispatch_icall(*(unsigned __int64 *)(v_rip + 8669673), (unsigned int)(*(unsigned int *)(a1)), *(unsigned __int64 *)(v_rip + 8669673), a4);
    result = 0;
    goto loc_006AB73B;
loc_006AB736:
loc_006AB73B:
    v_rsp = (v_rsp) + (40);
    return 2;
}
```

## 5. (Beta) C Style

```c
int64_t IaLpssWriteCmdStatus(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x8449E9) == 0) goto loc_006AB736;
    if (Arg1 == 0) goto loc_006AB736;
    result = guard_dispatch_icall(*(uint64_t *)(v_rip + 0x8449E9), (uint32_t)(*(uint32_t *)(Arg1)), *(uint64_t *)(v_rip + 0x8449E9), a4);
    result = 0;
    goto loc_006AB73B;
loc_006AB736:
loc_006AB73B:
    local_rsp = (local_rsp) + (40);
    return 2;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AB70C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AB70C[BB_006AB70C]
  bb_006AB71C[BB_006AB71C]
  bb_006AB721[BB_006AB721]
  bb_006AB736[BB_006AB736]
  bb_006AB73B[BB_006AB73B]
  bb_006AB740[BB_006AB740]
  bb_006AB70C -->|branch| bb_006AB736
  bb_006AB70C -->|fallthrough| bb_006AB71C
  bb_006AB71C -->|branch| bb_006AB736
  bb_006AB71C -->|fallthrough| bb_006AB721
  bb_006AB721 -->|branch| bb_006AB73B
  bb_006AB736 -->|flow| bb_006AB73B
```
