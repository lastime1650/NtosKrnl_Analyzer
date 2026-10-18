# TtmiLogTerminalCleanup

- RVA: `0x0077BA08`–`0x0077BAC4` (길이 `188` bytes)
- VA: `0x000000014077BA08`
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
- `0x0077BA3F` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x0077BAA9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x0077BAB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [TtmiSessionTerminalListWorker](TtmiSessionTerminalListWorker_function_0077CE14.md) at `0x0077CE98`

### Static image references
- `0x0077BA16` → RVA `0x00E0A740` (`.data`; read)
- `0x0077BA24` → RVA `0x00FD88C8` (`PAGEDATA`; read)
- `0x0077BA54` → RVA `0x000513D6` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0077BA3F` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x0077BAA9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x0077BAB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077BA08  40 55                           push rbp
0077BA0A  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0077BA0F  48 81 EC A0 00 00 00            sub rsp, 0xa0
0077BA16  48 8B 05 23 ED 68 00            mov rax, qword ptr [rip + 0x68ed23]
0077BA1D  48 33 C4                        xor rax, rsp
0077BA20  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0077BA24  83 3D 9D CE 85 00 05            cmp dword ptr [rip + 0x85ce9d], 5
0077BA2B  44 8B CA                        mov r9d, edx
0077BA2E  4C 8B D1                        mov r10, rcx
0077BA31  76 7B                           jbe 0x14077baae
0077BA33  BA 01 00 00 00                  mov edx, 1
0077BA38  48 8D 0D 89 CE 85 00            lea rcx, [rip + 0x85ce89]
0077BA3F  E8 5C 30 CB FF                  call 0x14042eaa0
0077BA44  84 C0                           test al, al
0077BA46  74 66                           je 0x14077baae
0077BA48  48 8D 45 E7                     lea rax, [rbp - 0x19]
0077BA4C  44 89 4D E7                     mov dword ptr [rbp - 0x19], r9d
0077BA50  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0077BA54  48 8D 15 7B 59 8D FF            lea rdx, [rip - 0x72a685]
0077BA5B  48 8D 45 EB                     lea rax, [rbp - 0x15]
0077BA5F  44 89 45 EB                     mov dword ptr [rbp - 0x15], r8d
0077BA63  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0077BA67  48 8D 0D 5A CE 85 00            lea rcx, [rip + 0x85ce5a]
0077BA6E  48 8D 45 EF                     lea rax, [rbp - 0x11]
0077BA72  48 C7 45 1F 04 00 00 00         mov qword ptr [rbp + 0x1f], 4
0077BA7A  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0077BA7E  45 33 C9                        xor r9d, r9d
0077BA81  48 8D 45 F7                     lea rax, [rbp - 9]
0077BA85  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
0077BA8D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0077BA92  45 33 C0                        xor r8d, r8d
0077BA95  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
0077BA9D  4C 89 55 EF                     mov qword ptr [rbp - 0x11], r10
0077BAA1  48 C7 45 3F 08 00 00 00         mov qword ptr [rbp + 0x3f], 8
0077BAA9  E8 32 A6 CA FF                  call 0x1404260e0
0077BAAE  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0077BAB2  48 33 CC                        xor rcx, rsp
0077BAB5  E8 86 0B F3 FF                  call 0x1406ac640
0077BABA  48 81 C4 A0 00 00 00            add rsp, 0xa0
0077BAC1  5D                              pop rbp
0077BAC2  C3                              ret
0077BAC3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmiLogTerminalCleanup(__int64 a1, int a2, int a3)
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
    unsigned __int64 v_stack_m74;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6876451)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 8769181)) <= 5) goto loc_0077BAAE;
    result = tlgKeywordOn(v_rip + 8769161, 1, a3, (unsigned int)(a2));
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_m78;
        v_stack_m78 = (unsigned int)((unsigned int)(a2));
        v_stack_m48 = result;
        a2 = v_rip - 7513733;
        result = v_stack_m74;
        v_stack_m74 = a3;
        v_stack_m38 = result;
        a1 = v_rip + 8769114;
        result = v_stack_m70;
        v_stack_m40 = 4;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m30 = 4;
        v_stack_m80 = result;
        a3 = 0;
        v_stack_m88 = 5;
        v_stack_m70 = a1;
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
int64_t TtmiLogTerminalCleanup(int64_t Arg1, int32_t Arg2, int32_t Arg3)
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
    uint64_t v_stack_m74;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x68ED23)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x85CE9D)) <= 5) goto loc_0077BAAE;
    result = tlgKeywordOn(v_rip + 8769161, 1, Arg3, (uint32_t)(Arg2));
    if ((uint8_t)(result) != 0) {
        result = v_stack_m78;
        v_stack_m78 = (uint32_t)((uint32_t)(Arg2));
        v_stack_m48 = result;
        Arg2 = v_rip - 7513733;
        result = v_stack_m74;
        v_stack_m74 = Arg3;
        v_stack_m38 = result;
        Arg1 = v_rip + 8769114;
        result = v_stack_m70;
        v_stack_m40 = 4;
        v_stack_m28 = result;
        a4 = 0;
        result = v_stack_m68;
        v_stack_m30 = 4;
        v_stack_m80 = result;
        Arg3 = 0;
        v_stack_m88 = 5;
        v_stack_m70 = Arg1;
        v_stack_m20 = 8;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077BA08&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077BA08[BB_0077BA08]
  bb_0077BA33[BB_0077BA33]
  bb_0077BA48[BB_0077BA48]
  bb_0077BAAE[BB_0077BAAE]
  bb_0077BAC3[BB_0077BAC3]
  bb_0077BA08 -->|branch| bb_0077BAAE
  bb_0077BA08 -->|fallthrough| bb_0077BA33
  bb_0077BA33 -->|branch| bb_0077BAAE
  bb_0077BA33 -->|fallthrough| bb_0077BA48
  bb_0077BA48 -->|flow| bb_0077BAAE
```
