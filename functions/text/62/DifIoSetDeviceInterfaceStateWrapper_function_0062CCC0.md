# DifIoSetDeviceInterfaceStateWrapper

- RVA: `0x0062CCC0`–`0x0062CE24` (길이 `356` bytes)
- VA: `0x000000014062CCC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00093E28`
- 디코드: `98`개 명령, `356/356` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062CCEE` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062CD16` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062CD49` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062CD70` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062CD89` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062CD94` → [IoSetDeviceInterfaceState](../../page/95/IoSetDeviceInterfaceState_function_00950740.md) (function, `0x00950740`)
- `0x0062CDC1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062CDE8` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062CE01` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062CD28` → RVA `0x00F048B8` (`.data`; read)
- `0x0062CD36` → RVA `0x00F04980` (`.data`; read)
- `0x0062CD42` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0062CD94` → [IoSetDeviceInterfaceState](../../page/95/IoSetDeviceInterfaceState_function_00950740.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062CCC0  48 8B C4                        mov rax, rsp
0062CCC3  48 89 58 08                     mov qword ptr [rax + 8], rbx
0062CCC7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
0062CCCB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0062CCCF  57                              push rdi
0062CCD0  41 56                           push r14
0062CCD2  41 57                           push r15
0062CCD4  48 83 EC 40                     sub rsp, 0x40
0062CCD8  0F 57 C0                        xorps xmm0, xmm0
0062CCDB  4C 8B F9                        mov r15, rcx
0062CCDE  B9 39 01 00 00                  mov ecx, 0x139
0062CCE3  44 8A F2                        mov r14b, dl
0062CCE6  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
0062CCEA  0F 11 40 D8                     movups xmmword ptr [rax - 0x28], xmm0
0062CCEE  E8 41 8D E6 FF                  call 0x140495a34
0062CCF3  48 8B F0                        mov rsi, rax
0062CCF6  48 85 C0                        test rax, rax
0062CCF9  0F 84 8F 00 00 00               je 0x14062cd8e
0062CCFF  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062CD02  A8 18                           test al, 0x18
0062CD04  74 0C                           je 0x14062cd12
0062CD06  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
0062CD0B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062CD10  EB 0E                           jmp 0x14062cd20
0062CD12  A8 04                           test al, 4
0062CD14  74 0A                           je 0x14062cd20
0062CD16  E8 ED 6E EA FF                  call 0x1404d3c08
0062CD1B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062CD20  40 32 ED                        xor bpl, bpl
0062CD23  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0062CD28  40 38 2D 89 7B 8D 00            cmp byte ptr [rip + 0x8d7b89], bpl
0062CD2F  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
0062CD34  75 0C                           jne 0x14062cd42
0062CD36  F7 05 40 7C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d7c40], 0x800
0062CD40  74 13                           je 0x14062cd55
0062CD42  48 8D 0D 37 71 8D 00            lea rcx, [rip + 0x8d7137]
0062CD49  E8 D2 98 BE FF                  call 0x140216620
0062CD4E  40 8A E8                        mov bpl, al
0062CD51  84 C0                           test al, al
0062CD53  74 39                           je 0x14062cd8e
0062CD55  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0062CD59  48 8B 1F                        mov rbx, qword ptr [rdi]
0062CD5C  EB 1A                           jmp 0x14062cd78
0062CD5E  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062CD62  48 85 C0                        test rax, rax
0062CD65  74 0E                           je 0x14062cd75
0062CD67  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062CD6B  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062CD70  E8 5B DD 08 00                  call 0x1406baad0
0062CD75  48 8B 1B                        mov rbx, qword ptr [rbx]
0062CD78  48 3B DF                        cmp rbx, rdi
0062CD7B  75 E1                           jne 0x14062cd5e
0062CD7D  40 84 ED                        test bpl, bpl
0062CD80  74 0C                           je 0x14062cd8e
0062CD82  48 8D 0D F7 70 8D 00            lea rcx, [rip + 0x8d70f7]
0062CD89  E8 F2 D0 D1 FF                  call 0x140349e80
0062CD8E  41 8A D6                        mov dl, r14b
0062CD91  49 8B CF                        mov rcx, r15
0062CD94  E8 A7 39 32 00                  call 0x140950740
0062CD99  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0062CD9D  48 85 F6                        test rsi, rsi
0062CDA0  74 64                           je 0x14062ce06
0062CDA2  40 32 FF                        xor dil, dil
0062CDA5  40 38 3D 0C 7B 8D 00            cmp byte ptr [rip + 0x8d7b0c], dil
0062CDAC  75 0C                           jne 0x14062cdba
0062CDAE  F7 05 C8 7B 8D 00 00 08 00 00   test dword ptr [rip + 0x8d7bc8], 0x800
0062CDB8  74 13                           je 0x14062cdcd
0062CDBA  48 8D 0D BF 70 8D 00            lea rcx, [rip + 0x8d70bf]
0062CDC1  E8 5A 98 BE FF                  call 0x140216620
0062CDC6  40 8A F8                        mov dil, al
0062CDC9  84 C0                           test al, al
0062CDCB  74 39                           je 0x14062ce06
0062CDCD  48 83 C6 30                     add rsi, 0x30
0062CDD1  48 8B 1E                        mov rbx, qword ptr [rsi]
0062CDD4  EB 1A                           jmp 0x14062cdf0
0062CDD6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062CDDA  48 85 C0                        test rax, rax
0062CDDD  74 0E                           je 0x14062cded
0062CDDF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062CDE3  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062CDE8  E8 E3 DC 08 00                  call 0x1406baad0
0062CDED  48 8B 1B                        mov rbx, qword ptr [rbx]
0062CDF0  48 3B DE                        cmp rbx, rsi
0062CDF3  75 E1                           jne 0x14062cdd6
0062CDF5  40 84 FF                        test dil, dil
0062CDF8  74 0C                           je 0x14062ce06
0062CDFA  48 8D 0D 7F 70 8D 00            lea rcx, [rip + 0x8d707f]
0062CE01  E8 7A D0 D1 FF                  call 0x140349e80
0062CE06  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0062CE0A  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
0062CE0F  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
0062CE14  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
0062CE19  48 83 C4 40                     add rsp, 0x40
0062CE1D  41 5F                           pop r15
0062CE1F  41 5E                           pop r14
0062CE21  5F                              pop rdi
0062CE22  C3                              ret
0062CE23  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoSetDeviceInterfaceStateWrapper(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 40) = v_xmm0;
    result = DifGetAPIThunkContextById(313, a2, a3, a4);
    if (result == 0) goto loc_0062CD8E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062CD12;
    v_stack_m38 = v_stack_p0;
    goto loc_0062CD20;
loc_0062CD12:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m38 = result;
    }
    v_rbp = 0;
    v_stack_m28 = a1;
    v_stack_m30 = a2;
    if ((*(unsigned __int8 *)(v_rip + 9272201)) != 0) goto loc_0062CD42;
    if (((*(unsigned int *)(v_rip + 9272384)) & (0x800ULL)) == 0) goto loc_0062CD55;
loc_0062CD42:
    result = ExAcquireRundownProtection(v_rip + 9269559, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062CD8E;
loc_0062CD55:
    goto loc_0062CD78;
loc_0062CD5E:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062CD78:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062CD5E;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9269495;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoSetDeviceInterfaceState(a1, a2, a3, a4);
    v_stack_m20 = (unsigned int)(result);
    if (result == 0) goto loc_0062CE06;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9272076)) != 0) goto loc_0062CDBA;
    if (((*(unsigned int *)(v_rip + 9272264)) & (0x800ULL)) == 0) goto loc_0062CDCD;
loc_0062CDBA:
    result = ExAcquireRundownProtection(v_rip + 9269439, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062CE06;
loc_0062CDCD:
    v_rsi = (result) + (48);
    goto loc_0062CDF0;
loc_0062CDD6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m38;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062CDF0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062CDD6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9269375;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m20);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoSetDeviceInterfaceStateWrapper(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x28) = v_xmm0;
    result = DifGetAPIThunkContextById(313, Arg2, a3, a4);
    if (result == 0) goto loc_0062CD8E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062CD12;
    v_stack_m38 = v_stack_p0;
    goto loc_0062CD20;
loc_0062CD12:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, a3, a4);
        v_stack_m38 = result;
    }
    local_rbp = 0;
    v_stack_m28 = Arg1;
    v_stack_m30 = Arg2;
    if ((*(uint8_t *)(v_rip + 0x8D7B89)) != 0) goto loc_0062CD42;
    if (((*(uint32_t *)(v_rip + 0x8D7C40)) & (0x800ULL)) == 0) goto loc_0062CD55;
loc_0062CD42:
    result = ExAcquireRundownProtection(v_rip + 9269559, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062CD8E;
loc_0062CD55:
    goto loc_0062CD78;
loc_0062CD5E:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062CD78:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062CD5E;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9269495;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    result = IoSetDeviceInterfaceState(Arg1, Arg2, a3, a4);
    v_stack_m20 = (uint32_t)(result);
    if (result == 0) goto loc_0062CE06;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D7B0C)) != 0) goto loc_0062CDBA;
    if (((*(uint32_t *)(v_rip + 0x8D7BC8)) & (0x800ULL)) == 0) goto loc_0062CDCD;
loc_0062CDBA:
    result = ExAcquireRundownProtection(v_rip + 9269439, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062CE06;
loc_0062CDCD:
    local_rsi = (result) + (48);
    goto loc_0062CDF0;
loc_0062CDD6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m38;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
loc_0062CDF0:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062CDD6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9269375;
        result = ExReleaseRundownProtection(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m20);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062CCC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062CCC0[BB_0062CCC0]
  bb_0062CCFF[BB_0062CCFF]
  bb_0062CD06[BB_0062CD06]
  bb_0062CD12[BB_0062CD12]
  bb_0062CD16[BB_0062CD16]
  bb_0062CD20[BB_0062CD20]
  bb_0062CD36[BB_0062CD36]
  bb_0062CD42[BB_0062CD42]
  bb_0062CD55[BB_0062CD55]
  bb_0062CD5E[BB_0062CD5E]
  bb_0062CD67[BB_0062CD67]
  bb_0062CD75[BB_0062CD75]
  bb_0062CD78[BB_0062CD78]
  bb_0062CD7D[BB_0062CD7D]
  bb_0062CD82[BB_0062CD82]
  bb_0062CD8E[BB_0062CD8E]
  bb_0062CDA2[BB_0062CDA2]
  bb_0062CDAE[BB_0062CDAE]
  bb_0062CDBA[BB_0062CDBA]
  bb_0062CDCD[BB_0062CDCD]
  bb_0062CDD6[BB_0062CDD6]
  bb_0062CDDF[BB_0062CDDF]
  bb_0062CDED[BB_0062CDED]
  bb_0062CDF0[BB_0062CDF0]
  bb_0062CDF5[BB_0062CDF5]
  bb_0062CDFA[BB_0062CDFA]
  bb_0062CE06[BB_0062CE06]
  bb_0062CE23[BB_0062CE23]
  bb_0062CCC0 -->|branch| bb_0062CD8E
  bb_0062CCC0 -->|fallthrough| bb_0062CCFF
  bb_0062CCFF -->|branch| bb_0062CD12
  bb_0062CCFF -->|fallthrough| bb_0062CD06
  bb_0062CD06 -->|branch| bb_0062CD20
  bb_0062CD12 -->|branch| bb_0062CD20
  bb_0062CD12 -->|fallthrough| bb_0062CD16
  bb_0062CD16 -->|flow| bb_0062CD20
  bb_0062CD20 -->|branch| bb_0062CD42
  bb_0062CD20 -->|fallthrough| bb_0062CD36
  bb_0062CD36 -->|branch| bb_0062CD55
  bb_0062CD36 -->|fallthrough| bb_0062CD42
  bb_0062CD42 -->|branch| bb_0062CD8E
  bb_0062CD42 -->|fallthrough| bb_0062CD55
  bb_0062CD55 -->|branch| bb_0062CD78
  bb_0062CD5E -->|branch| bb_0062CD75
  bb_0062CD5E -->|fallthrough| bb_0062CD67
  bb_0062CD67 -->|flow| bb_0062CD75
  bb_0062CD75 -->|flow| bb_0062CD78
  bb_0062CD78 -->|branch| bb_0062CD5E
  bb_0062CD78 -->|fallthrough| bb_0062CD7D
  bb_0062CD7D -->|branch| bb_0062CD8E
  bb_0062CD7D -->|fallthrough| bb_0062CD82
  bb_0062CD82 -->|flow| bb_0062CD8E
  bb_0062CD8E -->|branch| bb_0062CE06
  bb_0062CD8E -->|fallthrough| bb_0062CDA2
  bb_0062CDA2 -->|branch| bb_0062CDBA
  bb_0062CDA2 -->|fallthrough| bb_0062CDAE
  bb_0062CDAE -->|branch| bb_0062CDCD
  bb_0062CDAE -->|fallthrough| bb_0062CDBA
  bb_0062CDBA -->|branch| bb_0062CE06
  bb_0062CDBA -->|fallthrough| bb_0062CDCD
  bb_0062CDCD -->|branch| bb_0062CDF0
  bb_0062CDD6 -->|branch| bb_0062CDED
  bb_0062CDD6 -->|fallthrough| bb_0062CDDF
  bb_0062CDDF -->|flow| bb_0062CDED
  bb_0062CDED -->|flow| bb_0062CDF0
  bb_0062CDF0 -->|branch| bb_0062CDD6
  bb_0062CDF0 -->|fallthrough| bb_0062CDF5
  bb_0062CDF5 -->|branch| bb_0062CE06
  bb_0062CDF5 -->|fallthrough| bb_0062CDFA
  bb_0062CDFA -->|flow| bb_0062CE06
```
