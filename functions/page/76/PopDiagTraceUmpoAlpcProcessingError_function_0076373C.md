# PopDiagTraceUmpoAlpcProcessingError

- RVA: `0x0076373C`–`0x007637CF` (길이 `147` bytes)
- VA: `0x000000014076373C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000986E4`
- 디코드: `31`개 명령, `147/147` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0076376C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007637B7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007637C4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopUmpoProcessMessages](../A2/PopUmpoProcessMessages_function_00A2E790.md) at `0x00A2E8B8`

### Static image references
- `0x00763740` → RVA `0x00E0A740` (`.data`; read)
- `0x0076374F` → RVA `0x00E07748` (`.data`; read)
- `0x00763784` → RVA `0x000496AC` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0076376C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007637B7` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007637C4` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0076373C  48 83 EC 78                     sub rsp, 0x78
00763740  48 8B 05 F9 6F 6A 00            mov rax, qword ptr [rip + 0x6a6ff9]
00763747  48 33 C4                        xor rax, rsp
0076374A  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0076374F  83 3D F2 3F 6A 00 05            cmp dword ptr [rip + 0x6a3ff2], 5
00763756  44 8B C1                        mov r8d, ecx
00763759  76 61                           jbe 0x1407637bc
0076375B  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00763765  48 8D 0D DC 3F 6A 00            lea rcx, [rip + 0x6a3fdc]
0076376C  E8 2F B3 CC FF                  call 0x14042eaa0
00763771  84 C0                           test al, al
00763773  74 47                           je 0x1407637bc
00763775  83 64 24 64 00                  and dword ptr [rsp + 0x64], 0
0076377A  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0076377F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00763784  48 8D 15 21 5F 8E FF            lea rdx, [rip - 0x71a0df]
0076378B  48 8D 44 24 38                  lea rax, [rsp + 0x38]
00763790  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
00763795  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0076379A  48 8D 0D A7 3F 6A 00            lea rcx, [rip + 0x6a3fa7]
007637A1  45 33 C9                        xor r9d, r9d
007637A4  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
007637AC  45 33 C0                        xor r8d, r8d
007637AF  C7 44 24 60 04 00 00 00         mov dword ptr [rsp + 0x60], 4
007637B7  E8 24 29 CC FF                  call 0x1404260e0
007637BC  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007637C1  48 33 CC                        xor rcx, rsp
007637C4  E8 77 8E F4 FF                  call 0x1406ac640
007637C9  48 83 C4 78                     add rsp, 0x78
007637CD  C3                              ret
007637CE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceUmpoAlpcProcessingError(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 6975481)) ^ (v_rsp);
    v_stack_m10 = result;
    if ((*(unsigned int *)(v_rip + 6963186)) <= 5) goto loc_007637BC;
    result = tlgKeywordOn(v_rip + 6963164, a2, (unsigned int)(a1), a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        a2 = v_rip - 7446751;
        result = v_stack_m40;
        v_stack_m48 = (unsigned int)((unsigned int)(a1));
        v_stack_m50 = result;
        a1 = v_rip + 6963111;
        a4 = 0;
        v_stack_m58 = 3;
        a3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceUmpoAlpcProcessingError(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x6A6FF9)) ^ (local_rsp);
    v_stack_m10 = result;
    if ((*(uint32_t *)(v_rip + 0x6A3FF2)) <= 5) goto loc_007637BC;
    result = tlgKeywordOn(v_rip + 6963164, Arg2, (uint32_t)(Arg1), Arg4);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m48;
        v_stack_m20 = result;
        Arg2 = v_rip - 7446751;
        result = v_stack_m40;
        v_stack_m48 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m50 = result;
        Arg1 = v_rip + 6963111;
        Arg4 = 0;
        v_stack_m58 = 3;
        Arg3 = 0;
        v_stack_m18 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0076373C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0076373C[BB_0076373C]
  bb_0076375B[BB_0076375B]
  bb_00763775[BB_00763775]
  bb_007637BC[BB_007637BC]
  bb_007637CE[BB_007637CE]
  bb_0076373C -->|branch| bb_007637BC
  bb_0076373C -->|fallthrough| bb_0076375B
  bb_0076375B -->|branch| bb_007637BC
  bb_0076375B -->|fallthrough| bb_00763775
  bb_00763775 -->|flow| bb_007637BC
```
