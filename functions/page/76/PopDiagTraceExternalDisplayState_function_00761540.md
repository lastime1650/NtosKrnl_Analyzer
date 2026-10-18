# PopDiagTraceExternalDisplayState

- RVA: `0x00761540`–`0x00761609` (길이 `201` bytes)
- VA: `0x0000000140761540`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `42`개 명령, `201/201` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00761580` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007615EE` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007615FA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopWnfUsb4DisplayPresenceCallback](PopWnfUsb4DisplayPresenceCallback_function_007656E0.md) at `0x007657E4`
- [PopUpdateExternalDisplayState](PopUpdateExternalDisplayState_function_0076C0DC.md) at `0x0076C109`

### Static image references
- `0x0076154E` → RVA `0x00E0A740` (`.data`; read)
- `0x0076155C` → RVA `0x00E07748` (`.data`; read)
- `0x00761595` → RVA `0x0004953E` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00761580` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007615EE` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007615FA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00761540  40 55                           push rbp
00761542  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
00761547  48 81 EC A0 00 00 00            sub rsp, 0xa0
0076154E  48 8B 05 EB 91 6A 00            mov rax, qword ptr [rip + 0x6a91eb]
00761555  48 33 C4                        xor rax, rsp
00761558  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0076155C  83 3D E5 61 6A 00 05            cmp dword ptr [rip + 0x6a61e5], 5
00761563  44 8A C2                        mov r8b, dl
00761566  44 8A C9                        mov r9b, cl
00761569  0F 86 84 00 00 00               jbe 0x1407615f3
0076156F  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00761579  48 8D 0D C8 61 6A 00            lea rcx, [rip + 0x6a61c8]
00761580  E8 1B D5 CC FF                  call 0x14042eaa0
00761585  84 C0                           test al, al
00761587  74 6A                           je 0x1407615f3
00761589  48 8D 45 E7                     lea rax, [rbp - 0x19]
0076158D  44 88 4D E7                     mov byte ptr [rbp - 0x19], r9b
00761591  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00761595  48 8D 15 A2 7F 8E FF            lea rdx, [rip - 0x71805e]
0076159C  48 8D 45 E8                     lea rax, [rbp - 0x18]
007615A0  44 88 45 E8                     mov byte ptr [rbp - 0x18], r8b
007615A4  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007615A8  48 8D 0D 99 61 6A 00            lea rcx, [rip + 0x6a6199]
007615AF  48 8D 45 EF                     lea rax, [rbp - 0x11]
007615B3  48 C7 45 1F 01 00 00 00         mov qword ptr [rbp + 0x1f], 1
007615BB  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007615BF  45 33 C9                        xor r9d, r9d
007615C2  48 8D 45 F7                     lea rax, [rbp - 9]
007615C6  48 C7 45 2F 01 00 00 00         mov qword ptr [rbp + 0x2f], 1
007615CE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007615D3  45 33 C0                        xor r8d, r8d
007615D6  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
007615DE  48 C7 45 EF 00 00 00 01         mov qword ptr [rbp - 0x11], 0x1000000
007615E6  48 C7 45 3F 08 00 00 00         mov qword ptr [rbp + 0x3f], 8
007615EE  E8 ED 4A CC FF                  call 0x1404260e0
007615F3  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
007615F7  48 33 CC                        xor rcx, rsp
007615FA  E8 41 B0 F4 FF                  call 0x1406ac640
007615FF  48 81 C4 A0 00 00 00            add rsp, 0xa0
00761606  5D                              pop rbp
00761607  C3                              ret
00761608  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceExternalDisplayState(unsigned __int8 a1, unsigned __int8 a2)
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
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m77;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6984171)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 6971877)) <= 5) goto loc_007615F3;
    result = tlgKeywordOn(v_rip + 6971848, a2, a2, a1);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m78;
        v_stack_m78 = a1;
        v_stack_m48 = result;
        a2 = v_rip - 7438430;
        result = v_stack_m77;
        v_stack_m77 = a2;
        v_stack_m38 = result;
        a1 = v_rip + 6971801;
        result = v_stack_m70;
        v_stack_m40 = 1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m30 = 1;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceExternalDisplayState(uint8_t Arg1, uint8_t Arg2)
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
    uint64_t v_stack_m5F;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m77;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x6A91EB)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x6A61E5)) <= 5) goto loc_007615F3;
    result = tlgKeywordOn(v_rip + 6971848, Arg2, Arg2, Arg1);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m78;
        v_stack_m78 = Arg1;
        v_stack_m48 = result;
        Arg2 = v_rip - 7438430;
        result = v_stack_m77;
        v_stack_m77 = Arg2;
        v_stack_m38 = result;
        Arg1 = v_rip + 6971801;
        result = v_stack_m70;
        v_stack_m40 = 1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m30 = 1;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m70 = 0x1000000ULL;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00761540&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00761540[BB_00761540]
  bb_0076156F[BB_0076156F]
  bb_00761589[BB_00761589]
  bb_007615F3[BB_007615F3]
  bb_00761608[BB_00761608]
  bb_00761540 -->|branch| bb_007615F3
  bb_00761540 -->|fallthrough| bb_0076156F
  bb_0076156F -->|branch| bb_007615F3
  bb_0076156F -->|fallthrough| bb_00761589
  bb_00761589 -->|flow| bb_007615F3
```
