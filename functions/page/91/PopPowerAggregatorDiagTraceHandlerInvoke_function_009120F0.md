# PopPowerAggregatorDiagTraceHandlerInvoke

- RVA: `0x009120F0`–`0x0091217D` (길이 `141` bytes)
- VA: `0x00000001409120F0`
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
- `0x0091213B` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00912165` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00912172` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopPowerAggregatorInvokeStateMachine](PopPowerAggregatorInvokeStateMachine_function_00912038.md) at `0x00912096`

### Static image references
- `0x009120F4` → RVA `0x00E0A740` (`.data`; read)
- `0x00912112` → RVA `0x00E67858` (`.data`; read)
- `0x0091212D` → RVA `0x00F0B408` (`.data`; read)
- `0x00912134` → RVA `0x00011998` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0091213B` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00912165` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00912172` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009120F0  48 83 EC 68                     sub rsp, 0x68
009120F4  48 8B 05 45 86 4F 00            mov rax, qword ptr [rip + 0x4f8645]
009120FB  48 33 C4                        xor rax, rsp
009120FE  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00912103  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
00912108  B8 04 00 00 00                  mov eax, 4
0091210D  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
00912112  80 3D 3F 57 55 00 00            cmp byte ptr [rip + 0x55573f], 0
00912119  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0091211E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00912122  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00912127  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0091212B  74 3D                           je 0x14091216a
0091212D  48 8B 0D D4 92 5F 00            mov rcx, qword ptr [rip + 0x5f92d4]
00912134  48 8D 15 5D F8 6F FF            lea rdx, [rip - 0x9007a3]
0091213B  E8 10 03 A8 FF                  call 0x140392450
00912140  84 C0                           test al, al
00912142  74 26                           je 0x14091216a
00912144  48 8B 0D BD 92 5F 00            mov rcx, qword ptr [rip + 0x5f92bd]
0091214B  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00912150  41 B9 02 00 00 00               mov r9d, 2
00912156  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0091215B  45 33 C0                        xor r8d, r8d
0091215E  48 8D 15 33 F8 6F FF            lea rdx, [rip - 0x9007cd]
00912165  E8 B6 A5 B0 FF                  call 0x14041c720
0091216A  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
0091216F  48 33 CC                        xor rcx, rsp
00912172  E8 C9 A4 D9 FF                  call 0x1406ac640
00912177  48 83 C4 68                     add rsp, 0x68
0091217B  C3                              ret
0091217C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerAggregatorDiagTraceHandlerInvoke(__int64 a1, __int64 a2, int a3)
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
    result = (*(unsigned __int64 *)(v_rip + 5211717)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m38 = a1;
    v_stack_m30 = 4;
    v_stack_m28 = a2;
    v_stack_m20 = 4;
    if ((*(unsigned __int8 *)(v_rip + 5592895)) == 0) goto loc_0091216A;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6263508), v_rip - 9439139, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 6263485);
        result = v_stack_m38;
        a4 = 2;
        v_stack_m48 = result;
        a3 = 0;
        a2 = v_rip - 9439181;
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
int64_t PopPowerAggregatorDiagTraceHandlerInvoke(int64_t Arg1, int64_t Arg2, int32_t Arg3)
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
    result = (*(uint64_t *)(v_rip + 0x4F8645)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m38 = Arg1;
    v_stack_m30 = 4;
    v_stack_m28 = Arg2;
    v_stack_m20 = 4;
    if ((*(uint8_t *)(v_rip + 0x55573F)) == 0) goto loc_0091216A;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x5F92D4), v_rip - 9439139, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x5F92BD);
        result = v_stack_m38;
        a4 = 2;
        v_stack_m48 = result;
        Arg3 = 0;
        Arg2 = v_rip - 9439181;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009120F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009120F0[BB_009120F0]
  bb_0091212D[BB_0091212D]
  bb_00912144[BB_00912144]
  bb_0091216A[BB_0091216A]
  bb_0091217C[BB_0091217C]
  bb_009120F0 -->|branch| bb_0091216A
  bb_009120F0 -->|fallthrough| bb_0091212D
  bb_0091212D -->|branch| bb_0091216A
  bb_0091212D -->|fallthrough| bb_00912144
  bb_00912144 -->|flow| bb_0091216A
```
