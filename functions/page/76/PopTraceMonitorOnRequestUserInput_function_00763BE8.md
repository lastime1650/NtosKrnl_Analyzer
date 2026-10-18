# PopTraceMonitorOnRequestUserInput

- RVA: `0x00763BE8`–`0x00763CCD` (길이 `229` bytes)
- VA: `0x0000000140763BE8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC058`
- 디코드: `46`개 명령, `229/229` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00763C25` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00763CB2` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00763CBE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopMonitorInvocation](PopMonitorInvocation_function_00769710.md) at `0x0076978A`

### Static image references
- `0x00763BF6` → RVA `0x00E0A740` (`.data`; read)
- `0x00763C04` → RVA `0x00E07748` (`.data`; read)
- `0x00763C35` → RVA `0x00F0B410` (`.data`; read)
- `0x00763C3C` → RVA `0x0004978C` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00763C25` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00763CB2` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00763CBE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00763BE8  40 55                           push rbp
00763BEA  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00763BEF  48 81 EC C0 00 00 00            sub rsp, 0xc0
00763BF6  48 8B 05 43 6B 6A 00            mov rax, qword ptr [rip + 0x6a6b43]
00763BFD  48 33 C4                        xor rax, rsp
00763C00  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
00763C04  83 3D 3D 3B 6A 00 05            cmp dword ptr [rip + 0x6a3b3d], 5
00763C0B  44 8B C1                        mov r8d, ecx
00763C0E  0F 86 A3 00 00 00               jbe 0x140763cb7
00763C14  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00763C1E  48 8D 0D 23 3B 6A 00            lea rcx, [rip + 0x6a3b23]
00763C25  E8 76 AE CC FF                  call 0x14042eaa0
00763C2A  45 33 C9                        xor r9d, r9d
00763C2D  84 C0                           test al, al
00763C2F  0F 84 82 00 00 00               je 0x140763cb7
00763C35  48 8B 05 D4 77 7A 00            mov rax, qword ptr [rip + 0x7a77d4]
00763C3C  48 8D 15 49 5B 8E FF            lea rdx, [rip - 0x71a4b7]
00763C43  48 89 45 CF                     mov qword ptr [rbp - 0x31], rax
00763C47  48 8D 0D FA 3A 6A 00            lea rcx, [rip + 0x6a3afa]
00763C4E  48 8D 45 CF                     lea rax, [rbp - 0x31]
00763C52  44 89 45 CB                     mov dword ptr [rbp - 0x35], r8d
00763C56  48 89 45 07                     mov qword ptr [rbp + 7], rax
00763C5A  45 33 C0                        xor r8d, r8d
00763C5D  48 8D 45 C7                     lea rax, [rbp - 0x39]
00763C61  48 C7 45 0F 08 00 00 00         mov qword ptr [rbp + 0xf], 8
00763C69  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00763C6D  48 8D 45 CB                     lea rax, [rbp - 0x35]
00763C71  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
00763C75  48 8D 45 D7                     lea rax, [rbp - 0x29]
00763C79  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
00763C7D  48 8D 45 E7                     lea rax, [rbp - 0x19]
00763C81  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00763C86  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
00763C8E  44 88 4D C7                     mov byte ptr [rbp - 0x39], r9b
00763C92  48 C7 45 1F 01 00 00 00         mov qword ptr [rbp + 0x1f], 1
00763C9A  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
00763CA2  48 C7 45 D7 00 00 00 01         mov qword ptr [rbp - 0x29], 0x1000000
00763CAA  48 C7 45 3F 08 00 00 00         mov qword ptr [rbp + 0x3f], 8
00763CB2  E8 29 24 CC FF                  call 0x1404260e0
00763CB7  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
00763CBB  48 33 CC                        xor rcx, rsp
00763CBE  E8 7D 89 F4 FF                  call 0x1406ac640
00763CC3  48 81 C4 C0 00 00 00            add rsp, 0xc0
00763CCA  5D                              pop rbp
00763CCB  C3                              ret
00763CCC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopTraceMonitorOnRequestUserInput(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;

    v_rsp = (v_rsp) - (192);
    result = (*(unsigned __int64 *)(v_rip + 6974275)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 6961981)) <= 5) goto loc_00763CB7;
    result = tlgKeywordOn(v_rip + 6961955, a2, (unsigned int)(a1), a4);
    a4 = 0;
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(v_rip + 8026068);
        a2 = v_rip - 7447735;
        v_stack_m90 = result;
        a1 = v_rip + 6961914;
        result = v_stack_m90;
        v_stack_m94 = (unsigned int)((unsigned int)(a1));
        v_stack_m58 = result;
        a3 = 0;
        result = v_stack_m98;
        v_stack_m50 = 8;
        v_stack_m48 = result;
        result = v_stack_m94;
        v_stack_m38 = result;
        result = v_stack_m88;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        v_stack_m98 = 0;
        v_stack_m40 = 1;
        v_stack_m30 = 4;
        v_stack_m88 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (192);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopTraceMonitorOnRequestUserInput(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;

    local_rsp = (local_rsp) - (192);
    result = (*(uint64_t *)(v_rip + 0x6A6B43)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x6A3B3D)) <= 5) goto loc_00763CB7;
    result = tlgKeywordOn(v_rip + 6961955, Arg2, (uint32_t)(Arg1), Arg4);
    Arg4 = 0;
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(v_rip + 0x7A77D4);
        Arg2 = v_rip - 7447735;
        v_stack_m90 = result;
        Arg1 = v_rip + 6961914;
        result = v_stack_m90;
        v_stack_m94 = (uint32_t)((uint32_t)(Arg1));
        v_stack_m58 = result;
        Arg3 = 0;
        result = v_stack_m98;
        v_stack_m50 = 8;
        v_stack_m48 = result;
        result = v_stack_m94;
        v_stack_m38 = result;
        result = v_stack_m88;
        v_stack_m28 = result;
        result = v_stack_m78;
        v_stack_mA0 = result;
        v_stack_mA8 = 6;
        v_stack_m98 = 0;
        v_stack_m40 = 1;
        v_stack_m30 = 4;
        v_stack_m88 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (192);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00763BE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00763BE8[BB_00763BE8]
  bb_00763C14[BB_00763C14]
  bb_00763C35[BB_00763C35]
  bb_00763CB7[BB_00763CB7]
  bb_00763CCC[BB_00763CCC]
  bb_00763BE8 -->|branch| bb_00763CB7
  bb_00763BE8 -->|fallthrough| bb_00763C14
  bb_00763C14 -->|branch| bb_00763CB7
  bb_00763C14 -->|fallthrough| bb_00763C35
  bb_00763C35 -->|flow| bb_00763CB7
```
