# PopTraceSystemIdleS0LowPowerDozeTimerCancelled

- RVA: `0x00763F68`–`0x00763FEF` (길이 `135` bytes)
- VA: `0x0000000140763F68`
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
- `0x00763F96` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00763FD7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x00763FE4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopIdleCancelAoAcDozeS4Timer](../../text/4B/PopIdleCancelAoAcDozeS4Timer_function_004BC9C4.md) at `0x004BCA2E`

### Static image references
- `0x00763F70` → RVA `0x00E0A740` (`.data`; read)
- `0x00763F7F` → RVA `0x00E67858` (`.data`; read)
- `0x00763F88` → RVA `0x00F0B408` (`.data`; read)
- `0x00763F8F` → RVA `0x00022060` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00763F96` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00763FD7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x00763FE4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00763F68  89 4C 24 08                     mov dword ptr [rsp + 8], ecx
00763F6C  48 83 EC 58                     sub rsp, 0x58
00763F70  48 8B 05 C9 67 6A 00            mov rax, qword ptr [rip + 0x6a67c9]
00763F77  48 33 C4                        xor rax, rsp
00763F7A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00763F7F  80 3D D2 38 70 00 00            cmp byte ptr [rip + 0x7038d2], 0
00763F86  74 54                           je 0x140763fdc
00763F88  48 8B 0D 79 74 7A 00            mov rcx, qword ptr [rip + 0x7a7479]
00763F8F  48 8D 15 CA E0 8B FF            lea rdx, [rip - 0x741f36]
00763F96  E8 B5 E4 C2 FF                  call 0x140392450
00763F9B  84 C0                           test al, al
00763F9D  74 3D                           je 0x140763fdc
00763F9F  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
00763FA4  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00763FA9  48 8B 0D 58 74 7A 00            mov rcx, qword ptr [rip + 0x7a7458]
00763FB0  48 8D 15 A9 E0 8B FF            lea rdx, [rip - 0x741f57]
00763FB7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00763FBC  41 B9 01 00 00 00               mov r9d, 1
00763FC2  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00763FC7  C7 44 24 38 04 00 00 00         mov dword ptr [rsp + 0x38], 4
00763FCF  45 33 C0                        xor r8d, r8d
00763FD2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00763FD7  E8 44 87 CB FF                  call 0x14041c720
00763FDC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00763FE1  48 33 CC                        xor rcx, rsp
00763FE4  E8 57 86 F4 FF                  call 0x1406ac640
00763FE9  48 83 C4 58                     add rsp, 0x58
00763FED  C3                              ret
00763FEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceSystemIdleS0LowPowerDozeTimerCancelled(int a1, __int64 a2, int a3)
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
    result = (*(unsigned __int64 *)(v_rip + 6973385)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 7354578)) == 0) goto loc_00763FDC;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8025209), v_rip - 7610166, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_p8;
        a1 = *(unsigned __int64 *)(v_rip + 8025176);
        a2 = v_rip - 7610199;
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
int64_t PopTraceSystemIdleS0LowPowerDozeTimerCancelled(int32_t Arg1, int64_t Arg2, int32_t Arg3)
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
    result = (*(uint64_t *)(v_rip + 0x6A67C9)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x7038D2)) == 0) goto loc_00763FDC;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7A7479), v_rip - 7610166, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_p8;
        Arg1 = *(uint64_t *)(v_rip + 0x7A7458);
        Arg2 = v_rip - 7610199;
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00763F68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00763F68[BB_00763F68]
  bb_00763F88[BB_00763F88]
  bb_00763F9F[BB_00763F9F]
  bb_00763FDC[BB_00763FDC]
  bb_00763FEE[BB_00763FEE]
  bb_00763F68 -->|branch| bb_00763FDC
  bb_00763F68 -->|fallthrough| bb_00763F88
  bb_00763F88 -->|branch| bb_00763FDC
  bb_00763F88 -->|fallthrough| bb_00763F9F
  bb_00763F9F -->|flow| bb_00763FDC
```
