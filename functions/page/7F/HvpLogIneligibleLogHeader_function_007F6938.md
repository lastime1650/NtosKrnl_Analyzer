# HvpLogIneligibleLogHeader

- RVA: `0x007F6938`–`0x007F69F4` (길이 `188` bytes)
- VA: `0x00000001407F6938`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `42`개 명령, `188/188` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007F696F` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007F69D9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007F69E5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00B2E3D0](../B2/Unknown_function_00B2E3D0.md) at `0x00B2E41F`

### Static image references
- `0x007F6946` → RVA `0x00E0A740` (`.data`; read)
- `0x007F6954` → RVA `0x00E09F58` (`.data`; read)
- `0x007F6984` → RVA `0x00057751` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007F696F` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007F69D9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007F69E5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F6938  40 55                           push rbp
007F693A  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
007F693F  48 81 EC A0 00 00 00            sub rsp, 0xa0
007F6946  48 8B 05 F3 3D 61 00            mov rax, qword ptr [rip + 0x613df3]
007F694D  48 33 C4                        xor rax, rsp
007F6950  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
007F6954  83 3D FD 35 61 00 05            cmp dword ptr [rip + 0x6135fd], 5
007F695B  44 8B CA                        mov r9d, edx
007F695E  44 8B D1                        mov r10d, ecx
007F6961  76 7B                           jbe 0x1407f69de
007F6963  BA 08 00 00 00                  mov edx, 8
007F6968  48 8D 0D E9 35 61 00            lea rcx, [rip + 0x6135e9]
007F696F  E8 2C 81 C3 FF                  call 0x14042eaa0
007F6974  84 C0                           test al, al
007F6976  74 66                           je 0x1407f69de
007F6978  48 8D 45 E7                     lea rax, [rbp - 0x19]
007F697C  44 89 4D EB                     mov dword ptr [rbp - 0x15], r9d
007F6980  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007F6984  48 8D 15 C6 0D 86 FF            lea rdx, [rip - 0x79f23a]
007F698B  48 8D 45 EB                     lea rax, [rbp - 0x15]
007F698F  44 89 45 EF                     mov dword ptr [rbp - 0x11], r8d
007F6993  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007F6997  48 8D 0D BA 35 61 00            lea rcx, [rip + 0x6135ba]
007F699E  48 8D 45 EF                     lea rax, [rbp - 0x11]
007F69A2  44 88 55 E7                     mov byte ptr [rbp - 0x19], r10b
007F69A6  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007F69AA  45 33 C9                        xor r9d, r9d
007F69AD  48 8D 45 F7                     lea rax, [rbp - 9]
007F69B1  48 C7 45 1F 01 00 00 00         mov qword ptr [rbp + 0x1f], 1
007F69B9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007F69BE  45 33 C0                        xor r8d, r8d
007F69C1  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
007F69C9  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
007F69D1  48 C7 45 3F 04 00 00 00         mov qword ptr [rbp + 0x3f], 4
007F69D9  E8 02 F7 C2 FF                  call 0x1404260e0
007F69DE  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
007F69E2  48 33 CC                        xor rcx, rsp
007F69E5  E8 56 5C EB FF                  call 0x1406ac640
007F69EA  48 81 C4 A0 00 00 00            add rsp, 0xa0
007F69F1  5D                              pop rbp
007F69F2  C3                              ret
007F69F3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpLogIneligibleLogHeader(int a1, int a2, int a3)
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
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6372851)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 6370813)) <= 5) goto loc_007F69DE;
    result = tlgKeywordOn(v_rip + 6370793, 8, a3, (unsigned int)(a2));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m78;
        v_stack_m74 = (unsigned int)((unsigned int)(a2));
        v_stack_m48 = result;
        a2 = v_rip - 7991866;
        result = v_stack_m74;
        v_stack_m70 = a3;
        v_stack_m38 = result;
        a1 = v_rip + 6370746;
        result = v_stack_m70;
        v_stack_m78 = (unsigned __int8)((unsigned int)(a1));
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m40 = 1;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m30 = 4;
        v_stack_m20 = 4;
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
int64_t HvpLogIneligibleLogHeader(int32_t Arg1, int32_t Arg2, int32_t Arg3)
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
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x613DF3)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x6135FD)) <= 5) goto loc_007F69DE;
    result = tlgKeywordOn(v_rip + 6370793, 8, Arg3, (uint32_t)(Arg2));
    if ((uint8_t)(result) != 0) {
        result = v_stack_m78;
        v_stack_m74 = (uint32_t)((uint32_t)(Arg2));
        v_stack_m48 = result;
        Arg2 = v_rip - 7991866;
        result = v_stack_m74;
        v_stack_m70 = Arg3;
        v_stack_m38 = result;
        Arg1 = v_rip + 6370746;
        result = v_stack_m70;
        v_stack_m78 = (uint8_t)((uint32_t)(Arg1));
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m40 = 1;
        v_stack_m80 = result;
        Arg3 = 0;
        v_stack_m88 = 5;
        v_stack_m30 = 4;
        v_stack_m20 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F6938&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F6938[BB_007F6938]
  bb_007F6963[BB_007F6963]
  bb_007F6978[BB_007F6978]
  bb_007F69DE[BB_007F69DE]
  bb_007F69F3[BB_007F69F3]
  bb_007F6938 -->|branch| bb_007F69DE
  bb_007F6938 -->|fallthrough| bb_007F6963
  bb_007F6963 -->|branch| bb_007F69DE
  bb_007F6963 -->|fallthrough| bb_007F6978
  bb_007F6978 -->|flow| bb_007F69DE
```
