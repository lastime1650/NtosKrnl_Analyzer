# PopDiagTraceHibernateErrorStatus

- RVA: `0x00B713B4`–`0x00B7143B` (길이 `135` bytes)
- VA: `0x0000000140B713B4`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AD25C`
- 디코드: `29`개 명령, `135/135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00B713E2` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00B71423` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00B71430` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopTransitionSystemPowerStateEx](PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F808`

### Static image references
- `0x00B713BC` → RVA `0x00E0A740` (`.data`; read)
- `0x00B713CB` → RVA `0x00E67858` (`.data`; read)
- `0x00B713D4` → RVA `0x00F0B408` (`.data`; read)
- `0x00B713DB` → RVA `0x000213F0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B713E2` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGELK` → `.text`)
  - `0x00B71423` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGELK` → `.text`)
  - `0x00B71430` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B713B4  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00B713B8  48 83 EC 58                     sub rsp, 0x58
00B713BC  48 8B 05 7D 93 29 00            mov rax, qword ptr [rip + 0x29937d]
00B713C3  48 33 C4                        xor rax, rsp
00B713C6  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00B713CB  80 3D 86 64 2F 00 00            cmp byte ptr [rip + 0x2f6486], 0
00B713D2  74 54                           je 0x140b71428
00B713D4  48 8B 0D 2D A0 39 00            mov rcx, qword ptr [rip + 0x39a02d]
00B713DB  48 8D 15 0E 00 4B FF            lea rdx, [rip - 0xb4fff2]
00B713E2  E8 69 10 82 FF                  call 0x140392450
00B713E7  84 C0                           test al, al
00B713E9  74 3D                           je 0x140b71428
00B713EB  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
00B713F0  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00B713F5  48 8B 0D 0C A0 39 00            mov rcx, qword ptr [rip + 0x39a00c]
00B713FC  48 8D 15 ED FF 4A FF            lea rdx, [rip - 0xb50013]
00B71403  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B71408  41 B9 01 00 00 00               mov r9d, 1
00B7140E  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00B71413  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
00B7141B  45 33 C0                        xor r8d, r8d
00B7141E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B71423  E8 F8 B2 8A FF                  call 0x14041c720
00B71428  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00B7142D  48 33 CC                        xor rcx, rsp
00B71430  E8 0B B2 B3 FF                  call 0x1406ac640
00B71435  48 83 C4 58                     add rsp, 0x58
00B71439  C3                              ret
00B7143A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceHibernateErrorStatus(int a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 2724733)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 3105926)) == 0) goto loc_00B71428;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 3776557), v_rip - 11862002, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 3776524);
        a2 = v_rip - 11862035;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 4;
        a3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceHibernateErrorStatus(int32_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint32_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x29937D)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x2F6486)) == 0) goto loc_00B71428;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x39A02D), v_rip - 11862002, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x39A00C);
        Arg2 = v_rip - 11862035;
        v_stack_m28 = result;
        a4 = 1;
        result = v_stack_m28;
        v_stack_m20 = 4;
        Arg3 = 0;
        v_stack_m38 = result;
        result = EtwWrite(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B713B4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B713B4[BB_00B713B4]
  bb_00B713D4[BB_00B713D4]
  bb_00B713EB[BB_00B713EB]
  bb_00B71428[BB_00B71428]
  bb_00B7143A[BB_00B7143A]
  bb_00B713B4 -->|branch| bb_00B71428
  bb_00B713B4 -->|fallthrough| bb_00B713D4
  bb_00B713D4 -->|branch| bb_00B71428
  bb_00B713D4 -->|fallthrough| bb_00B713EB
  bb_00B713EB -->|flow| bb_00B71428
```
