# KsepDsEventPoolAllocate

- RVA: `0x005CD0D0`–`0x005CD1C5` (길이 `245` bytes)
- VA: `0x00000001405CD0D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB558`
- 디코드: `57`개 명령, `245/245` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005CD114` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x005CD1AA` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x005CD1B6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KseDsHookExAllocatePool](KseDsHookExAllocatePool_function_005CC3D0.md) at `0x005CC409`
- [KseDsHookExAllocatePoolWithTag](KseDsHookExAllocatePoolWithTag_function_005CC430.md) at `0x005CC46D`

### Static image references
- `0x005CD0EF` → RVA `0x00E0A740` (`.data`; read)
- `0x005CD0FD` → RVA `0x00E66CE0` (`.data`; read)
- `0x005CD10D` → RVA `0x00021BC8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CD0D0  48 8B C4                        mov rax, rsp
005CD0D3  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
005CD0D7  44 89 40 18                     mov dword ptr [rax + 0x18], r8d
005CD0DB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
005CD0DF  48 89 48 08                     mov qword ptr [rax + 8], rcx
005CD0E3  55                              push rbp
005CD0E4  48 8D 68 A9                     lea rbp, [rax - 0x57]
005CD0E8  48 81 EC A0 00 00 00            sub rsp, 0xa0
005CD0EF  48 8B 05 4A D6 83 00            mov rax, qword ptr [rip + 0x83d64a]
005CD0F6  48 33 C4                        xor rax, rsp
005CD0F9  48 89 45 3F                     mov qword ptr [rbp + 0x3f], rax
005CD0FD  48 8B 0D DC 9B 89 00            mov rcx, qword ptr [rip + 0x899bdc]
005CD104  48 85 C9                        test rcx, rcx
005CD107  0F 84 A2 00 00 00               je 0x1405cd1af
005CD10D  48 8D 15 B4 4A A5 FF            lea rdx, [rip - 0x5ab54c]
005CD114  E8 37 53 DC FF                  call 0x140392450
005CD119  84 C0                           test al, al
005CD11B  0F 84 8E 00 00 00               je 0x1405cd1af
005CD121  83 65 FB 00                     and dword ptr [rbp - 5], 0
005CD125  48 8D 45 5F                     lea rax, [rbp + 0x5f]
005CD129  83 65 0B 00                     and dword ptr [rbp + 0xb], 0
005CD12D  48 8D 15 94 4A A5 FF            lea rdx, [rip - 0x5ab56c]
005CD134  83 65 1B 00                     and dword ptr [rbp + 0x1b], 0
005CD138  41 B8 08 00 00 00               mov r8d, 8
005CD13E  83 65 2B 00                     and dword ptr [rbp + 0x2b], 0
005CD142  45 33 C9                        xor r9d, r9d
005CD145  83 65 3B 00                     and dword ptr [rbp + 0x3b], 0
005CD149  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
005CD14D  48 8D 45 67                     lea rax, [rbp + 0x67]
005CD151  48 89 45 FF                     mov qword ptr [rbp - 1], rax
005CD155  41 8D 48 FC                     lea ecx, [r8 - 4]
005CD159  48 8D 45 6F                     lea rax, [rbp + 0x6f]
005CD15D  44 89 45 F7                     mov dword ptr [rbp - 9], r8d
005CD161  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
005CD165  48 8D 45 77                     lea rax, [rbp + 0x77]
005CD169  48 89 45 1F                     mov qword ptr [rbp + 0x1f], rax
005CD16D  48 8D 45 7F                     lea rax, [rbp + 0x7f]
005CD171  48 89 45 2F                     mov qword ptr [rbp + 0x2f], rax
005CD175  48 8D 45 EF                     lea rax, [rbp - 0x11]
005CD179  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005CD17E  C7 44 24 30 05 00 00 00         mov dword ptr [rsp + 0x30], 5
005CD186  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
005CD18C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005CD192  44 89 45 07                     mov dword ptr [rbp + 7], r8d
005CD196  89 4D 17                        mov dword ptr [rbp + 0x17], ecx
005CD199  44 89 45 27                     mov dword ptr [rbp + 0x27], r8d
005CD19D  45 33 C0                        xor r8d, r8d
005CD1A0  89 4D 37                        mov dword ptr [rbp + 0x37], ecx
005CD1A3  48 8B 0D 36 9B 89 00            mov rcx, qword ptr [rip + 0x899b36]
005CD1AA  E8 21 1F C9 FF                  call 0x14025f0d0
005CD1AF  48 8B 4D 3F                     mov rcx, qword ptr [rbp + 0x3f]
005CD1B3  48 33 CC                        xor rcx, rsp
005CD1B6  E8 85 F4 0D 00                  call 0x1406ac640
005CD1BB  48 81 C4 A0 00 00 00            add rsp, 0xa0
005CD1C2  5D                              pop rbp
005CD1C3  C3                              ret
005CD1C4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDsEventPoolAllocate(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 8640074)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 87 + 63) = result;
    if (*(unsigned __int64 *)(v_rip + 9018332) == 0) goto loc_005CD1AF;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 9018332), v_rip - 5944652, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = v_rsp - 87 + 95;
        a2 = v_rip - 5944684;
        a3 = 8;
        a4 = 0;
        *(unsigned __int64 *)(v_rsp - 87 - 17) = result;
        result = v_rsp - 87 + 103;
        *(unsigned __int64 *)(v_rsp - 87 - 1) = result;
        a1 = a3 - 4;
        result = v_rsp - 87 + 111;
        *(unsigned int *)(v_rsp - 87 - 9) = a3;
        *(unsigned __int64 *)(v_rsp - 87 + 15) = result;
        result = v_rsp - 87 + 119;
        *(unsigned __int64 *)(v_rsp - 87 + 31) = result;
        result = v_rsp - 87 + 127;
        *(unsigned __int64 *)(v_rsp - 87 + 47) = result;
        result = v_rsp - 87 - 17;
        v_stack_m70 = result;
        v_stack_m78 = 5;
        *(unsigned int *)(v_rsp - 87 + 7) = a3;
        *(unsigned int *)(v_rsp - 87 + 23) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 87 + 39) = a3;
        a3 = 0;
        *(unsigned int *)(v_rsp - 87 + 55) = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 9018166);
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 87 + 63)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDsEventPoolAllocate(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x83D64A)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x57 + 0x3F) = result;
    if (*(uint64_t *)(v_rip + 0x899BDC) == 0) goto loc_005CD1AF;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x899BDC), v_rip - 5944652, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = local_rsp - 87 + 95;
        Arg2 = v_rip - 5944684;
        Arg3 = 8;
        Arg4 = 0;
        *(uint64_t *)(local_rsp - 0x57 - 0x11) = result;
        result = local_rsp - 87 + 103;
        *(uint64_t *)(local_rsp - 0x57 - 0x1) = result;
        Arg1 = Arg3 - 4;
        result = local_rsp - 87 + 111;
        *(uint32_t *)(local_rsp - 0x57 - 0x9) = Arg3;
        *(uint64_t *)(local_rsp - 0x57 + 0xF) = result;
        result = local_rsp - 87 + 119;
        *(uint64_t *)(local_rsp - 0x57 + 0x1F) = result;
        result = local_rsp - 87 + 127;
        *(uint64_t *)(local_rsp - 0x57 + 0x2F) = result;
        result = local_rsp - 87 - 17;
        v_stack_m70 = result;
        v_stack_m78 = 5;
        *(uint32_t *)(local_rsp - 0x57 + 0x7) = Arg3;
        *(uint32_t *)(local_rsp - 0x57 + 0x17) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0x57 + 0x27) = Arg3;
        Arg3 = 0;
        *(uint32_t *)(local_rsp - 0x57 + 0x37) = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0x899B36);
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0x57 + 0x3F)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CD0D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CD0D0[BB_005CD0D0]
  bb_005CD10D[BB_005CD10D]
  bb_005CD121[BB_005CD121]
  bb_005CD1AF[BB_005CD1AF]
  bb_005CD1C4[BB_005CD1C4]
  bb_005CD0D0 -->|branch| bb_005CD1AF
  bb_005CD0D0 -->|fallthrough| bb_005CD10D
  bb_005CD10D -->|branch| bb_005CD1AF
  bb_005CD10D -->|fallthrough| bb_005CD121
  bb_005CD121 -->|flow| bb_005CD1AF
```
