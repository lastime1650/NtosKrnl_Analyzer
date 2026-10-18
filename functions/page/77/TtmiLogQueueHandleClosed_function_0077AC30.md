# TtmiLogQueueHandleClosed

- RVA: `0x0077AC30`–`0x0077ACEC` (길이 `188` bytes)
- VA: `0x000000014077AC30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079278`
- 디코드: `42`개 명령, `188/188` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0077AC67` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077ACD1` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077ACDD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmpCloseQueueHandle](TtmpCloseQueueHandle_function_0077DF80.md) at `0x0077DF9E`

### Static image references
- `0x0077AC3E` → RVA `0x00E0A740` (`.data`; read)
- `0x0077AC4C` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077AC7C` → RVA `0x000515C4` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077AC67` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077ACD1` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077ACDD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077AC30  40 55                           push rbp
0077AC32  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0077AC37  48 81 EC B0 00 00 00            sub rsp, 0xb0
0077AC3E  48 8B 05 FB FA 68 00            mov rax, qword ptr [rip + 0x68fafb]
0077AC45  48 33 C4                        xor rax, rsp
0077AC48  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077AC4C  83 3D 75 DC 85 00 05            cmp dword ptr [rip + 0x85dc75], 5
0077AC53  4C 8B CA                        mov r9, rdx
0077AC56  4C 8B D1                        mov r10, rcx
0077AC59  76 7B                           jbe 0x14077acd6
0077AC5B  BA 01 00 00 00                  mov edx, 1
0077AC60  48 8D 0D 61 DC 85 00            lea rcx, [rip + 0x85dc61]
0077AC67  E8 34 3E CB FF                  call 0x14042eaa0
0077AC6C  84 C0                           test al, al
0077AC6E  74 66                           je 0x14077acd6
0077AC70  48 8D 45 D7                     lea rax, [rbp - 0x29]
0077AC74  4C 89 4D DF                     mov qword ptr [rbp - 0x21], r9
0077AC78  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077AC7C  48 8D 15 41 69 8D FF            lea rdx, [rip - 0x7296bf]
0077AC83  48 8D 45 DF                     lea rax, [rbp - 0x21]
0077AC87  4C 89 45 E7                     mov qword ptr [rbp - 0x19], r8
0077AC8B  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077AC8F  48 8D 0D 32 DC 85 00            lea rcx, [rip + 0x85dc32]
0077AC96  48 8D 45 E7                     lea rax, [rbp - 0x19]
0077AC9A  4C 89 55 D7                     mov qword ptr [rbp - 0x29], r10
0077AC9E  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077ACA2  45 33 C9                        xor r9d, r9d
0077ACA5  48 8D 45 F7                     lea rax, [rbp - 9]
0077ACA9  48 C7 45 1F 08 00 00 00         mov qword ptr [rbp + 0x1f], 8
0077ACB1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077ACB6  45 33 C0                        xor r8d, r8d
0077ACB9  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
0077ACC1  48 C7 45 2F 08 00 00 00         mov qword ptr [rbp + 0x2f], 8
0077ACC9  48 C7 45 3F 08 00 00 00         mov qword ptr [rbp + 0x3f], 8
0077ACD1  E8 0A B4 CA FF                  call 0x1404260e0
0077ACD6  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077ACDA  48 33 CC                        xor rcx, rsp
0077ACDD  E8 5E 19 F3 FF                  call 0x1406ac640
0077ACE2  48 81 C4 B0 00 00 00            add rsp, 0xb0
0077ACE9  5D                              pop rbp
0077ACEA  C3                              ret
0077ACEB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogQueueHandleClosed(__int64 a1, __int64 a2, __int64 a3)
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
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m98;

    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 6879995)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8772725)) <= 5) goto loc_0077ACD6;
    result = tlgKeywordOn(v_rip + 8772705, 1, a3, a2);
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m88;
        v_stack_m80 = a2;
        v_stack_m48 = result;
        a2 = v_rip - 7509695;
        result = v_stack_m80;
        v_stack_m78 = a3;
        v_stack_m38 = result;
        a1 = v_rip + 8772658;
        result = v_stack_m78;
        v_stack_m88 = a1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m40 = 8;
        v_stack_m90 = result;
        a3 = 0;
        v_stack_m98 = 5;
        v_stack_m30 = 8;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmiLogQueueHandleClosed(int64_t Arg1, int64_t Arg2, int64_t Arg3)
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
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m98;

    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x68FAFB)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85DC75)) <= 5) goto loc_0077ACD6;
    result = tlgKeywordOn(v_rip + 8772705, 1, Arg3, Arg2);
    if ((uint8_t)(result) != 0) {
        result = v_stack_m88;
        v_stack_m80 = Arg2;
        v_stack_m48 = result;
        Arg2 = v_rip - 7509695;
        result = v_stack_m80;
        v_stack_m78 = Arg3;
        v_stack_m38 = result;
        Arg1 = v_rip + 8772658;
        result = v_stack_m78;
        v_stack_m88 = Arg1;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m40 = 8;
        v_stack_m90 = result;
        Arg3 = 0;
        v_stack_m98 = 5;
        v_stack_m30 = 8;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077AC30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077AC30[BB_0077AC30]
  bb_0077AC5B[BB_0077AC5B]
  bb_0077AC70[BB_0077AC70]
  bb_0077ACD6[BB_0077ACD6]
  bb_0077ACEB[BB_0077ACEB]
  bb_0077AC30 -->|branch| bb_0077ACD6
  bb_0077AC30 -->|fallthrough| bb_0077AC5B
  bb_0077AC5B -->|branch| bb_0077ACD6
  bb_0077AC5B -->|fallthrough| bb_0077AC70
  bb_0077AC70 -->|flow| bb_0077ACD6
```
