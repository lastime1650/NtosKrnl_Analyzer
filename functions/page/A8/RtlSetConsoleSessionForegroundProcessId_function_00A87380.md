# RtlSetConsoleSessionForegroundProcessId

- RVA: `0x00A87380`–`0x00A873B9` (길이 `57` bytes)
- VA: `0x0000000140A87380`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F13C`
- 디코드: `16`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A87389` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00A873A7` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A87392` → RVA `0x00FC5008` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A87389` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00A873A7` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A87380  40 53                           push rbx
00A87382  48 83 EC 20                     sub rsp, 0x20
00A87386  48 8B D9                        mov rbx, rcx
00A87389  E8 52 EF 9A FF                  call 0x1404362e0
00A8738E  84 C0                           test al, al
00A87390  75 15                           jne 0x140a873a7
00A87392  48 8B 05 6F DC 53 00            mov rax, qword ptr [rip + 0x53dc6f]
00A87399  48 89 98 38 03 00 00            mov qword ptr [rax + 0x338], rbx
00A873A0  48 83 C4 20                     add rsp, 0x20
00A873A4  5B                              pop rbx
00A873A5  C3                              ret
00A873A6  CC                              int3
00A873A7  E8 44 6E 87 FF                  call 0x1402fe1f0
00A873AC  48 8B 88 08 05 00 00            mov rcx, qword ptr [rax + 0x508]
00A873B3  48 89 59 08                     mov qword ptr [rcx + 8], rbx
00A873B7  EB E7                           jmp 0x140a873a0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlSetConsoleSessionForegroundProcessId(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A873A7;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 5495919) + 824) = a1;
loc_00A873A0:
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(v_rip + 5495919);
loc_00A873A7:
    result = PsGetCurrentServerSiloGlobals(a1, a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 1288) + 8) = a1;
    goto loc_00A873A0;
}
```

## 5. (Beta) C Style

```c
int64_t RtlSetConsoleSessionForegroundProcessId(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PsIsCurrentThreadInServerSilo(Arg1, a2, a3, a4);
    if ((uint8_t)(result) != 0) goto loc_00A873A7;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x53DC6F) + 0x338) = Arg1;
loc_00A873A0:
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(v_rip + 0x53DC6F);
loc_00A873A7:
    result = PsGetCurrentServerSiloGlobals(Arg1, a2, a3, a4);
    *(uint64_t *)(*(uint64_t *)(result + 0x508) + 0x8) = Arg1;
    goto loc_00A873A0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A87380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A87380[BB_00A87380]
  bb_00A87392[BB_00A87392]
  bb_00A873A0[BB_00A873A0]
  bb_00A873A6[BB_00A873A6]
  bb_00A873A7[BB_00A873A7]
  bb_00A87380 -->|branch| bb_00A873A7
  bb_00A87380 -->|fallthrough| bb_00A87392
  bb_00A87392 -->|flow| bb_00A873A0
  bb_00A873A6 -->|flow| bb_00A873A7
  bb_00A873A7 -->|branch| bb_00A873A0
```
