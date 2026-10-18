# PopPowerAggregatorDiagTraceInternalStateChange

- RVA: `0x0098A6C4`–`0x0098A751` (길이 `141` bytes)
- VA: `0x000000014098A6C4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F9F8`
- 디코드: `31`개 명령, `141/141` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0098A70F` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0098A739` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0098A746` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPowerAggregatorSetCurrentState](PopPowerAggregatorSetCurrentState_function_0098A3B0.md) at `0x0098A3DA`

### Static image references
- `0x0098A6C8` → RVA `0x00E0A740` (`.data`; read)
- `0x0098A6E6` → RVA `0x00E67858` (`.data`; read)
- `0x0098A701` → RVA `0x00F0B408` (`.data`; read)
- `0x0098A708` → RVA `0x00013330` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0098A70F` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x0098A739` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0098A746` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098A6C4  48 83 EC 68                     sub rsp, 0x68
0098A6C8  48 8B 05 71 00 48 00            mov rax, qword ptr [rip + 0x480071]
0098A6CF  48 33 C4                        xor rax, rsp
0098A6D2  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0098A6D7  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
0098A6DC  B8 04 00 00 00                  mov eax, 4
0098A6E1  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
0098A6E6  80 3D 6B D1 4D 00 00            cmp byte ptr [rip + 0x4dd16b], 0
0098A6ED  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0098A6F2  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0098A6F6  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0098A6FB  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0098A6FF  74 3D                           je 0x14098a73e
0098A701  48 8B 0D 00 0D 58 00            mov rcx, qword ptr [rip + 0x580d00]
0098A708  48 8D 15 21 8C 68 FF            lea rdx, [rip - 0x9773df]
0098A70F  E8 3C 7D A0 FF                  call 0x140392450
0098A714  84 C0                           test al, al
0098A716  74 26                           je 0x14098a73e
0098A718  48 8B 0D E9 0C 58 00            mov rcx, qword ptr [rip + 0x580ce9]
0098A71F  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0098A724  41 B9 02 00 00 00               mov r9d, 2
0098A72A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0098A72F  45 33 C0                        xor r8d, r8d
0098A732  48 8D 15 F7 8B 68 FF            lea rdx, [rip - 0x977409]
0098A739  E8 E2 1F A9 FF                  call 0x14041c720
0098A73E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0098A743  48 33 CC                        xor rcx, rsp
0098A746  E8 F5 1E D2 FF                  call 0x1406ac640
0098A74B  48 83 C4 68                     add rsp, 0x68
0098A74F  C3                              ret
0098A750  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerAggregatorDiagTraceInternalStateChange(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 4718705)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m38 = a1;
    v_stack_m30 = 4;
    v_stack_m28 = a2;
    v_stack_m20 = 4;
    if ((*(unsigned __int8 *)(v_rip + 5099883)) == 0) goto loc_0098A73E;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5770496), v_rip - 9925599, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 5770473);
        result = v_stack_m38;
        a4 = 2;
        v_stack_m48 = result;
        a3 = 0;
        a2 = v_rip - 9925641;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerAggregatorDiagTraceInternalStateChange(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x480071)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m38 = Arg1;
    v_stack_m30 = 4;
    v_stack_m28 = Arg2;
    v_stack_m20 = 4;
    if ((*(uint8_t *)(v_rip + 0x4DD16B)) == 0) goto loc_0098A73E;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x580D00), v_rip - 9925599, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x580CE9);
        result = v_stack_m38;
        a4 = 2;
        v_stack_m48 = result;
        Arg3 = 0;
        Arg2 = v_rip - 9925641;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098A6C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098A6C4[BB_0098A6C4]
  bb_0098A701[BB_0098A701]
  bb_0098A718[BB_0098A718]
  bb_0098A73E[BB_0098A73E]
  bb_0098A750[BB_0098A750]
  bb_0098A6C4 -->|branch| bb_0098A73E
  bb_0098A6C4 -->|fallthrough| bb_0098A701
  bb_0098A701 -->|branch| bb_0098A73E
  bb_0098A701 -->|fallthrough| bb_0098A718
  bb_0098A718 -->|flow| bb_0098A73E
```
