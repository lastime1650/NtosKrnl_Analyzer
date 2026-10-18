# PopDiagTraceConsoleDisplayState

- RVA: `0x00A31978`–`0x00A319FF` (길이 `135` bytes)
- VA: `0x0000000140A31978`
- 실행 섹션: `PAGE`
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
- `0x00A319A6` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00A319E7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00A319F4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopUpdateConsoleDisplayState](PopUpdateConsoleDisplayState_function_00A31298.md) at `0x00A312C8`

### Static image references
- `0x00A31980` → RVA `0x00E0A740` (`.data`; read)
- `0x00A3198F` → RVA `0x00E67858` (`.data`; read)
- `0x00A31998` → RVA `0x00F0B408` (`.data`; read)
- `0x00A3199F` → RVA `0x0001A2C0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A319A6` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00A319E7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00A319F4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A31978  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00A3197C  48 83 EC 58                     sub rsp, 0x58
00A31980  48 8B 05 B9 8D 3D 00            mov rax, qword ptr [rip + 0x3d8db9]
00A31987  48 33 C4                        xor rax, rsp
00A3198A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A3198F  80 3D C2 5E 43 00 00            cmp byte ptr [rip + 0x435ec2], 0
00A31996  74 54                           je 0x140a319ec
00A31998  48 8B 0D 69 9A 4D 00            mov rcx, qword ptr [rip + 0x4d9a69]
00A3199F  48 8D 15 1A 89 5E FF            lea rdx, [rip - 0xa176e6]
00A319A6  E8 A5 0A 96 FF                  call 0x140392450
00A319AB  84 C0                           test al, al
00A319AD  74 3D                           je 0x140a319ec
00A319AF  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
00A319B4  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00A319B9  48 8B 0D 48 9A 4D 00            mov rcx, qword ptr [rip + 0x4d9a48]
00A319C0  48 8D 15 F9 88 5E FF            lea rdx, [rip - 0xa17707]
00A319C7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A319CC  41 B9 01 00 00 00               mov r9d, 1
00A319D2  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00A319D7  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
00A319DF  45 33 C0                        xor r8d, r8d
00A319E2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A319E7  E8 34 AD 9E FF                  call 0x14041c720
00A319EC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00A319F1  48 33 CC                        xor rcx, rsp
00A319F4  E8 47 AC C7 FF                  call 0x1406ac640
00A319F9  48 83 C4 58                     add rsp, 0x58
00A319FD  C3                              ret
00A319FE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceConsoleDisplayState(int a1, __int64 a2, int a3)
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
    result = (*(unsigned __int64 *)(v_rip + 4033977)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 4415170)) == 0) goto loc_00A319EC;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 5085801), v_rip - 10581734, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 5085768);
        a2 = v_rip - 10581767;
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
int64_t PopDiagTraceConsoleDisplayState(int32_t Arg1, int64_t Arg2, int32_t Arg3)
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
    result = (*(uint64_t *)(v_rip + 0x3D8DB9)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x435EC2)) == 0) goto loc_00A319EC;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x4D9A69), v_rip - 10581734, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x4D9A48);
        Arg2 = v_rip - 10581767;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A31978&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A31978[BB_00A31978]
  bb_00A31998[BB_00A31998]
  bb_00A319AF[BB_00A319AF]
  bb_00A319EC[BB_00A319EC]
  bb_00A319FE[BB_00A319FE]
  bb_00A31978 -->|branch| bb_00A319EC
  bb_00A31978 -->|fallthrough| bb_00A31998
  bb_00A31998 -->|branch| bb_00A319EC
  bb_00A31998 -->|fallthrough| bb_00A319AF
  bb_00A319AF -->|flow| bb_00A319EC
```
